#!/usr/bin/env python3
"""Checks for the new isolated project; never executes the analyzed engine."""
import configparser
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
NEW = ROOT / "engenharia-reversa"
ORIGINAL = NEW / "original"
PIN = "5f9187cd279084581fd8c333ba4c6c2c8c506c11"
URL = "https://github.com/morluto/rea.git"


def git(*args, cwd=ROOT):
    return subprocess.check_output(["git", *args], cwd=cwd, text=True).strip()


class IsolatedOriginalTests(unittest.TestCase):
    def test_existing_legacy_folder_is_left_intact(self):
        self.assertTrue((ROOT / "rea" / "README.md").is_file())
        self.assertTrue(git("rev-parse", "HEAD:rea"))

    def test_submodule_is_a_separate_gitlink(self):
        entry = git("ls-files", "--stage", "--", "engenharia-reversa/original")
        self.assertEqual(entry, f"160000 {PIN} 0\tengenharia-reversa/original")

    def test_official_submodule_url(self):
        config = configparser.ConfigParser()
        self.assertTrue(config.read(ROOT / ".gitmodules"))
        section = 'submodule "engenharia-reversa/original"'
        self.assertTrue(config.has_section(section))
        self.assertEqual(config.get(section, "path"), "engenharia-reversa/original")
        self.assertEqual(config.get(section, "url"), URL)

    def test_separate_project_config(self):
        manifest = json.loads((NEW / "project.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["id"], "engenharia-reversa-novo")
        self.assertEqual(manifest["upstream"]["commit"], PIN)
        self.assertEqual(manifest["repository_path"], "engenharia-reversa")
        self.assertFalse(manifest["isolation"]["may_remove_legacy"])
        self.assertEqual(manifest["vps"]["private_root"], "/home/ubuntu/engenharia-reversa-novo")

    def test_official_source_is_checked_out_exactly(self):
        self.assertTrue((ORIGINAL / "package.json").is_file(), "submodule nao foi inicializado")
        self.assertEqual(git("rev-parse", "HEAD", cwd=ORIGINAL), PIN)
        package = json.loads((ORIGINAL / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(package.get("name"), "rea-agents")
        self.assertTrue((ORIGINAL / "scripts" / "rea.mjs").is_file())
        self.assertEqual(git("remote", "get-url", "origin", cwd=ORIGINAL), URL)

    def test_new_scripts_do_not_target_legacy(self):
        deploy = (NEW / "scripts" / "vps_install.sh").read_text(encoding="utf-8")
        self.assertIn("engenharia-reversa-novo", deploy)
        self.assertNotIn("rea-original-upstream-680", deploy)
        self.assertNotIn("/srv/rea", deploy)
        active_script = "\n".join(line for line in deploy.splitlines() if not line.lstrip().startswith("#"))
        self.assertNotRegex(active_script, r"(?m)^\s*sudo(?:\s|$)|[;&|]\s*sudo(?:\s|$)")
        self.assertNotIn("rm -rf", active_script)


if __name__ == "__main__":
    unittest.main()
