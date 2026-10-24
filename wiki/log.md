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

## [2026-10-22] ingest | 강사 경력·AI 코딩 변천사 + 웹 사실 확인 (Copilot·GPT-4·Claude Code·○○ 엔지니어링·Karpathy)
- raw 추가: instructor-career-story, ai-coding-timeline-facts
- 신규: sources 2, concepts/ai-engineering-paradigms, syntheses/ai-coding-timeline / 갱신: tools/claude-code, practices/ai-native-dev-team, sources/karpathy-llm-wiki, index, overview
- 플래그: [!conflict] 하네스·루프 엔지니어링 계층 관계 해석이 출처마다 다름

## [2026-10-22] script | L1-01 도입부 재구성 — 강사 경력·AI 코딩 변천사·변하지 않는 가치·카파시 소개 8블록 추가, 기존 S04·S05를 맨 끝(S26·S27)으로 이동, S06 흡수
- [S] 23 → 29블록, 내레이션 약 5,020자, 예상 약 24분. slides.md는 아직 옛 번호 — 승인 후 재동기화. 상태 slides → script

## [2026-10-22] ingest | 강사 경력 순서 정정 (대형 포털 → 커머스 플랫폼 → 건강 플랫폼 스타트업)
- raw 추가: instructor-career-clarification / 갱신: sources/instructor-career-story, syntheses/ai-coding-timeline, L1-01 script S03·outline

## [2026-10-22] script | L1-01 순서 변경 — 강사 소개(S01~S08)를 맨 앞으로, 여행 훅·표지를 S09·S10으로
- S01에 인사와 "이 영상을 보면" 한 줄 추가(첫 30초 규칙), S08·S10 연결 문장 수정, S22 "아까 처음에" → "아까"

## [2026-10-22] script | L1-01 S01(경력)·S02(스타트업 합류) 한 블록으로 병합 — [S] 28블록으로 재번호

## [2026-10-23] ingest | 그래프 엔지니어링·이밸 엔지니어링 용어 확인 (arXiv 2608.21156, SiliconANGLE 등)
- raw 추가: graph-eval-engineering / 신규: sources/graph-eval-engineering / 갱신: concepts/ai-engineering-paradigms, index

## [2026-10-23] script | L1-01 S05에 이밸·그래프 엔지니어링 추가

## [2026-10-23] ingest | 강사 현재 회사 확인 — 대기업 산하 헬스케어 플랫폼 회사(커머스 플랫폼 개발), "20명 → 5명" 경험의 무대
- raw 추가: instructor-current-company / 갱신: sources/instructor-career-story, sources/instructor-interview-ai-dev-reality, practices/ai-native-dev-team, syntheses/ai-coding-timeline, L1-01 outline·script S25

## [2026-10-23] script | L1-01 여행 장면(옛 S08)을 실화 블록 바로 앞(S20)으로 이동 — S07·S20·S21·S24 연결 문장 수정

## [2026-10-23] setup | 슬라이드 제작을 사용자(Gemini)로 변경 — slides.md·Google Slides 커넥터 단계 제거
- CLAUDE.md 1·3·4·5·6·7절 갱신, outline `gslides_url` → `slides_url`. Claude는 대본 수정 시 영향받는 [S] 번호를 알린다.

## [2026-10-25] setup | 슬라이드 덱을 Google Drive에서 관리 — CLAUDE.md 5절에 폴더·파일명 규칙, Claude는 Drive 커넥터로 읽기만

## [2026-10-25] setup | 강의 덱 Drive 폴더(강의자료) 등록, L1-01 덱 링크를 outline slides_url에 기록

## [2026-10-25] outline | L1-01 제목 변경 — "AI 시대에도 변하지 않는 것 — LLM 위키로 쌓는 나만의 지식" (여행은 예시로)
- outline 기획 의도·학습 목표, script S08 표지, curriculum, overview 갱신. 레슨 ID·폴더명 유지

## [2026-10-25] setup | 옛 슬라이드 파이프라인 파일 삭제 — L1-01 slides.md, templates/slides.md, tools/gslides/

## [2026-10-25] setup | 슬라이드 텍스트 수정을 Claude가 담당(항상 사용자 컨펌), 싱크 확인 절차와 outline `slides_synced` 추가

## [2026-10-25] setup | sync-speaker-notes 스킬 추가 — script.md [S] 블록 → 같은 번호 슬라이드 발표자 노트 (컨펌 후 쓰기)
- .claude/skills/sync-speaker-notes (SKILL.md + scripts/notes_sync.py), .claude/settings.json PostToolUse 훅, CLAUDE.md 5절, outline `notes_synced`

## [2026-10-25] slides | L1-01 발표자 노트 동기화 (S01–S28 전체, 빈 슬라이드 S09·S25–S28은 위치로 매칭)
- 덱 노트가 전부 비어 있어 28장 모두 채움. script 85b361a 기준

## [2026-10-25] ingest | S01 사실 확인 — 무한도전(2015) 빅데이터 활용, LLM 다음 토큰 예측
- raw 추가: bigdata-llm-facts / 신규: sources/bigdata-llm-facts / 갱신: index

## [2026-10-25] script | L1-01 S01 강사 수정본 반영 — 띄어쓰기·맞춤법 12곳 수정, 내레이션 약 5,670자·26분

## [2026-10-25] slides | L1-01 S01 본문 "개발 총괄" → "개발 담당", S01 발표자 노트 동기화 (강사 컨펌)

## [2026-10-25] ingest | S01 사실 확인 — 무한도전(2015) 빅데이터 활용, LLM 다음 토큰 예측
- raw 추가: bigdata-llm-facts / 신규: sources/bigdata-llm-facts / 갱신: index

## [2026-10-25] script | L1-01 S01 강사 수정본 반영 — 띄어쓰기·맞춤법 12곳 수정, 내레이션 약 5,670자·26분

## [2026-10-25] slides | L1-01 S01 본문 "개발 총괄" → "개발 담당", S01 발표자 노트 동기화 (강사 컨펌)

## [2026-10-25] slides | L1-01 S02 발표자 노트 동기화 (강사가 "GPT-3를 개량한 모델로" → "GPT-3로" 수정)
