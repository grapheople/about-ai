---
type: concept
title: 검색 증강 생성(RAG)
aliases: [RAG, Retrieval-Augmented Generation]
levels: [L1, L4]
volatility: low
updated: 2026-10-21
sources: [sources/karpathy-llm-wiki]
tags: [retrieval]
---

# 검색 증강 생성(RAG)

질문을 받으면 그때그때 문서 더미에서 관련 조각을 찾아 LLM에게 건네 답하게 하는 방식.
NotebookLM, ChatGPT 파일 업로드 등 대부분의 "내 문서로 답하기"가 이렇게 동작한다.

## 본문
- 장점: 문서를 올리기만 하면 바로 쓸 수 있다.
- 한계 (Karpathy): 매 질문마다 지식을 처음부터 다시 찾는다. 여러 문서를 종합해야 하는 질문일수록 매번 조각을 다시 맞춰야 하고, **아무것도 쌓이지 않는다**.
- [[concepts/llm-wiki]]는 이 한계를 "미리 정리해 두고 계속 고친다"로 푼다. 수백 페이지 규모까지는 index.md만으로 충분하다고 한다.
- L4에서 RAG 구현을 다룰 때 별도 소스로 보강 필요.

## 관련
- [[concepts/llm-wiki]]

## 출처
- [[sources/karpathy-llm-wiki]]
