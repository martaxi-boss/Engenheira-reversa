#!/usr/bin/env python3
"""Audita em leitura o checkout final instalado. Nao instala, remove ou inicia servicos."""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

PIN = "160d821ac9a0310afcb8d1fc427862dd6508add5"
URL = "https://github.com/morluto/rea.git"
CANONICAL = Path("/home/ubuntu/rea-original-upstream-680")
EVIDENCE = Path("/home/ubuntu/rea-original-upstream-680-evidence")
LEGACY = Path("/opt/rea-reversa/rea")
FINAL_RUNTIME = Path("/home/ubuntu/rea-final-runtime")
EXPECTED_BINARIES = {
    "dist/process/ProcessOwnership.js": "2171c79dfa0e49c8836cef350c966746ceb90b246a2d678b2e98578167aff852",
    "dist/process/ProcessOwnershipObservation.js": "81b1aaeded14556d884adaffa570cef41909deb01f76fc25a2d7bd0f9a775655",
}


def git_read(root, *args):
    p = subprocess.run(["git", "-C", str(root), *args], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, text=True, timeout=10, check=False)
    return p.stdout.strip() if p.returncode == 0 else None


def sha256_file(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def inventory(root=CANONICAL, evidence=EVIDENCE, legacy=LEGACY):
    r = {
        "project": "engenharia-reversa-final",
        "source_root": str(root),
        "source_expected_commit": PIN,
        "source": "NOT_TESTED",
        "dependency_isolation": "NOT_TESTED",
        "providers": "NOT_TESTED",
        "legacy_retirement_completed": not legacy.parent.exists(),
        "changes_made": False,
        "observations": {},
    }
    if root.is_symlink() or not root.is_dir():
        r["source"] = "BLOCKED_ROOT_UNAVAILABLE"
        return r
    commit = git_read(root, "rev-parse", "HEAD")
    url = git_read(root, "remote", "get-url", "origin")
    pkg = {}
    try:
        pkg = json.loads((root / "package.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        pass
    r["observations"]["commit"] = commit
    r["observations"]["origin"] = url
    r["observations"]["package_version"] = pkg.get("version")
    hashes = {}
    for name, expected in EXPECTED_BINARIES.items():
        path = root / name
        try:
            actual = sha256_file(path) if path.is_file() else None
        except OSError:
            actual = None
        hashes[name] = {"present": actual is not None, "matches_tested": actual == expected}
    r["observations"]["compiled"] = hashes
    valid = commit == PIN and url == URL and pkg.get("name") == "rea-agents" and pkg.get("version") == "6.8.0"
    valid = valid and all(item["matches_tested"] for item in hashes.values())
    r["source"] = "PASS" if valid else "FAIL_OR_NOT_PROVEN"
    deps = root / "node_modules"
    if deps.is_symlink():
        dest = deps.resolve(strict=False)
        r["observations"]["node_modules"] = {"kind": "symlink", "target": str(dest)}
        if dest == (legacy / "node_modules").resolve(strict=False):
            r["dependency_isolation"] = "BLOCKED_SHARED_LEGACY"
        elif dest == (FINAL_RUNTIME / "node_modules").resolve(strict=False) and dest.is_dir():
            r["dependency_isolation"] = "FINAL_RUNTIME_COPY_PRESENT_VERIFY_TEST_EVIDENCE"
        else:
            r["dependency_isolation"] = "BLOCKED_OTHER_SYMLINK"
    elif deps.is_dir():
        r["dependency_isolation"] = "LOCAL_DIRECTORY_NOT_YET_CERTIFIED"
        r["observations"]["node_modules"] = {"kind": "local_directory"}
    else:
        r["dependency_isolation"] = "MISSING"
    r["observations"]["evidence_dir_exists"] = evidence.is_dir()
    copies = FINAL_RUNTIME / "vendors"
    r["providers"] = ("FINAL_VENDOR_RUNTIME_PRESENT" if copies.is_dir() and not copies.is_symlink()
                      else "FINAL_VENDOR_RUNTIME_MISSING")
    r["observations"]["final_vendor_copies_present"] = copies.is_dir() and not copies.is_symlink()
    r["observations"]["final_runtime_present"] = FINAL_RUNTIME.is_dir() and not FINAL_RUNTIME.is_symlink()
    r["observations"]["legacy_installation_absent"] = not legacy.parent.exists()
    # Presence of a program does not imply functional certification.
    return r


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=CANONICAL,
                   help="só para testes; por omissao verifica o motor FINAL da VPS")
    p.add_argument("--evidence", type=Path, default=EVIDENCE)
    p.add_argument("--legacy", type=Path, default=LEGACY)
    args = p.parse_args()
    try:
        result = inventory(args.root, args.evidence, args.legacy)
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as exc:
        result = {"project": "engenharia-reversa-final", "source": "BLOCKED",
                  "error_type": type(exc).__name__, "legacy_retirement_completed": None}
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if result.get("source") == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
