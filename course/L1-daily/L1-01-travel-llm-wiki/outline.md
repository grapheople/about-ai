---
lesson: L1-01
title: Claude와 Obsidian으로 "기억하는 여행 계획" 만들기 — LLM 위키 입문
level: L1
status: slides   # idea | outline | script | slides | final | recorded | published
target_minutes: 24
prerequisites: []
gslides_url: 
updated: 2026-10-20
---

# L1-01 Claude와 Obsidian으로 "기억하는 여행 계획" 만들기

## 이 영상을 보면
터미널을 처음 여는 사람도 Obsidian + Claudian으로 Claude와 대화하며,
**대화가 사라지지 않고 쌓이는 나만의 여행 위키**를 만들어 실제 여행 계획을 짤 수 있다.

## 왜 이 영상인가 (기획 의도)
- 채널의 첫 영상. "일상 AI 활용" 레벨이지만, 단순 채팅을 넘어 **지식이 쌓이는 사용법**을 첫인상으로 보여 준다.
- 근거는 강사 본인의 실제 경험: 2026-06 도쿄 가족여행을 LLM 위키(pathfinder 저장소)로 준비하고,
  현지에서 날이 좋아 실내 일정(teamLab Planets)을 수상버스(크루즈)로 바꿨을 때 위키 전체가 함께 갱신된 경험.
- **성공 기준: 반응.** 어떤 반응이든 소중하고, **무반응이 실패**다.
  → 첫 30초 훅과, 댓글을 부르는 마무리 질문을 설계의 일부로 다룬다.

## 대상
- 비개발자. 터미널을 **처음** 열어 보는 사람.
- Claude 유료 플랜(Pro 이상)이 필요하다는 점을 영상 앞부분에서 안내한다 (무료 플랜 불가, as of 2026-10).

## 학습 목표 (3개 이내)
1. LLM 위키가 일반 채팅과 무엇이 다른지 한 문장으로 설명할 수 있다. ("대화는 사라지지만, 위키는 쌓인다")
2. Mac에서 Obsidian · Claude Code · Claudian을 설치하고 로그인까지 마칠 수 있다.
3. Karpathy의 LLM 위키 글을 Claude에게 건네 **나만의 여행 위키 규칙(CLAUDE.md)을 함께 만들고**, 여행 계획을 짜고 고칠 수 있다.

## 확정된 결정 (인터뷰에서 사용자가 정한 것)
- 도구: **Obsidian + Claudian 플러그인** (내부적으로 Claude Code 사용).
- **설치와 시연을 한 편에** 담는다.
- 촬영은 **Mac만**. Windows는 설명란 안내로 대체.
- 시청자는 **빈 볼트에서 시작**한다. 강사의 pathfinder는 **"계속 쓰면 이렇게 자란다"는 완성본**으로 훅·엔딩에 보여 준다.
- CLAUDE.md는 배포 파일로 주지 않고, **시청자가 gist 링크를 Claude에게 붙여 넣어 함께 만드는 과정**을 보여 준다.
  시청자마다 결과가 조금 달라도 된다 (영상에서 그렇게 말해 준다).
- 시연 첫 요청 문장: **"6월에 가족이랑 3박 4일 도쿄 여행 계획 짜줘. 동행자는 6세 아이와 아내 둘이야."**
- 클라이맥스 소재: 실제 여행 6/4의 현지 변경 **하나만** — 날이 좋아 실내 일정을 **수상버스(크루즈)·도쿄타워·아자부다이 동선으로 교체**.
  (비 시나리오는 실화가 아니므로 쓰지 않는다.)
- 강사 이야기 구간: 여행 계획(설치·시연) **이전**에, 현업에서 AI로 커머스 플랫폼을 개발하는 개발자로서 느끼는 요즘 세상에 대한 멘트를 넣는다.
- 촬영 형식: **슬라이드 + 화면녹화**. 개념·요약은 슬라이드, 설치·시연은 화면녹화. 얼굴은 작은 원형 캠 또는 없음.
- pathfinder 노출: **그래프 뷰 + 본문 일부**(log·일정표). 가족 세부 정보는 촬영용 사본에서 가리거나 수정한다.

## 흐름
| # | 섹션 | 핵심 메시지 | 근거 | 예상 분 |
|---|---|---|---|---|
| 1 | 훅 | 완성된 pathfinder 위키(그래프 뷰) + "현지에서 한 문장 → 일정·식당·요약이 같이 바뀌는" 장면을 먼저 보여 준다 | [[practices/travel-llm-wiki]] | 0.5 |
| 2 | 강사 이야기: 요즘 세상 | 현업에서 AI로 커머스 플랫폼을 개발하는 개발자로서 느끼는 요즘 세상. 일하는 방식이 어떻게 바뀌었는지 → "그래서 개발자가 아니어도 지금 시작해야 한다"로 이 영상과 연결 | [[practices/ai-native-dev-team]] (강사 본인 경험·의견) | 2 |
| 3 | 오늘 할 것 · 준비물 | 결과물 예고, 필요한 것: Mac · Claude 유료 플랜 · 30분 | [[sources/claude-pricing]] | 1 |
| 4 | LLM 위키란 | 채팅/RAG는 매번 처음부터 찾는다 vs 위키는 정리된 지식이 쌓인다. 사람은 질문·방향, AI는 정리·연결 | [[sources/karpathy-llm-wiki]], [[concepts/llm-wiki]] | 3 |
| 5 | 설치 ① Obsidian | 다운로드 → 새 볼트 만들기 ("travel-wiki") | [[tools/obsidian]] | 1.5 |
| 6 | 설치 ② Claude Code | 생애 첫 터미널: 여는 법 → 명령 한 줄 붙여넣기 → `claude` 실행 → 브라우저 로그인. "무서워 보여도 여기가 유일한 터미널 구간" | [[tools/claude-code]] | 3 |
| 7 | 설치 ③ Claudian | 설정 → 커뮤니티 플러그인 → "Claudian" 검색·설치·활성화 → 사이드바에 Claude 창 | [[tools/claudian]] | 1.5 |
| 8 | 위키 규칙 함께 만들기 | gist 링크 + "이걸로 내 여행 위키를 만들어 줘" → Claude가 질문하며 CLAUDE.md·폴더·내 여행 취향 프로필 생성 | [[concepts/llm-wiki]] | 3 |
| 9 | 자료 넣기 (Ingest) | 도쿄 여행 자료 1~2개 → 위키 페이지 생성·연결 → 그래프 뷰에서 점이 늘어나는 장면 | [[concepts/llm-wiki]] | 2.5 |
| 10 | 계획 요청 | 첫 요청 문장 입력 → 위키를 근거로 일정 파일 생성. 아이 동반 조건이 일정에 반영되는 것 짚기 | [[practices/travel-llm-wiki]] | 2 |
| 11 | 클라이맥스: 현지 변경 | 강사 실화 한 줄 소개(6/4 날이 좋아 크루즈로) → 시연 볼트에서 재현: "여행 둘째 날인데 날이 좋아서 실내 대신 수상버스 타고 싶어" → 일정·식당·요약이 함께 바뀜. 채팅이었다면 처음부터 다시 설명해야 했다는 대비 | [[practices/travel-llm-wiki]] | 2.5 |
| 12 | 완성본 | pathfinder: 쓸수록 이렇게 자란다 — 그래프 뷰, 현지용 한 화면 요약(quick-reference), 두 번째 여행(제천)이 같은 위키에 쌓인 모습 | [[sources/pathfinder-case]] | 1 |
| 13 | 요약 · 다음 영상 · 댓글 질문 | 3줄 요약 → 다음 영상 예고 → "여러분은 어떤 위키를 만들고 싶나요?" 댓글 유도 | — | 0.5 |

합계 약 24분. 8~11번은 Claude 응답 대기 시간을 편집으로 빨리감기 한다.

## 제작 메모
- **개인정보**: pathfinder는 그래프 뷰 + log·일정표 일부까지 보여 준다. 임신 주수 등 가족 세부 정보는 **촬영용 사본 볼트**에서 수정한 뒤 녹화한다 (원본 pathfinder는 건드리지 않음).
- **슬라이드 vs 화면녹화**: 1·5~12번은 화면녹화가 중심이고, 슬라이드는 각 구간의 "지금 할 것" 표지 1장 정도. 2번(강사 이야기)·4번(LLM 위키 개념)·3·13번은 슬라이드 중심. 화면녹화 구간 대본은 낭독문보다 진행 큐시트에 가깝게 쓴다.
- **재현 가능성**: 7~10번은 Claude 응답이 매번 다르다. 촬영 전 리허설 볼트로 한 번 돌려 보고, 실제 촬영본을 쓴다.
- **클라이맥스 재현**: 시연 볼트는 여행 전 상태이므로 11번은 "여행 둘째 날이라고 가정하고" 요청한다.
- **Windows 안내(설명란)**: 공식 설치 문서 링크, PowerShell 설치 명령, Claudian에서 Claude Code 경로 지정, `ANTHROPIC_API_KEY` 환경변수로 인한 `authentication_failed` 대처.
- **강사 이야기 구간 (2번)**: 내용은 강사 본인의 생각이므로 대본 단계에서 강사 인터뷰로 채운다. Claude가 의견을 지어내지 않는다.
  회사·사내 시스템 등 공개하면 안 되는 내용은 일반화해서 말한다. 업계 수치·통계를 인용하면 위키 출처를 단다.
  - 강사 재료 (raw/2026-10-21-instructor-interview-ai-dev-reality.md):
    ① 코드를 한 줄도 직접 짜지 않는다 — 개발은 전부 AI가 한다.
    ② AI의 영역이 개발 → 기획·QA·디자인까지 넓어졌다.
    ③ 20명 규모 프로젝트를 5명이 한다.
    ④ 모든 의사소통은 AI가 쓴 "바이블 같은 기획서"로 이뤄진다.
  - 연결 고리 (Claude 제안): ④의 "모두가 기준으로 삼는, AI가 쓰고 계속 고치는 문서"가 바로 이 영상의 LLM 위키다.
    "회사에서 5명이 20명 몫을 하게 만든 그 방식을, 오늘 여러분의 여행 계획에 써 봅니다"로 3·4번에 넘긴다.
- **Ingest 시연 자료 (Claude 결정)**: 한국어 위키백과 "아사쿠사", "긴자" 문서 URL 2개. 누구나 따라 할 수 있고 화면에 띄워도 저작권 부담이 적다.
  pathfinder도 같은 문서를 소스로 썼다. 아이 동반 조건은 자료가 아니라 첫 요청 문장과 프로필에서 들어간다.
- **엔딩 "완성본" 구성 (Claude 결정)**: 도쿄 trip에 debrief.md가 없으므로 회고 대신 quick-reference와 제천 trip으로 "쌓이는" 모습을 보여 준다.
- **휘발성 정보**: 요금제·설치 명령·Claudian 요구사항(Obsidian v1.13.0+)은 촬영 직전에 다시 확인한다 (as of 2026-10).

## 필요한 소스 — ingest 완료 (2026-10-21)
- [x] Karpathy LLM Wiki → [[sources/karpathy-llm-wiki]], [[concepts/llm-wiki]], [[concepts/rag]]
- [x] Claude Code 설치 문서·터미널 가이드 → [[sources/claude-code-setup-docs]], [[sources/claude-code-terminal-guide]], [[tools/claude-code]]
- [x] Claude 요금제 → [[sources/claude-pricing]]
- [x] Claudian README → [[sources/claudian-readme]], [[tools/claudian]]
- [x] Obsidian 설치·라이선스 → [[sources/obsidian-install-license]], [[tools/obsidian]]
- [x] pathfinder 사례 → [[sources/pathfinder-case]], [[practices/travel-llm-wiki]]
- [x] 강사 인터뷰 → [[sources/instructor-interview-ai-dev-reality]], [[practices/ai-native-dev-team]]

## 열린 확인 사항
- Claude Code Desktop 앱만으로 Claudian이 동작하는지 미확인 → 현재는 CLI 설치 경로로 간다 ([[tools/claude-code]]).
