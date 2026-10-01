"""Check the proof registry contract and preservation of exact arithmetic."""

import ast
import copy
import re
import sys
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import repository as repo


class RegistryContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cd, cls.kd, cls.hd = repo.load()
        cls.proof = (repo.ROOT / "PROOF.md").read_text()
        cls.research = (repo.ROOT / "RESEARCH.md").read_text()

    def model(self, cd=None, kd=None, hd=None, proof=None):
        return repo.validate_model(
            cd or self.cd,
            kd or self.kd,
            hd or self.hd,
            self.proof if proof is None else proof,
            self.research,
        )

    def test_current_integrity(self):
        self.assertEqual(repo.validate(), [])

    def test_rejects_cycles(self):
        cd = copy.deepcopy(self.cd)
        cd["claims"][0]["depends_on"] = ["C02"]
        self.assertTrue(any("cycle" in e for e in self.model(cd=cd)))

    def test_rejects_unproved_dependency(self):
        cd = copy.deepcopy(self.cd)
        cd["claims"][0]["depends_on"] = ["MAIN"]
        self.assertTrue(any("unresolved/retracted" in e for e in self.model(cd=cd)))

    def test_rejects_duplicate_canonical_location(self):
        self.assertTrue(
            any(
                "canonical proof location" in e
                for e in self.model(proof=self.proof + '\n<a id="c01"></a>')
            )
        )

    def test_rejects_missing_proof_location(self):
        self.assertTrue(
            any(
                "canonical proof location" in e
                for e in self.model(proof=self.proof.replace('<a id="c01"></a>', ""))
            )
        )

    def test_rejects_detached_certificate(self):
        kd = copy.deepcopy(self.kd)
        kd["checks"][0]["claims"] = []
        self.assertTrue(any("detached check" in e for e in self.model(kd=kd)))

    def test_rejects_overlapping_source_proof(self):
        cd = copy.deepcopy(self.cd)
        cd["claims"][1]["sources"].append(cd["claims"][0]["sources"][0])
        self.assertTrue(any("duplicated" in e for e in self.model(cd=cd)))

    def test_rejects_main_theorem_upgrade(self):
        cd = copy.deepcopy(self.cd)
        next(c for c in cd["claims"] if c["id"] == "MAIN")["status"] = "已严格完成"
        self.assertTrue(any("main theorem" in e for e in self.model(cd=cd)))

    def test_rejects_lost_source_route(self):
        hd = copy.deepcopy(self.hd)
        hd["files"][0]["routes"] = []
        self.assertTrue(any("uncatalogued" in e for e in self.model(hd=hd)))


class ArithmeticPreservation(unittest.TestCase):
    def test_python_math_unchanged(self):
        _, kd, hd = repo.load()
        renames = kd["renames"]
        stems = {
            Path(old).stem: Path(new).stem
            for old, new in renames.items()
            if old.endswith(".py")
        }

        class Relocate(ast.NodeTransformer):
            def visit_Module(self, node):
                self.generic_visit(node)
                if (
                    node.body
                    and isinstance(node.body[0], ast.Expr)
                    and isinstance(node.body[0].value, ast.Constant)
                    and isinstance(node.body[0].value.value, str)
                ):
                    node.body.pop(0)
                return node

            def visit_ImportFrom(self, node):
                node.module = stems.get(node.module, node.module)
                return node

            def visit_Constant(self, node):
                if isinstance(node.value, str):
                    value = node.value
                    for old, new in stems.items():
                        value = re.sub(r"\b" + re.escape(old) + r"\b", new, value)
                    node.value = value
                return node

            def visit_BinOp(self, node):
                self.generic_visit(node)
                if (
                    isinstance(node.op, ast.Div)
                    and isinstance(node.right, ast.Constant)
                    and node.right.value in ("research-checks", "crt-descent")
                ):
                    return node.left
                return node

        with zipfile.ZipFile(repo.ROOT / hd["archive"]) as z:
            for old, new in renames.items():
                if old.endswith(".py"):
                    original = Relocate().visit(ast.parse(z.read(old).decode()))
                    current = Relocate().visit(ast.parse((repo.ROOT / new).read_text()))
                    self.assertEqual(ast.dump(original), ast.dump(current), new)

    def test_cpp_sources_byte_identical(self):
        _, kd, hd = repo.load()
        with zipfile.ZipFile(repo.ROOT / hd["archive"]) as z:
            for old, new in kd["renames"].items():
                if old.endswith(".cpp"):
                    self.assertEqual(z.read(old), (repo.ROOT / new).read_bytes(), new)

    def test_selected_display_formulas_preserved(self):
        cd, _, hd = repo.load()
        fm = {f["id"]: f for f in hd["files"]}
        current = (repo.ROOT / "PROOF.md").read_text()

        def compact(text):
            # Malformed \frac tokens in old files are the catalogued typographic fix.
            return re.sub(r"\s+", "", text.replace("\nrac ", r"\frac "))

        current = compact(current)
        count = 0
        with zipfile.ZipFile(repo.ROOT / hd["archive"]) as z:
            for c in cd["claims"]:
                for part in c["sources"]:
                    lines = z.read(fm[part["source"]]["path"]).decode().splitlines()
                    text = "\n".join(lines[part["start"] - 1 : part["end"]])
                    formulas = []
                    block = None
                    fenced = False
                    for line in text.splitlines():
                        stripped = line.strip()
                        if stripped in (r"\[", "```math"):
                            if block is not None:
                                formulas.append("\n".join(block))
                            block = []
                            fenced = stripped == "```math"
                            continue
                        if block is not None and (
                            stripped == ("```" if fenced else r"\]")
                            or stripped.startswith("#")
                            or stripped == "---"
                            or (stripped and "\u4e00" <= stripped[0] <= "\u9fff")
                        ):
                            formulas.append("\n".join(block))
                            block = None
                            continue
                        if block is not None:
                            block.append(line)
                    if block is not None:
                        formulas.append("\n".join(block))
                    for formula in formulas:
                        self.assertTrue(
                            compact(formula) in current,
                            c["id"]
                            + ": "
                            + part["source"]
                            + " formula: "
                            + formula[:180],
                        )
                        count += 1
        self.assertGreater(count, 2000)


if __name__ == "__main__":
    unittest.main()
