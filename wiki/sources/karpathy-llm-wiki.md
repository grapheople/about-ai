---
type: source
title: Karpathy — LLM Wiki (gist)
raw: raw/2026-10-20-karpathy-llm-wiki.md
author: Andrej Karpathy
published: 2026 (정확한 게시일 미확인)
ingested: 2026-10-21
levels: [L1, L2, L4]
tags: [llm-wiki, knowledge-base, rag]
---

# Karpathy — LLM Wiki

LLM이 원본 자료를 읽어 **지속적으로 유지되는 마크다운 위키**를 직접 쓰고 고치게 하는 개인 지식 베이스 패턴.
질문할 때마다 원문에서 다시 찾는 RAG와 달리, 지식이 한 번 정리되어 **계속 쌓인다**.

## 저자
- Andrej Karpathy — OpenAI 공동 창업자, Tesla AI 리드 출신. 2026-05-19 Anthropic 사전학습 팀 합류 발표 (as of 2026-10, [[sources/ai-coding-timeline-facts]]).

## 핵심 내용
- 3계층: 원본 소스(불변) / 위키(LLM이 소유·작성) / 스키마(CLAUDE.md 같은 규칙 문서).
- 3가지 작업: Ingest(자료 넣기 → 10~15개 페이지 갱신), Query(답하고 좋은 답은 위키에 되돌려 저장), Lint(모순·고아 페이지·낡은 주장 점검).
- index.md(내용 카탈로그)와 log.md(시간순 기록) 두 파일로 길을 찾는다. 수백 페이지 규모까지는 임베딩 RAG 없이도 충분.
- 사람은 자료 고르기·방향·질문, LLM은 요약·교차참조·정리 같은 "장부 관리"를 맡는다.
- "Obsidian은 IDE, LLM은 프로그래머, 위키는 코드베이스."
- 활용 예시에 **여행 계획(trip planning)**이 명시되어 있다.
- 사용법 자체가 "이 글을 LLM 에이전트에게 붙여 넣고 같이 구체화하라"는 것.

## 강의에 쓸 만한 포인트
- L1-01: "대화는 사라지지만 위키는 쌓인다" 대비, gist를 Claude에게 붙여 넣어 CLAUDE.md를 같이 만드는 장면의 근거.
- L4-02: RAG와의 비교.
- 사람이 위키를 포기하는 이유는 유지 비용 → LLM이 유지 비용을 0에 가깝게 만든다 (Memex 비유).

## 갱신한 위키 페이지
- [[concepts/llm-wiki]], [[concepts/rag]], [[tools/obsidian]]
