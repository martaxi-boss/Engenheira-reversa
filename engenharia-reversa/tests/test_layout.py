#!/usr/bin/env python3
"""Contrato do projeto final: o motor usado nos testes da tarde e nenhum outro."""
import configparser
import json
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[2]
NEW = ROOT / "engenharia-reversa"
ORIGINAL = NEW / "original"
PIN = "160d821ac9a0310afcb8d1fc427862dd6508add5"
URL = "https://github.com/morluto/rea.git"


def git(*args, cwd=ROOT):
    return subprocess.check_output(["git", *args], cwd=cwd, text=True).strip()


class FinalProject(unittest.TestCase):
    def test_legacy_code_and_certifications_preserved(self):
        self.assertEqual(git("rev-parse", "HEAD:rea"), "15e6fec513dcce08cefdbcf441200986397e2793")
        self.assertEqual(git("rev-parse", "HEAD:certifications"), "8616de55052a9986bf992f902587abe3d32992af")

    def test_submodule_points_to_same_original_used_in_live_tests(self):
        entry = git("ls-files", "--stage", "--", "engenharia-reversa/original")
        self.assertEqual(entry, f"160000 {PIN} 0\tengenharia-reversa/original")
        self.assertEqual(git("rev-parse", "HEAD", cwd=ORIGINAL), PIN)
        self.assertEqual(git("remote", "get-url", "origin", cwd=ORIGINAL), URL)
        package = json.loads((ORIGINAL / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(package["name"], "rea-agents")
        self.assertEqual(package["version"], "6.8.0")
        self.assertTrue((ORIGINAL / "scripts" / "rea.mjs").is_file())

    def test_official_url(self):
        cfg = configparser.ConfigParser()
        self.assertTrue(cfg.read(ROOT / ".gitmodules"))
        sect = 'submodule "engenharia-reversa/original"'
        self.assertEqual(cfg.get(sect, "path"), "engenharia-reversa/original")
        self.assertEqual(cfg.get(sect, "url"), URL)

    def test_final_project_manifest_not_a_duplicate(self):
        obj = json.loads((NEW / "project.json").read_text(encoding="utf-8"))
        self.assertEqual(obj["verified_source_commit"], PIN)
        self.assertEqual(obj["vps_installation"]["canonical_path"], "/home/ubuntu/rea-original-upstream-680")
        self.assertFalse(obj["vps_installation"]["new_installation_required"])
        self.assertFalse(obj["dependency_isolation"]["fully_independent"])
        self.assertFalse(obj["previous_legacy"]["retirement_permitted"])
        self.assertEqual(obj["acceptance_evidence"][1]["run_id"], 40915197781)
        self.assertNotIn("/home/ubuntu/engenharia-reversa-novo", json.dumps(obj))

    def test_safe_read_only_script_and_workflow(self):
        src = (NEW / "scripts" / "vps_verify_existing.py").read_text(encoding="utf-8")
        w = (ROOT / ".github/workflows/engenharia-reversa-novo.yml").read_text(encoding="utf-8")
        for blocked in ("sudo ", "sshpass ", "npm ci", "apt-get", "rm -rf", "git clone", "ENG_REV_VPS_SSH_KEY"):
            self.assertNotIn(blocked, src)
            self.assertNotIn(blocked, w)
        self.assertNotIn("instalar-vps-somente-manual", w)
        self.assertNotIn("/home/ubuntu/engenharia-reversa-novo", w)

    def test_old_duplicate_script_removed(self):
        self.assertFalse((NEW / "scripts" / "vps_install.sh").exists())


if __name__ == "__main__":
    unittest.main()
