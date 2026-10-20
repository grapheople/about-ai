---
type: practice
title: 여행 계획을 LLM 위키로 하기
aliases: [여행 위키, pathfinder]
levels: [L1]
volatility: low
updated: 2026-10-21
sources: [sources/pathfinder-case, sources/karpathy-llm-wiki]
tags: [travel, case-study]
---

# 여행 계획을 LLM 위키로 하기

여행 자료·취향·일정을 LLM 위키로 관리하면, 계획이 바뀔 때 관련 문서가 **함께** 바뀌고 다음 여행에도 지식이 남는다.
강사의 실제 사례 pathfinder(2026-06 도쿄 가족여행)가 근거다.

## 본문

### 구성 (pathfinder 기준)
- `profile.md`: 내 여행 취향 기준선 — 페이스, 하루 도보 한계, 좋아하는 테마, 피하는 것.
- 여행별 덮어쓰기: 아이 동반이라 하루 도보 5km → 3km처럼 이번 여행만의 조건.
- `wiki/`: 도시·명소·식당·숙소·테마 페이지.
- `trips/<여행>/`: 일정, 예산, 짐 목록, 식당·호텔 후보, 현지용 한 화면 요약.

### 가장 강력한 장면 — 현지 변경 (2026-06-04)
날이 좋아 실내 일정을 수상버스(크루즈)·도쿄타워·아자부다이 동선으로 바꿨다.
요청 한 번에 새 장소 페이지 3개가 생기고, 일정·현지 요약·식당 후보·촬영 컷이 함께 갱신되었으며, 도보 3km 한계도 다시 점검됐다.
채팅이었다면 여행 조건부터 다시 설명해야 했을 일이다.

### 쌓이는 효과
같은 위키 위에 두 번째 여행(제천)이 추가되었다. 취향·노하우는 다음 여행에 그대로 쓰인다.

### 입문자에게
pathfinder의 규칙 문서(약 21KB)는 고급형이다. 입문자는 빈 볼트에서 Karpathy 글을 Claude에게 건네 작은 규칙부터 같이 만든다.

## 관련
- [[concepts/llm-wiki]] · [[tools/claudian]]

## 출처
- [[sources/pathfinder-case]] · [[sources/karpathy-llm-wiki]]
