#!/usr/bin/env python3
"""script.md의 [S] 블록을 Google Slides 발표자 노트에 맞추기 위한 도우미.

  blocks <script.md>
      대본을 [S] 블록별 노트 텍스트로 나눠 JSON으로 출력한다.

  plan <script.md> <presentation.json> [--out requests.json]
      read_presentation 결과(아래 MASK로 읽은 JSON)를 받아 슬라이드의 [Sxx] 표시로 블록과 짝짓고,
      노트가 다른 슬라이드만 골라 변경 보고서를 stdout에, update_presentation 요청을 --out 파일에 쓴다.

MASK는 SKILL.md에 있다. 슬라이드는 순서가 아니라 슬라이드 위 글자 속 [Sxx] 표시로 찾는다.
"""
import argparse
import json
import re
import sys

LABEL = re.compile(r"\[S(\d{2})\]")
HEADER = re.compile(r"(?m)^## \[S(\d{2})\] (.*)$")
COMMENT = re.compile(r"<!--.*?-->", re.S)
MARKERS = re.compile(r"\s*[🖼📽]\s*$")


def parse_blocks(path):
    text = open(path, encoding="utf-8").read()
    # frontmatter 제거
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    matches = list(HEADER.finditer(text))
    blocks = {}
    for i, m in enumerate(matches):
        num = m.group(1)
        title = MARKERS.sub("", m.group(2)).strip()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = COMMENT.sub("", text[m.end():body_end])
        lines = [l.rstrip() for l in body.strip("\n").split("\n")]
        # 블록 끝의 구분선과 빈 줄 정리, 빈 줄은 최대 1개
        while lines and lines[-1] in ("", "---"):
            lines.pop()
        out = []
        for l in lines:
            if l == "" and (not out or out[-1] == ""):
                continue
            out.append(l)
        if num in blocks:
            sys.exit(f"대본에 [S{num}] 헤더가 두 번 있다")
        blocks[num] = {"title": title, "notes": f"[S{num}] {title}\n\n" + "\n".join(out).strip()}
    return blocks


def texts(elements):
    """페이지 요소들의 모든 글자를 모은다 (그룹·표 포함)."""
    for el in elements or []:
        for te in (el.get("shape", {}).get("text", {}) or {}).get("textElements", []) or []:
            c = (te.get("textRun") or {}).get("content")
            if c:
                yield c
        for row in (el.get("table", {}) or {}).get("tableRows", []) or []:
            for cell in row.get("tableCells", []) or []:
                for te in (cell.get("text", {}) or {}).get("textElements", []) or []:
                    c = (te.get("textRun") or {}).get("content")
                    if c:
                        yield c
        yield from texts((el.get("elementGroup") or {}).get("children"))


def norm(s):
    return "\n".join(l.rstrip() for l in s.replace("\r", "").replace("\v", "\n").strip().split("\n"))


def plan(script_path, pres_path, out_path):
    blocks = parse_blocks(script_path)
    pres = json.load(open(pres_path, encoding="utf-8"))
    rev = pres.get("revisionId")
    report = {"revisionId": rev, "update": [], "same": [], "unlabeled_slides": [],
              "duplicate_labels": [], "missing_slides": [], "slides_not_in_script": []}
    requests, seen = [], {}
    for idx, slide in enumerate(pres.get("slides", []), 1):
        labels = sorted(set(LABEL.findall("".join(texts(slide.get("pageElements"))))))
        if not labels:
            report["unlabeled_slides"].append({"position": idx, "objectId": slide["objectId"]})
            continue
        if len(labels) > 1:
            report["duplicate_labels"].append({"position": idx, "labels": labels})
            continue
        num = labels[0]
        if num in seen:
            report["duplicate_labels"].append({"position": idx, "labels": [num], "also_at": seen[num]})
            continue
        seen[num] = idx
        if num not in blocks:
            report["slides_not_in_script"].append({"position": idx, "label": f"S{num}"})
            continue
        notes_page = (slide.get("slideProperties") or {}).get("notesPage") or {}
        notes_id = (notes_page.get("notesProperties") or {}).get("speakerNotesObjectId")
        if not notes_id:
            sys.exit(f"S{num} 슬라이드에 speakerNotesObjectId가 없다 — MASK를 확인")
        current = "".join(texts([e for e in notes_page.get("pageElements", []) if e.get("objectId") == notes_id]))
        want = blocks[num]["notes"]
        if norm(current) == norm(want):
            report["same"].append(f"S{num}")
            continue
        report["update"].append({"slide": f"S{num}", "position": idx, "was_empty": not current.strip(),
                                 "current_preview": norm(current)[:80], "new_chars": len(want)})
        if current.strip():
            requests.append({"deleteText": {"objectId": notes_id, "textRange": {"type": "ALL"}}})
        requests.append({"insertText": {"objectId": notes_id, "insertionIndex": 0, "text": want}})
    report["missing_slides"] = [f"S{n}" for n in sorted(blocks) if n not in seen]
    if out_path:
        body = {"requests": requests}
        if requests:
            body["writeControl"] = {"requiredRevisionId": rev}
        json.dump(body, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(report, ensure_ascii=False, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("blocks")
    b.add_argument("script")
    p = sub.add_parser("plan")
    p.add_argument("script")
    p.add_argument("presentation")
    p.add_argument("--out")
    a = ap.parse_args()
    if a.cmd == "blocks":
        print(json.dumps(parse_blocks(a.script), ensure_ascii=False, indent=1))
    else:
        plan(a.script, a.presentation, a.out)


if __name__ == "__main__":
    main()
