---
type: concept
title: LLM 위키 (LLM Wiki)
aliases: [LLM Wiki, 지식이 쌓이는 위키]
levels: [L1, L2, L4]
volatility: low
updated: 2026-10-21
sources: [sources/karpathy-llm-wiki, sources/pathfinder-case]
tags: [knowledge-base]
---

# LLM 위키

LLM이 원본 자료를 읽고 **마크다운 위키를 직접 쓰고 계속 고쳐 나가는** 지식 관리 방식.
사람은 자료를 고르고 질문하며, 정리·연결·갱신은 LLM이 한다. 한 번 정리된 지식은 다음 질문 때 처음부터 다시 찾지 않고 **쌓인다**.

## 본문

### 세 계층
| 계층 | 누가 쓰나 | 예 |
|---|---|---|
| 원본 소스 | 사람이 모음, 수정 안 함 | 블로그 글, 위키백과 문서, 메모 |
| 위키 | LLM이 작성·유지 | 장소 페이지, 일정, 비교표 |
| 스키마 | 사람과 LLM이 함께 다듬음 | CLAUDE.md (규칙·폴더 구조·작업 순서) |

### 세 가지 작업
- **Ingest**: 자료를 넣으면 요약 페이지를 쓰고 관련 페이지 10~15개를 함께 갱신.
- **Query**: 위키를 근거로 답하고, 좋은 답은 새 페이지로 저장.
- **Lint**: 모순·낡은 주장·연결 안 된 페이지 점검.

### 그냥 채팅과 무엇이 다른가
- 채팅: 대화가 끝나면 맥락이 사라진다. 다음에 다시 설명해야 한다.
- [[concepts/rag]]: 매번 원문 조각을 다시 찾아 조합한다. 쌓이지 않는다.
- LLM 위키: 정리된 결과가 파일로 남고, 새 정보가 오면 관련 페이지가 **함께** 바뀐다.
  예: pathfinder에서 현지 동선을 바꾸자 일정·식당·현지 요약이 한 번에 갱신됨 ([[practices/travel-llm-wiki]]).

### 시작하는 법
Karpathy의 글은 구현이 아니라 "아이디어"다. 글을 LLM 에이전트에게 붙여 넣고 내 용도에 맞는 규칙을 **같이** 만드는 것이 의도된 사용법이다.
그래서 사람마다 결과 구조가 조금씩 달라도 정상이다.

### 도구 조합
[[tools/obsidian]](읽기·그래프 뷰) + [[tools/claude-code]](작성) — 둘을 한 화면에 묶는 것이 [[tools/claudian]].

## 관련
- [[concepts/rag]] · [[practices/travel-llm-wiki]] · [[practices/ai-native-dev-team]]

## 출처
- [[sources/karpathy-llm-wiki]] · [[sources/pathfinder-case]]
