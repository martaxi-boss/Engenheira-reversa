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
    def test_legacy_code_and_certifications_retired(self):
        tracked = set(git("ls-tree", "--name-only", "HEAD").splitlines())
        self.assertNotIn("rea", tracked)
        self.assertNotIn("certifications", tracked)
        self.assertFalse((ROOT / "rea").exists())
        self.assertFalse((ROOT / "certifications").exists())

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
        self.assertEqual(cfg.sections(), [sect])

    def test_final_project_manifest_not_a_duplicate(self):
        obj = json.loads((NEW / "project.json").read_text(encoding="utf-8"))
        self.assertEqual(obj["verified_source_commit"], PIN)
        self.assertEqual(obj["vps_installation"]["canonical_path"], "/home/ubuntu/rea-original-upstream-680")
        self.assertFalse(obj["vps_installation"]["new_installation_required"])
        self.assertTrue(obj["dependency_isolation"]["fully_independent"])
        self.assertTrue(obj["previous_legacy"]["retirement_permitted"])
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

    def test_versioned_skill_source_is_available(self):
        folder = NEW / "skills" / "engenharia-reversa"
        for name in (
            "SKILL.md", "agents/openai.yaml",
            "references/ambiente_final.md", "references/metodologia.md",
            "references/relatorio.md", "scripts/inspecionar_artefacto.py"
        ):
            self.assertTrue((folder / name).is_file(), name)
        content = (folder / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---\nname: engenharia-reversa\n"))
        self.assertIn(PIN, content)
        self.assertIn("/home/ubuntu/rea-original-upstream-680", content)
        self.assertNotIn("ENG_REV_VPS_SSH_KEY", content)

    def test_runtime_dependency_isolation_and_retirement_gate(self):
        obj = json.loads((NEW / "project.json").read_text(encoding="utf-8"))
        isolation = obj["dependency_isolation"]
        self.assertEqual(isolation["node_modules_path"], "/home/ubuntu/rea-final-runtime/node_modules")
        self.assertEqual(isolation["external_supplier_copy_root"], "/home/ubuntu/rea-final-runtime/vendors")
        self.assertTrue(isolation["fully_independent"])
        self.assertTrue(obj["previous_legacy"]["retirement_permitted"])
        self.assertTrue((NEW / "RETIRADA_LEGADO.md").is_file())

    def test_strict_legacy_isolation_policy(self):
        obj = json.loads((NEW / "project.json").read_text(encoding="utf-8"))
        iso = obj["dependency_isolation"]
        self.assertTrue(iso["fully_independent"])
        self.assertFalse(iso["external_suppliers_still_point_to_old_paths"])
        self.assertEqual(iso["runtime_symlinks_into_old"], 0)
        self.assertEqual(iso["runtime_provider_entries_into_old"], 0)
        self.assertEqual(iso["runtime_launchers_old_path_refs"], 0)
        self.assertEqual(iso["final_strict_symlink_audit_run"], 40974645346)
        self.assertTrue((NEW / "SEPARACAO_ABSOLUTA_20261029.md").is_file())
        self.assertTrue(obj["previous_legacy"]["retirement_permitted"])

    def test_operational_skill_docs_after_retirement(self):
        skill = (NEW / "skills/engenharia-reversa/SKILL.md").read_text(encoding="utf-8")
        env = (NEW / "skills/engenharia-reversa/references/ambiente_final.md").read_text(encoding="utf-8")
        bridge = (NEW / "skills/engenharia-reversa/references/ponte_operacional.md").read_text(encoding="utf-8")
        for text in (skill, env, bridge):
            self.assertNotIn("alguns continuam partilhados", text)
            self.assertNotIn("continua pendente", text)
            self.assertNotIn("O legado conserva-se", text)
            self.assertNotIn("Nao apagar o legado", text)
        self.assertIn("30/10/2026", skill)
        self.assertIn("30/10/2026", env)
        self.assertIn("strict_separation_audit", bridge)

    def test_verifier_uses_private_final_vendor_runtime(self):
        source = (NEW / "scripts/vps_verify_existing.py").read_text(encoding="utf-8")
        self.assertIn("FINAL_VENDOR_RUNTIME_PRESENT", source)
        self.assertIn("legacy_installation_absent", source)
        self.assertNotIn("PRESENT_BUT_SHARED_LOCATION", source)

    def test_old_duplicate_script_removed(self):
        self.assertFalse((NEW / "scripts" / "vps_install.sh").exists())


if __name__ == "__main__":
    unittest.main()
