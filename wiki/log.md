# Log

Append-only 작업 기록. 형식: `## [YYYY-MM-DD] <ingest|query|lint|outline|slides|script|publish> | <대상>`

## [2026-10-20] setup | 저장소 구조와 CLAUDE.md 스키마 생성
- 첫 원본 소스 추가: raw/2026-10-20-karpathy-llm-wiki.md (아직 ingest 전)

## [2026-10-20] setup | 슬라이드 결과물을 Marp PPTX에서 Google Slides(커넥터)로 변경

## [2026-10-20] setup | 레슨 파이프라인을 대본 우선(outline → script → slides → gslides → final)으로 변경

## [2026-10-20] outline | L1-01 travel-llm-wiki — 인터뷰로 기획, 커리큘럼 L1 번호 재배치(모두 idea 단계)

## [2026-10-21] outline | L1-01 강사 이야기 구간 추가, 강사 인터뷰를 raw에 저장

## [2026-10-21] ingest | L1-01 근거 자료 7건 (Karpathy·Claude Code 문서 2·요금제·Claudian·Obsidian·pathfinder·강사 인터뷰)
- raw 추가: claude-code-setup-docs, claude-code-terminal-guide, claude-pricing, claudian-readme, obsidian-install-license, pathfinder-case, instructor-interview
- sources 8 / concepts 2 (llm-wiki, rag) / tools 3 (claude-code, claudian, obsidian) / practices 2 (travel-llm-wiki, ai-native-dev-team)
- 플래그: [!conflict] Pro 플랜 Claude Code 테스트, [!unverified] Desktop 앱만으로 Claudian 동작 여부

## [2026-10-21] script | L1-01 대본 초안 — [S] 23블록, 내레이션 4,030자, 예상 약 21분

## [2026-10-21] slides | L1-01 slides.md 23장 — script [S01]~[S23]과 1:1, Marp HTML 렌더 확인
