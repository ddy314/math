"""Repository navigation, exact-check runner and proof/source integrity checks."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import time
import zipfile
from datetime import UTC, datetime
from itertools import pairwise
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATES = {"已严格完成", "有限证书", "待证", "失效/降级"}
BRANCHES = {"common", "a2", "dd", "a1"}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(root: Path = ROOT):
    return (
        read_json(root / "registry/claims.json"),
        read_json(root / "registry/checks.json"),
        read_json(root / "history/sources.json"),
    )


def anchors(text: str) -> set[str]:
    return set(re.findall(r'<a id="([^"]+)"></a>', text))


def validate_check_sources(checks, root: Path) -> list[str]:
    """Include local imports and headers in the certificate hash contract."""
    errors = []
    for check in checks:
        for source in [check, *check.get("dependencies", [])]:
            path = (root / source["path"]).resolve()
            label = f"{check['id']}/{source['path']}"
            if not path.is_relative_to(root.resolve()):
                errors.append(label + ": source escapes repository")
            elif not path.is_file():
                errors.append(label + ": missing source")
            elif digest(path.read_bytes()) != source["sha256"]:
                errors.append(
                    label
                    + ": source hash differs (update audited registry after intentional edits)"
                )
    return errors


def validate_model(
    claim_doc, check_doc, history, proof: str, research: str
) -> list[str]:
    """Validate the graph and evidence contract; this does not prove mathematics."""
    errors = []
    claims = claim_doc["claims"]
    checks = check_doc["checks"]
    routes = claim_doc["routes"]

    def unique(rows, field, name):
        values = [row[field] for row in rows]
        if len(values) != len(set(values)):
            errors.append(f"{name}: duplicate {field}")
        return {row[field]: row for row in rows}

    cm = unique(claims, "id", "claims")
    km = unique(checks, "id", "checks")
    rm = unique(routes, "id", "routes")
    fm = unique(history["files"], "id", "sources")
    unique(history["files"], "path", "source paths")
    unique(history["records"], "id", "ledger records")
    all_ids = list(re.findall(r'<a id="([^"]+)"></a>', proof))
    if len(all_ids) != len(set(all_ids)):
        errors.append("proof: duplicate anchors")
    ra = anchors(research)
    for route in routes:
        if route["id"] not in ra:
            errors.append(f"route {route['id']}: missing record anchor")
        if route["status"] not in STATES:
            errors.append(f"route {route['id']}: invalid state")
    main = cm.get("MAIN", {})
    if claim_doc.get("overall_status") != "待证" or main.get("status") != "待证":
        errors.append(
            "main theorem must remain open until the proof is actually complete"
        )
    for branch in ("A2", "DD", "A1"):
        if cm.get("OPEN-" + branch, {}).get("status") != "待证":
            errors.append(f"{branch}: complete branch is still open")
    graph = {c["id"]: c["depends_on"] for c in claims}
    visiting = set()
    visited = set()

    def visit(node):
        if node in visiting:
            errors.append("claim dependency cycle at " + node)
            return
        if node in visited:
            return
        visiting.add(node)
        for dep in graph.get(node, []):
            if dep in graph:
                visit(dep)
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        visit(node)
    for c in claims:
        cid = c["id"]
        if c["status"] not in STATES:
            errors.append(f"{cid}: invalid state")
        if c["branch"] not in BRANCHES:
            errors.append(f"{cid}: invalid branch")
        if not c["scope"].strip():
            errors.append(f"{cid}: empty mathematical scope")
        if c["route"] not in rm:
            errors.append(f"{cid}: missing route")
        if proof.count(f'<a id="{cid.lower()}"></a>') != 1:
            errors.append(f"{cid}: needs exactly one canonical proof location")
        fragment = proof.split(f'<a id="{cid.lower()}"></a>', 1)[-1]
        # Locate the state immediately after the unique registered claim heading.
        if not re.search(
            rf"### {re.escape(cid)}[^\n]*\n\n\*\*状态：{re.escape(c['status'])}。\*\*",
            fragment,
        ):
            errors.append(f"{cid}: manuscript state differs from registry")
        for d in c["depends_on"]:
            if d not in cm:
                errors.append(f"{cid}: unknown dependency {d}")
            elif c["status"] in {"已严格完成", "有限证书"} and cm[d]["status"] in {
                "待证",
                "失效/降级",
            }:
                errors.append(
                    f"{cid}: proved claim depends on unresolved/retracted {d}"
                )
        for ck in c["checks"]:
            if ck not in km:
                errors.append(f"{cid}: unknown check {ck}")
            elif cid not in km[ck]["claims"]:
                errors.append(f"{cid}/{ck}: asymmetric link")
        for s in c["sources"]:
            if s["source"] not in fm:
                errors.append(f"{cid}: unknown source {s['source']}")
            if not 1 <= s["start"] <= s["end"]:
                errors.append(f"{cid}: invalid source span")
    for c in checks:
        if c["kind"] not in {"python", "cpp"}:
            errors.append(f"{c['id']}: unknown runtime")
        if c["group"] not in {"quick", "full"}:
            errors.append(f"{c['id']}: invalid run group")
        if not c["purpose"].strip():
            errors.append(f"{c['id']}: missing scope/role")
        if not c["claims"]:
            errors.append(f"{c['id']}: detached check")
        for cid in c["claims"]:
            if cid not in cm or c["id"] not in cm[cid]["checks"]:
                errors.append(f"{c['id']}/{cid}: asymmetric link")
    for f in history["files"]:
        if not f["routes"] or any(r not in rm for r in f["routes"]):
            errors.append(f"{f['id']}: uncatalogued source route")
        for cid in f["current_claims"]:
            if cid not in cm:
                errors.append(f"{f['id']}: unknown current use {cid}")
    for record in history["records"]:
        if record["source"] not in fm:
            errors.append(f"{record['id']}: missing container")
        if not record["routes"] or any(r not in rm for r in record["routes"]):
            errors.append(f"{record['id']}: unknown route")
    # A canonical source span occurs once, regardless of how many previous files cited it.
    spans = {}
    for c in claims:
        for s in c["sources"]:
            spans.setdefault(s["source"], []).append((s["start"], s["end"], c["id"]))
    for source, ss in spans.items():
        ordered = sorted(ss)
        for left, right in pairwise(ordered):
            if left[1] >= right[0]:
                errors.append(
                    f"{source}: source proof span duplicated by {left[2]} and {right[2]}"
                )
    return errors


def validate(root: Path = ROOT) -> list[str]:
    errors = []
    for path in (
        "README.md",
        "PROOF.md",
        "RESEARCH.md",
        "CHECKS.md",
        "AGENTS.md",
        "CONTRIBUTING.md",
        "main.py",
        "repository.py",
    ):
        if not (root / path).is_file():
            errors.append("missing " + path)
    if errors:
        return errors
    cd, kd, hd = load(root)
    proof = (root / "PROOF.md").read_text()
    research = (root / "RESEARCH.md").read_text()
    errors.extend(validate_model(cd, kd, hd, proof, research))
    # Check every visible Markdown link, including explicit fragments in local targets.
    for p in sorted(root.rglob("*.md")):
        if any(x in p.parts for x in (".venv", ".git")):
            continue
        text = p.read_text()
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for label, target in re.findall(r"\[([^\]\n]+)\]\(([^)\n]+)\)", text):
            if re.match(r"[a-zA-Z][\w+.-]*:", target):
                continue
            file, _, fragment = target.partition("#")
            dest = (p.parent / file).resolve() if file else p
            if not dest.is_relative_to(root.resolve()):
                errors.append(f"{p.name}: link escapes repository")
                continue
            if not dest.is_file():
                errors.append(f"{p.name}: missing link {target}")
                continue
            if fragment and fragment not in anchors(dest.read_text()):
                errors.append(f"{p.name}: missing fragment {target}")
    declared = {
        source["path"]
        for c in kd["checks"]
        for source in [c, *c.get("dependencies", [])]
    }
    actual = {
        p.relative_to(root).as_posix()
        for p in (root / "checks").rglob("*")
        if p.suffix in {".py", ".cpp", ".hpp"}
    }
    if declared != actual:
        errors.append("check source files differ from the registered active set")
    errors.extend(validate_check_sources(kd["checks"], root))
    for obsolete in ("docs", "scripts"):
        if (root / obsolete).exists():
            errors.append(f"obsolete parallel tree remains: {obsolete}")
    archive = root / hd["archive"]
    if not archive.is_file():
        return errors + ["missing frozen source archive"]
    if digest(archive.read_bytes()) != hd["archive_sha256"]:
        errors.append("frozen archive hash differs")
    with zipfile.ZipFile(archive) as z:
        expected = {f["path"] for f in hd["files"]}
        if expected != set(z.namelist()):
            errors.append("source archive members differ from catalog")
        for f in hd["files"]:
            path = Path(f["path"])
            if path.is_absolute() or ".." in path.parts:
                errors.append("unsafe source path " + f["path"])
                continue
            b = z.read(f["path"])
            if len(b) != f["bytes"] or digest(b) != f["sha256"]:
                errors.append("source integrity mismatch " + f["id"])
        fm = {f["id"]: f for f in hd["files"]}
        for c in cd["claims"]:
            for s in c["sources"]:
                a = z.read(fm[s["source"]]["path"]).decode().splitlines()
                b = ("\n".join(a[s["start"] - 1 : s["end"]]) + "\n").encode()
                if s["end"] > len(a) or digest(b) != s["sha256"]:
                    errors.append(f"{c['id']}: proof source span checksum differs")
        for r in hd["records"]:
            a = z.read(fm[r["source"]]["path"]).decode().splitlines()
            b = ("\n".join(a[r["start"] - 1 : r["end"]]) + "\n").encode()
            if digest(b) != r["sha256"]:
                errors.append("ledger record checksum differs " + r["id"])
    return list(dict.fromkeys(errors))


def status(root=ROOT):
    cd, _, _ = load(root)
    print("主不存在性命题：待证；A2、DD、A1 三个完整异常分支仍未全部关闭。")
    print("完整子域：后两分母一位已排除；其它子域的范围见 PROOF.md。")
    print(f"现行命题 {len(cd['claims'])} 项，研究路线 {len(cd['routes'])} 条。")
    print("阅读：PROOF.md → RESEARCH.md → CHECKS.md")


def source_rows(hd, route=None):
    rows = hd["files"] + hd["records"]
    return [r for r in rows if route is None or route in r["routes"]]


def source_item(hd, id):
    rows = {r["id"]: r for r in hd["files"] + hd["records"]}
    if id in rows:
        return rows[id]
    item = next((r for r in hd["files"] if r["path"] == id), None)
    if item:
        return item
    raise ValueError("unknown source ID/path: " + id)


def source_text(root, hd, item):
    fm = {r["id"]: r for r in hd["files"]}
    f = fm[item["source"]] if "source" in item else item
    with zipfile.ZipFile(root / hd["archive"]) as z:
        b = z.read(f["path"])
    if digest(b) != f["sha256"]:
        raise ValueError("source checksum mismatch")
    text = b.decode()
    if "source" in item:
        text = "\n".join(text.splitlines()[item["start"] - 1 : item["end"]]) + "\n"
        if digest(text.encode()) != item["sha256"]:
            raise ValueError("record checksum mismatch")
    return f["path"], text


def run_checks(ids, group, report, ubsan=False, root=ROOT):
    _, kd, hd = load(root)
    km = {c["id"]: c for c in kd["checks"]}
    selected = (
        [c for c in kd["checks"] if c["group"] == group]
        if group
        else [km[id] for id in ids]
    )
    if not selected:
        raise ValueError("choose at least one check ID or --group")
    if len({c["id"] for c in selected}) != len(selected):
        raise ValueError("duplicate check ID")
    errors = validate(root)
    if errors:
        raise ValueError("repository integrity check failed:\n" + "\n".join(errors))
    temporary = Path(tempfile.mkdtemp(prefix="math-verify-"))
    rows = []
    print(f"核对日志：{temporary}", flush=True)
    for c in selected:
        started = datetime.now(UTC).isoformat()
        now = time.monotonic()
        log = temporary / (c["id"] + ".log")
        commands = []
        returncode = 0
        print("RUN " + c["id"] + ": " + c["purpose"], flush=True)
        with log.open("w") as output:
            if c["kind"] == "cpp":
                binary = temporary / c["id"]
                cmd = ["g++", "-O2", "-std=c++20", "-Wall", "-Wextra"]
                if ubsan:
                    cmd += ["-fsanitize=undefined", "-fno-sanitize-recover=all"]
                cmd += [str(root / c["path"]), "-o", str(binary)]
                commands.append(cmd)
                result = subprocess.run(
                    cmd, cwd=root, stdout=output, stderr=subprocess.STDOUT, check=False
                )
                returncode = result.returncode
                command = [str(binary), *c["args"]]
            else:
                command = [sys.executable, str(root / c["path"]), *c["args"]]
            if returncode == 0:
                commands.append(command)
                result = subprocess.run(
                    command,
                    cwd=root,
                    stdout=output,
                    stderr=subprocess.STDOUT,
                    check=False,
                )
                returncode = result.returncode
        b = log.read_bytes()
        tail = "\n".join(b.decode(errors="replace").splitlines()[-8:])
        rows.append(
            {
                "id": c["id"],
                "source_sha256": c["sha256"],
                "dependencies": c.get("dependencies", []),
                "commands": commands,
                "started_at": started,
                "duration_seconds": round(time.monotonic() - now, 3),
                "returncode": returncode,
                "stdout_sha256": digest(b),
                "log": str(log),
                "tail": tail,
            }
        )
        print(
            ("PASS " if returncode == 0 else "FAIL ")
            + c["id"]
            + f" ({rows[-1]['duration_seconds']:.2f}s)",
            flush=True,
        )
        print(tail, flush=True)
        if returncode != 0:
            break
    payload = {
        "archive_sha256": hd["archive_sha256"],
        "proof_sha256": digest((root / "PROOF.md").read_bytes()),
        "registry_sha256": digest((root / "registry/checks.json").read_bytes()),
        "checks": rows,
    }
    destination = Path(report) if report else temporary / "report.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print("验证报告：" + str(destination), flush=True)
    return (
        0
        if len(rows) == len(selected) and all(r["returncode"] == 0 for r in rows)
        else 1
    )


def cli(argv=None):
    parser = argparse.ArgumentParser(description="Exact Lift 的统一证明与核对入口")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("status")
    sub.add_parser("check")
    listing = sub.add_parser("list")
    listing.add_argument("kind", choices=("claims", "checks", "routes", "sources"))
    listing.add_argument("--branch", choices=sorted(BRANCHES))
    listing.add_argument("--route")
    listing.add_argument("--match", default="")
    verify = sub.add_parser("verify")
    verify.add_argument("ids", nargs="*")
    verify.add_argument("--group", choices=("quick", "full"))
    verify.add_argument("--report")
    verify.add_argument(
        "--ubsan", action="store_true", help="for directly compiled C++ checks"
    )
    src = sub.add_parser("source")
    ss = src.add_subparsers(dest="action", required=True)
    show = ss.add_parser("show")
    show.add_argument("id")
    show.add_argument("--start", type=int, default=1)
    show.add_argument("--end", type=int, default=200)
    search = ss.add_parser("search")
    search.add_argument("pattern")
    search.add_argument("--route")
    search.add_argument("--limit", type=int, default=30)
    extract = ss.add_parser("extract")
    extract.add_argument("directory")
    args = parser.parse_args(argv)
    try:
        if args.command in (None, "status"):
            status()
            return 0
        if args.command == "check":
            errors = validate()
            if errors:
                print("\n".join("FAIL: " + e for e in errors))
                return 1
            cd, kd, hd = load()
            print(
                f"PASS: {len(cd['claims'])} claims, {len(kd['checks'])} check modes, {len(hd['files'])} frozen sources, {len(hd['records'])} ledger records"
            )
            print(
                "命题依赖、唯一位置、链接、证书路径与全部来源哈希通过；此检查不证明数学结论。"
            )
            return 0
        if args.command == "verify":
            if args.ids and args.group:
                raise ValueError("IDs and --group are alternatives")
            return run_checks(args.ids, args.group, args.report, args.ubsan)
        cd, kd, hd = load()
        if args.command == "list":
            options = {
                "claims": cd["claims"],
                "checks": kd["checks"],
                "routes": cd["routes"],
                "sources": source_rows(hd, args.route),
            }
            for row in options[args.kind]:
                branch = row.get("branch") or (
                    row.get("path", "/").split("/")[1]
                    if row.get("path", "").startswith("checks/")
                    else None
                )
                if args.branch and branch != args.branch:
                    continue
                if (
                    args.route
                    and args.kind != "sources"
                    and row.get("route") != args.route
                    and row.get("id") != args.route
                ):
                    continue
                if args.match and args.match not in json.dumps(row, ensure_ascii=False):
                    continue
                title = row.get("title", row.get("purpose", row.get("path", "")))
                state = row.get("status", row.get("group", "来源"))
                print(f"{row['id']}\t{state}\t{title}")
            return 0
        if args.action == "show":
            item = source_item(hd, args.id)
            path, text = source_text(ROOT, hd, item)
            lines = text.splitlines()
            if args.start < 1 or args.end < args.start:
                raise ValueError("invalid line range")
            print(f"{item['id']} · {path} · SHA-256 {item['sha256']}")
            for i in range(args.start - 1, min(args.end, len(lines))):
                print(f"{i + 1}: {lines[i]}")
            print(
                f"显示 {args.start}..{min(args.end, len(lines))} / {len(lines)} 行；用 --end 指定完整范围。"
            )
            return 0
        if args.action == "search":
            if args.limit < 1:
                raise ValueError("limit must be positive")
            count = 0
            # Search each physical source once; ledger records remain separately navigable.
            for item in hd["files"]:
                if (
                    args.route
                    and args.route not in item["routes"]
                    and not any(
                        r["source"] == item["id"] and args.route in r["routes"]
                        for r in hd["records"]
                    )
                ):
                    continue
                path, text = source_text(ROOT, hd, item)
                for i, line in enumerate(text.splitlines(), 1):
                    if args.pattern in line:
                        print(f"{item['id']}:{i}\t{path}\t{line[:200]}")
                        count += 1
                        if count >= args.limit:
                            return 0
            return 0
        if args.action == "extract":
            dest = Path(args.directory).resolve()
            if dest == ROOT or dest.is_relative_to(ROOT):
                raise ValueError("extract outside current repository")
            if dest.exists() and any(dest.iterdir()):
                raise ValueError("destination must be empty")
            errors = validate()
            if errors:
                raise ValueError("source integrity failed: " + "; ".join(errors))
            dest.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(ROOT / hd["archive"]) as z:
                for f in hd["files"]:
                    target = dest / f["path"]
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(z.read(f["path"]))
            print(
                f"已只读解包 {len(hd['files'])} 个原始源码到 {dest}；历史指令不改变现行工作规则。"
            )
            return 0
    except (ValueError, KeyError, OSError, zipfile.BadZipFile) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
