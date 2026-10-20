---
type: source
title: Claude Code 공식 설치 문서 (Advanced setup)
raw: raw/2026-10-21-claude-code-setup-docs.md
author: Anthropic
published: 2026-10 (캡처일)
ingested: 2026-10-21
levels: [L1, L3]
tags: [claude-code, install]
---

# Claude Code 공식 설치 문서

시스템 요구사항, OS별 설치 명령, 로그인 요구 플랜을 담은 공식 문서. (as of 2026-10)

## 핵심 내용
- 요구사항: macOS 13.0+, Windows 10 1809+, 4GB+ RAM, 인터넷 연결, 지원 국가.
- 권장 설치(Native): macOS `curl -fsSL https://claude.ai/install.sh | bash` / Windows PowerShell `irm https://claude.ai/install.ps1 | iex`. 대안: Homebrew `brew install --cask claude-code`, WinGet.
- 설치 중 진행 표시가 없다. 끝나면 새 터미널에서 `claude --version`으로 확인.
- Native 설치는 백그라운드 자동 업데이트. Homebrew·WinGet은 수동.
- **Pro, Max, Team, Enterprise, Console 계정 필요. 무료 claude.ai 플랜은 Claude Code 미포함.**
- 로그인: `claude` 실행 → 브라우저에서 로그인.
- 터미널을 원치 않으면 Desktop 앱으로 Claude Code를 쓸 수 있다는 안내가 있다.
- Windows: Git for Windows는 선택. 없으면 PowerShell 도구 사용.

## 강의에 쓸 만한 포인트
- L1-01 설치 ②: 명령 한 줄, "진행 표시 없음 → 기다리기" 안내.

## 갱신한 위키 페이지
- [[tools/claude-code]]
