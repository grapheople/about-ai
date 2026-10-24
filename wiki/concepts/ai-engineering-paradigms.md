---
type: concept
title: 프롬프트 → 컨텍스트 → 하네스 → 루프 → 그래프 엔지니어링 (+ 이밸)
aliases: [context engineering, harness engineering, loop engineering, 컨텍스트 엔지니어링, 하네스 엔지니어링, 루프 엔지니어링, graph engineering, eval engineering, 그래프 엔지니어링, 이밸 엔지니어링]
levels: [L1, L3, L4]
volatility: high
updated: 2026-10-23
sources: [sources/ai-coding-timeline-facts, sources/instructor-career-story, sources/graph-eval-engineering]
tags: [agent, methodology]
---

# 프롬프트 → 컨텍스트 → 하네스 → 루프 → 그래프 엔지니어링 (+ 이밸)

AI를 잘 쓰는 방법론이 "질문 한 번 잘 하기"에서 "AI가 볼 정보 고르기", "AI를 둘러싼 장치 만들기",
"사람 없이도 반복해서 일하게 하기", "여러 AI를 함께 엮기"로 넓어져 온 흐름. 이와 나란히 "AI가 한 일을 자동으로 평가하기"(이밸)도 따로 이름을 얻었다. 앞 단계는 사라지지 않고 다음 단계의 토대가 된다 (as of 2026-10).

## 본문
| 단계 | 무엇을 다루나 | 한 줄 비유 |
|---|---|---|
| 프롬프트 엔지니어링 | 시스템 프롬프트 + 사용자 메시지, 한 번 묻고 답하기 | 질문을 잘 하기 |
| 컨텍스트 엔지니어링 | 다음 작업에 모델이 볼 정보를 고르고 노이즈를 뺀다 | 필요한 자료를 챙겨 주기 |
| 하네스 엔지니어링 | 도구·스킬·MCP 서버·시스템 프롬프트·훅·샌드박스·관측. "에이전트 = 모델 + 하네스" | 일할 작업 환경 갖춰 주기 |
| 루프 엔지니어링 | 에이전트를 반복 실행·검증·기억하게 해 사람이 매번 지시하지 않게 한다 | 알아서 돌아가는 체계 만들기 |
| 그래프 엔지니어링 | 작업·에이전트·상태를 그래프로 표현해 여러 에이전트를 조율한다 ("시스템 지능") | 여러 AI를 한 팀으로 엮기 |
| 이밸 엔지니어링 | 에이전트 평가를 설계·자동 실행·운영. 최종 답 + 경로·도구 사용 채점, LLM-as-a-judge | AI가 한 일을 자동 채점하기 |

- 출처(codecentric)에 따르면 각 계층은 아래 계층의 약점을 물려받는다.
- "루프 엔지니어링"은 Addy Osmani가 2026-06-07에 붙인 이름이다.
- 그래프 엔지니어링은 arXiv 2608.21156(2026-08)이 제안했다. 앞의 네 단계를 "단일 에이전트 최적화"로 묶고, 그 다음 단계로 여러 에이전트의 협업을 둔다.
- 이밸 엔지니어링은 arXiv 2608.21156이 제시한 프롬프트→그래프 사다리에는 들어 있지 않아 표에서는 맨 끝에 따로 두었다. 합의된 정의가 없고 출처 대부분이 벤더·블로그다 (as of 2026-10).
- > [!conflict] 계층 관계의 해석이 갈린다. arXiv 2608.21884는 "각 층이 앞 층을 포함한다"고 보고, 다른 논문은 루프가 하네스 위에 따로 놓인다고 본다. 용어가 빠르게 퍼졌지만 실무 채택은 측정되지 않았다는 지적도 있다 ([[sources/ai-coding-timeline-facts]]).
- 강사 경험: Claude Code의 스킬·플러그인 생태계와 함께 이 변천을 직접 겪었다 ([[sources/instructor-career-story]]).

## 관련
- [[tools/claude-code]] · [[concepts/llm-wiki]] · [[syntheses/ai-coding-timeline]]

## 출처
- [[sources/ai-coding-timeline-facts]] · [[sources/instructor-career-story]] · [[sources/graph-eval-engineering]]
