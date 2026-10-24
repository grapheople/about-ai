---
type: web-clipping
collected: 2026-10-22
context: L1-01 도입부의 날짜·인물 사실 확인용 웹 검색 결과 요약
---

# AI 코딩 도구 타임라인 & 관련 인물 — 웹 확인 메모

## GitHub Copilot
- 2021-06-29 초대제 기술 프리뷰 시작, 2022-06-21 정식 출시(GA). 개인 $10/월.
- 기반 모델은 OpenAI Codex — GPT-3를 개량한 후손 모델.
- 출처: https://visualstudiomagazine.com/Articles/2022/06/21/github-copilot-ga.aspx ,
  https://techcrunch.com/2022/06/21/copilot-githubs-ai-powered-programming-assistant-is-now-generally-available/ ,
  https://en.wikipedia.org/wiki/GitHub_Copilot

## GPT-4
- OpenAI가 2023-03-14 발표·출시. 초기에는 ChatGPT Plus와 API 대기자 명단으로 제한 제공.
- 출처: https://en.wikipedia.org/wiki/GPT-4

## Claude Code
- 2025-02-24 Claude 3.7 Sonnet과 함께 "제한된 리서치 프리뷰"로 공개. 터미널에서 쓰는 에이전트형 코딩 도구.
- 출처: https://www.anthropic.com/news/claude-3-7-sonnet ,
  https://sdtimes.com/ai/anthropic-releases-claude-3-7-sonnet-and-claude-code/

## Claude Code 플러그인·스킬 (as of 2026-10)
- 플러그인 = 스킬·에이전트·훅·MCP 서버 등을 한 묶음으로 설치하는 디렉터리. 마켓플레이스에서 설치.
- 스킬 = Claude가 필요할 때 불러 쓰는 `SKILL.md` 지침. 명령으로도 실행 가능.
- 출처: https://code.claude.com/docs/en/plugins

## 프롬프트 → 컨텍스트 → 하네스 → 루프 엔지니어링
- codecentric 블로그 (Benjamin Font Pera, 2026-07-05) 정리:
  - 프롬프트 엔지니어링: 단일 프롬프트(시스템 프롬프트 + 사용자 메시지)로 한 번 묻고 답하기.
  - 컨텍스트 엔지니어링: 모델이 다음 작업에 볼 정보를 고르고 노이즈를 빼는 일. 위 계층의 토대.
  - 하네스 엔지니어링: 코딩 에이전트를 둘러싼 장치 — 도구·스킬·MCP 서버·시스템 프롬프트·훅·샌드박스·관측. "에이전트 = 모델 + 하네스".
  - 루프 엔지니어링: 사람이 매번 지시하지 않아도 에이전트를 반복 실행·검증·기억하게 하는 시스템. 하네스 위의 계층.
  - "루프 엔지니어링"은 Addy Osmani가 2026-06-07에 명명 (Boris Cherny 발언 직후).
- IBM: 루프 엔지니어링 = 최소한의 사람 개입으로 에이전트를 목표까지 반복 유도하는 워크플로 설계.
- arXiv 2608.21884: 용어가 빠르게 퍼졌지만 정의는 저자마다 다르고 실무 채택은 측정되지 않았다.
- 출처: https://www.codecentric.de/en/knowledge-hub/blog/loop-harness-context-engineering-explained ,
  https://www.ibm.com/think/topics/loop-engineering , https://arxiv.org/html/2608.21884v1

## Andrej Karpathy
- OpenAI 공동 창업자. Tesla에서 AI를 이끌었다.
- 2026-05-19 X에 "Anthropic에 합류했다"고 발표. 사전학습(pre-training) 팀(리드 Nick Joseph)에서
  Claude로 사전학습 연구를 가속하는 팀을 꾸린다 (Anthropic 대변인, TechCrunch).
- 출처: https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/ ,
  https://en.wikipedia.org/wiki/Andrej_Karpathy
