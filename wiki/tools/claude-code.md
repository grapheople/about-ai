---
type: tool
title: Claude Code
aliases: [claude]
levels: [L1, L3, L4]
volatility: high
updated: 2026-10-21
sources: [sources/claude-code-setup-docs, sources/claude-code-terminal-guide, sources/claude-pricing]
tags: [anthropic, agent]
---

# Claude Code

Anthropic의 에이전트형 AI 도구. 내 컴퓨터의 폴더에서 파일을 읽고·쓰고·명령을 실행한다.
코딩용으로 알려졌지만 "원하는 것을 말로 설명하면 된다" — 비개발자도 쓸 수 있다.

## 본문

### 설치 (macOS, as of 2026-10)
1. `Cmd + Space` → "Terminal" → `Enter`
2. `curl -fsSL https://claude.ai/install.sh | bash` 붙여넣기 → `Enter` → 진행 표시 없이 대기 → "Claude Code successfully installed!"
3. `claude` 입력 → 브라우저에서 로그인
- 요구: macOS 13.0+, 4GB+ RAM.
- 확인: 새 터미널에서 `claude --version`.
- `command not found: claude` → PATH 문제 (공식 문서 해결법 → 새 터미널).
- Windows: PowerShell에서 `irm https://claude.ai/install.ps1 | iex`.

### 필요한 플랜 (as of 2026-10)
- **Pro($20/월) 이상** 필요. Free 플랜에는 없음. Max·Team·Enterprise·Console 포함.
- > [!conflict] 2026-04 신규 가입자 약 2% 대상으로 Pro에서 Claude Code를 빼는 테스트가 보도됨. 현재 요금제 페이지는 Pro 포함으로 표기. 촬영 직전 재확인.

### 터미널 없이 쓰기
- > [!unverified] 공식 문서는 "터미널이 싫으면 Desktop 앱"을 안내한다. 그러나 [[tools/claudian]]은 Claude Code **CLI**를 찾아 실행하므로, Desktop 앱 설치만으로 Claudian이 동작하는지는 확인되지 않았다. L1-01은 CLI 설치 경로로 간다.

### 터미널 기본 조작 (초보자용)
클릭 대신 화살표 키, `Esc` 중단, `exit` 종료, `/help` 명령 목록.

## 관련
- [[tools/claudian]] · [[tools/obsidian]] · [[concepts/llm-wiki]]

## 출처
- [[sources/claude-code-setup-docs]] · [[sources/claude-code-terminal-guide]] · [[sources/claude-pricing]]
