---
type: case-note
origin: /Users/pax/Documents/GitHub/pathfinder (강사 본인 저장소, 읽기 전용으로 조사)
captured: 2026-10-21
note: 영상에 쓸 수 있는 사실만 요약. 가족 세부 정보(임신 주수 등)는 의도적으로 제외.
---

# pathfinder — 강사의 실제 여행 LLM 위키 (사례 메모)

## 무엇인가
Karpathy의 LLM Wiki 패턴을 여행 도메인에 적용한 개인 지식 베이스. Claude Code + Obsidian으로 운영.
2026-05-27 init → 2026-06 도쿄 가족여행(3박 4일) 준비·현지 운영 → 2026-06 제천 여행 추가.

## 구조 (2026-10-21 기준 수치)
- `sources/` 21개 — 디시인사이드 여행 갤러리 글, 한국어 위키백과, 공식 사이트 요약 등
- `wiki/` 31개 페이지 — countries / cities / pois(명소·식당·숙소·액티비티) / themes
- `trips/2026-06-tokyo/` 10개 파일 — index, itinerary, budget, packing-list, food-options, hotel-options, logistics, quick-reference, content, shot-list
- `trips/2026-06-jecheon/` — 두 번째 여행이 같은 위키 위에 쌓임
- `profile.md` — 여행 취향 기준선(페이스, 하루 도보 한계, 끌리는 테마, 피하는 것). 여행별 `overrides`로 덮어씀
  (예: 기준 하루 도보 5km → 이번 여행 3km)
- 커스텀 명령 5개: /ingest, /query, /plan-trip, /lint, /debrief
- log.md 기록 27건 (ingest, plan, plan-update, lint, schema-update)
- CLAUDE.md 약 21KB — 입문자에게는 무거운 고급 스키마

## 현지 변경 사례 — 2026-06-04 (여행 둘째 날)
- 원래 계획: 도요스 teamLab Planets (실내)
- 현지 결정: 날이 좋아 **수상버스(아사쿠사 → 히노데) → 도쿄타워 → 아자부다이 힐즈 → 신주쿠** 동선으로 교체
- 요청 한 번으로 일어난 일 (log.md 기준):
  - 새 소스 1개 저장, 새 위키 페이지 3개 (tokyo-tower, azabudai-hills, teamlab-borderless-azabudai)
  - 기존 페이지 갱신: sumida-river(수상버스 정보), tokyo, index
  - trip 산출물 갱신: itinerary(도보 거리 ~3km 한계 점검 포함), quick-reference, content, shot-list, food-options(점심 후보를 새 동선 권역으로 교체)
- 같은 날 오후 두 번째 조정: teamLab Borderless 제외, 아자부다이는 광장만, 저녁 도청 무료 전망대 야경 복귀
- 주의: log에 "비 때문에 변경"한 기록은 없다. 영상에서는 크루즈 교체 실화만 쓴다.

## 화면 노출 가능 범위 (강사 결정, 2026-10-21)
그래프 뷰 + log·일정표 일부. 가족 세부 정보는 촬영용 사본에서 수정한 뒤 녹화.
