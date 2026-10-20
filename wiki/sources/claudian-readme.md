---
type: source
title: Claudian README (GitHub)
raw: raw/2026-10-21-claudian-readme.md
author: YishenTu
published: 2026-10 (캡처일)
ingested: 2026-10-21
levels: [L1, L2]
tags: [claudian, obsidian, plugin]
---

# Claudian README

Obsidian 볼트 안에 Claude Code 등 코딩 에이전트를 넣는 플러그인. 볼트가 에이전트의 작업 폴더가 된다. (as of 2026-10)

## 핵심 내용
- 지원 에이전트: Claude Code, Codex, Grok Build, OpenCode, Pi, DeepSeek Harness. 하나 이상 설치 필요.
- 요구사항: **Obsidian v1.13.0+**, 데스크톱 전용(macOS·Linux·Windows), 호환 구독 또는 API.
- 설치(권장): 설정 → 커뮤니티 플러그인 → 둘러보기 → "Claudian" 검색 → 설치 → 활성화.
- 기능: 사이드바 채팅, 인라인 편집, 슬래시 명령·스킬, `@`로 파일 참조, 탭·세션 관리, MCP.
- 개인정보: 입력·첨부 파일·도구 출력은 선택한 제공자(Claude면 Anthropic)로 전송. 플러그인 자체 텔레메트리 없음.
- 문제 해결:
  - CLI를 못 찾음(`spawn claude ENOENT`): 터미널에서 `which claude`로 경로 확인 → 설정 → Claudian → Providers → Claude Code → CLI path.
  - macOS는 로그인 셸에서 PATH를 읽어 자동 탐지.
  - `authentication_failed`: 시스템의 `ANTHROPIC_API_KEY`/`ANTHROPIC_AUTH_TOKEN`이 구독 로그인보다 우선 → Custom variables에 `ANTHROPIC_API_KEY=` 빈 값 추가.

## 강의에 쓸 만한 포인트
- L1-01 설치 ③: 커뮤니티 플러그인 검색 설치 장면.
- 설명란 문제 해결 팁 2개 (CLI 경로, API 키 충돌).

## 갱신한 위키 페이지
- [[tools/claudian]], [[tools/obsidian]]
