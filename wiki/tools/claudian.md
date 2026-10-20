---
type: tool
title: Claudian (Obsidian 플러그인)
aliases: [Claudian]
levels: [L1, L2]
volatility: high
updated: 2026-10-21
sources: [sources/claudian-readme]
tags: [obsidian-plugin]
---

# Claudian

[[tools/obsidian]] 사이드바에 [[tools/claude-code]] 같은 AI 에이전트를 넣어 주는 커뮤니티 플러그인.
볼트(노트 폴더)가 그대로 에이전트의 작업 폴더가 되어, 대화하면 노트가 생기고 바뀌는 것을 옆에서 바로 볼 수 있다.

## 본문

### 요구사항 (as of 2026-10)
- Obsidian **v1.13.0 이상**, 데스크톱 전용.
- Claude Code CLI 설치·로그인 완료 상태 (Claudian이 내부에서 실행).

### 설치
설정 → 커뮤니티 플러그인 → 둘러보기 → "Claudian" 검색 → 설치 → 활성화 → 리본 아이콘 또는 명령 팔레트로 열기.

### 자주 막히는 곳
| 증상 | 원인 | 해결 |
|---|---|---|
| `spawn claude ENOENT`, "Claude Code CLI not found" | CLI 경로 탐지 실패 | 터미널 `which claude` → 설정 → Claudian → Providers → Claude Code → CLI path |
| 터미널에선 되는데 Obsidian에서 `authentication_failed` | 시스템 `ANTHROPIC_API_KEY`가 구독 로그인보다 우선 | Custom variables에 `ANTHROPIC_API_KEY=` 빈 값 |
| (Windows) 경로 | `.cmd`·`.ps1` 래퍼 사용 | `where.exe claude`로 `claude.exe` 지정, Obsidian 재시작 |

### 알아둘 점
- 입력·첨부 파일·도구 결과는 Anthropic으로 전송된다. 플러그인 자체 텔레메트리는 없음.
- 그 밖의 기능: 인라인 편집, `@`로 파일 참조, 슬래시 명령, 탭.

## 관련
- [[tools/claude-code]] · [[tools/obsidian]] · [[concepts/llm-wiki]]

## 출처
- [[sources/claudian-readme]]
