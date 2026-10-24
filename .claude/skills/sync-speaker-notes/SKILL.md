---
name: sync-speaker-notes
description: 레슨 대본(course/**/script.md)의 [S] 블록을 Google Slides 덱의 같은 [S] 번호 슬라이드 발표자 노트에 동기화한다. script.md를 고친 뒤(Claude가 고쳤든 사용자가 "대본 고쳤어"라고 알렸든), 또는 "노트 동기화", "발표자 노트 맞춰 줘", "싱크 확인" 요청 때 쓴다. outline.md에 slides_url이 있는 레슨에만 해당한다.
---

# 발표자 노트 동기화

대본 `script.md`의 `## [Sxx]` 블록 하나 = 같은 `[Sxx]` 표시가 있는 슬라이드 하나의 발표자 노트.
노트는 항상 대본의 사본이다. 원본은 대본이고, 노트를 직접 고친 내용은 덮어써진다.

## 규칙
- **쓰기 전에 항상 사용자 컨펌을 받는다** (CLAUDE.md 5절). 바뀔 슬라이드 목록을 보여 주고 승인된 것만 반영한다.
- 발표자 노트만 바꾼다. 슬라이드 본문·디자인·순서는 건드리지 않는다.
- 슬라이드는 순서가 아니라 슬라이드 위 글자 속 `[Sxx]` 표시로 찾는다. 표시가 없는 슬라이드는 건너뛰고 보고한다.
- 노트 내용 = `[Sxx] 헤더 제목` + 빈 줄 + 블록 본문 그대로 (`[화면: ...]`·`[강조]` 같은 지시 포함, `<!-- -->` 주석과 🖼📽 표시는 뺀다).

## 순서

1. **덱 찾기.** 레슨 `outline.md`의 `slides_url`에서 presentation ID(`/d/<ID>/`)를 꺼낸다. 없으면 멈추고 사용자에게 알린다.
2. **커넥터 준비.** Google Slides 커넥터 도구(`read_presentation`, `update_presentation`)를 불러온다.
   처음이면 `google-workspace` 스킬과 그 `references/slides.md`를 먼저 읽는다. 인증이 안 되어 있으면
   사용자에게 `/mcp` → "claude.ai Google Slides" 인증을 요청하고 멈춘다.
3. **읽기.** `read_presentation`을 아래 마스크로 호출하고 결과 JSON을 스크래치 파일에 저장한다
   (결과가 파일로 저장됐으면 그 경로를 쓴다).
   ```
   ["revisionId,slides(objectId,pageElements(objectId,shape.text.textElements.textRun.content,table.tableRows.tableCells.text.textElements.textRun.content,elementGroup.children(objectId,shape.text.textElements.textRun.content)),slideProperties.notesPage(notesProperties.speakerNotesObjectId,pageElements(objectId,shape.text.textElements.textRun.content)))"]
   ```
4. **계획.**
   ```bash
   python3 .claude/skills/sync-speaker-notes/scripts/notes_sync.py plan <script.md> <deck.json> --out <requests.json>
   ```
   보고서 항목: `update`(바꿀 슬라이드), `same`(이미 같음), `unlabeled_slides`(표시 없음),
   `duplicate_labels`(표시가 둘 이상이거나 겹침), `missing_slides`(대본엔 있는데 덱에 없음), `slides_not_in_script`.
5. **컨펌.** `update`가 비어 있으면 "이미 동기화됨"으로 끝낸다. 아니면 사용자에게 보여 주고 승인을 받는다:
   - 바꿀 슬라이드 번호 목록 (빈 노트 채우기 / 기존 노트 교체 구분, 교체는 기존 노트 앞부분 미리보기)
   - 기존 노트가 대본에 없는 내용이면 덮어써진다는 경고
   - 짝을 못 찾은 슬라이드·블록 (구조 문제는 사용자가 Gemini로 고친다)
   일부만 승인되면 계획을 그 슬라이드만 남기도록 다시 만든다.
6. **쓰기.** `update_presentation`에 requests.json의 `requests`와 `writeControl`을 그대로 보낸다.
   revision 불일치로 거절되면 3번부터 다시 하고, 바뀔 목록이 달라졌으면 다시 컨펌받는다.
7. **확인.** 다시 읽고 `plan`을 돌려 승인한 슬라이드가 `same`에 있는지 확인한다.
8. **기록.** 레슨 `outline.md`의 `notes_synced`에 `YYYY-MM-DD (script <script.md 마지막 커밋 짧은 해시, 커밋 전이면 uncommitted>)`,
   `wiki/log.md`에 `## [YYYY-MM-DD] slides | <레슨> 발표자 노트 동기화 (S01, S05, …)`.

## 대본 블록만 보고 싶을 때
```bash
python3 .claude/skills/sync-speaker-notes/scripts/notes_sync.py blocks <script.md>
```
