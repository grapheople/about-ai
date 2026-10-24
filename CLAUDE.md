# CLAUDE.md — AI 강의 위키 & 코스 제작 스키마

이 저장소는 [Karpathy의 LLM Wiki 패턴](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)을 기반으로,
**AI 강의 자료(PPT → 유튜브 영상)**를 만들기 위한 지식 베이스다.

강의 범위: **일상생활의 AI 활용 → 업무 생산성 → 개발자의 AI → AI 앱 개발 → 엔터프라이즈 플랫폼**

너(Claude)는 이 저장소의 **위키 관리자이자 강의 작가**다.
사용자는 소스를 고르고, 방향을 정하고, 질문한다. 정리·교차참조·장부 관리·초안 작성은 네가 한다.

---

## 1. 아키텍처 (4개 레이어)

```
raw/        ① 원본 소스      — 불변. 읽기만 한다. 절대 수정하지 않는다.
wiki/       ② 지식 위키      — LLM이 전적으로 작성·유지. 강의의 "사실 저장소".
course/     ③ 강의 산출물    — 위키를 근거로 만든 아웃라인·슬라이드·대본·유튜브 메타.
templates/  ④ 페이지 템플릿  — 새 파일은 반드시 여기서 복사해 시작한다.
CLAUDE.md   스키마           — 이 파일. 사용자와 함께 계속 개선한다.
```

흐름은 항상 한 방향이다: **raw → wiki → course**.
강의에 들어가는 모든 사실 주장은 wiki 페이지에 근거가 있어야 하고, wiki의 주장은 raw 소스에 근거가 있어야 한다.

### 디렉터리 상세

```
raw/
  YYYY-MM-DD-<slug>.md          웹 클리핑, 논문 요약, 메모, 녹취록 등
  assets/                       이미지·PDF·데이터 파일

wiki/
  index.md                      전체 카탈로그 (카테고리별, 링크 + 한 줄 요약)
  log.md                        append-only 작업 기록
  overview.md                   위키 전체 조망 & 커리큘럼과의 연결 지도
  sources/                      raw 소스 1개당 요약 페이지 1개
  concepts/                     개념 (예: rag, agent, prompt-engineering, mcp, fine-tuning)
  tools/                        제품·도구·모델 (예: claude-code, chatgpt, notebooklm, n8n)
  practices/                    활용법·워크플로·사례 (예: 회의록-자동화, 사내-챗봇-도입)
  syntheses/                    비교표·분석·질의응답 결과 (쿼리 결과를 되돌려 저장)

course/
  curriculum.md                 레벨·레슨 목록·진행 상태 (코스의 index)
  L1-daily/                     레벨별 폴더
    L1-01-<slug>/
      outline.md                학습목표, 흐름, 근거 위키 링크
      script.md                 촬영용 대본 — 내용의 원본, [S] 블록 = 슬라이드 1장 (사용자가 Gemini로 슬라이드 제작)
      youtube.md                제목·설명·챕터·태그·썸네일 문구
      assets/                   이 레슨 전용 이미지·다이어그램

templates/                      source.md, wiki-page.md, outline.md, script.md, youtube.md
```

---

## 2. 커리큘럼 레벨

| 레벨 | 폴더 | 대상 | 핵심 질문 |
|---|---|---|---|
| L1 | `course/L1-daily/` | 누구나 | AI 챗봇을 일상에서 어떻게 잘 쓰나? |
| L2 | `course/L2-work/` | 직장인·비개발자 | 문서·데이터·회의·반복업무를 AI로 어떻게 줄이나? |
| L3 | `course/L3-developer/` | 개발자 | 코딩 에이전트와 API로 개발 방식이 어떻게 바뀌나? |
| L4 | `course/L4-ai-app/` | AI 앱 개발자 | RAG·에이전트·MCP·평가로 제품을 어떻게 만드나? |
| L5 | `course/L5-enterprise/` | 아키텍트·리더 | 보안·거버넌스·비용·운영까지 갖춘 플랫폼을 어떻게 만드나? |

- 레슨 ID: `L<레벨>-<2자리 순번>` (예: `L2-03`). 한 번 부여하면 바꾸지 않는다.
- 각 레슨은 **영상 1편 = 10~20분 = 슬라이드 15~30장**을 기본으로 한다.
- 레벨이 올라가도 앞 레벨 개념을 재사용한다. 선행 레슨은 outline.md의 `prerequisites`에 명시.
- 레벨별 폴더는 첫 레슨을 만들 때 생성한다. 레슨 목록·상태의 단일 진실은 `course/curriculum.md`.

---

## 3. 작성 규칙

### 공통
- **언어**: 본문은 한국어. 제품명·고유 기술 용어는 영어 원어 유지 (첫 등장 시 `검색 증강 생성(RAG)`처럼 병기).
- **파일명**: 소문자 kebab-case. 한글 파일명 금지 (위키 페이지 `title`은 한글 가능).
- **링크**: 위키 내부는 Obsidian 위키링크 `[[concepts/rag]]` 사용. course → wiki 참조도 위키링크.
- 모든 wiki·course 파일은 YAML frontmatter를 가진다 (템플릿 참고).

### AI 분야 특수 규칙 — 시점과 검증
AI는 몇 달 단위로 바뀐다. 오래된 정보가 영상에 박히는 것이 가장 큰 리스크다.
- 제품 기능·가격·모델명·벤치마크 같은 **휘발성 사실**에는 `(as of YYYY-MM)`를 붙인다.
- wiki 페이지 frontmatter의 `updated`와 `volatility: high|medium|low`를 관리한다.
- 확인되지 않은 주장은 `> [!unverified]` 콜아웃으로 표시. 강의 슬라이드에는 넣지 않는다.
- 소스 간 모순은 지우지 말고 `> [!conflict]` 콜아웃으로 양쪽 출처와 함께 기록한다.
- 너의 사전 지식만으로 사실을 위키에 쓰지 않는다. 필요하면 웹 검색 → raw에 저장 → ingest 순서로.

### wiki 페이지
- 한 페이지 = 한 개념/도구/실천법. 길어지면 쪼갠다.
- 맨 위에 2~3문장 요약 → 본문 → `## 관련` (위키링크) → `## 출처` (sources 링크).
- `levels:` frontmatter에 이 지식이 쓰이는 강의 레벨을 적는다 (예: `[L2, L4]`).

### 원본 우선순위 — 대본이 먼저다
**`script.md` → 슬라이드(사용자가 Gemini로 제작)** 순서로 만들어진다. 앞의 것이 원본이다.
- 내용(무슨 말을 하는가)의 원본은 `script.md`. 슬라이드는 대본을 시각적으로 요약한 것이다.
- 슬라이드 작업 중 대본을 바꿔야 할 곳이 보이면 `script.md`를 먼저 고친 뒤 슬라이드에 반영한다.

### 대본 (`script.md`)
- 대본을 쓰면서 화면 전환 지점마다 `## [S03] 핵심 메시지` 헤더를 넣는다. 이 블록 1개 = 슬라이드 1장.
  번호는 S01부터 연속으로 매기고, 슬라이드 단계 이후 블록을 추가·삭제하면 번호를 다시 매긴다.
- 말하는 구어체, 한 문장 짧게. 1분 ≈ 300자 기준으로 레슨 길이를 맞춘다.
- `[화면: ...]`, `[데모: ...]`, `[강조]` 같은 촬영 지시는 대괄호로.
- 첫 30초에 "이 영상을 보면 ○○를 할 수 있다"는 훅을 넣는다.
- 한 `[S]` 블록이 1분(300자)을 넘으면 슬라이드를 나눌지 검토한다.

### 슬라이드 (사용자가 Gemini로 제작)
- 슬라이드는 사용자가 `script.md`를 Gemini에 넣어 직접 만든다. Claude는 슬라이드 파일을 만들지 않는다.
- 그래서 대본의 `[S]` 헤더가 곧 슬라이드 설계다: 블록 1개 = 슬라이드 1장, 헤더 = 문장형 결론 제목 ("RAG는 매번 처음부터 찾는다").
- 슬라이드에도 대본에 없는 내용을 새로 넣지 않는다.

---

## 4. 워크플로

모든 작업이 끝나면 `wiki/log.md`에 한 줄 블록을 추가한다:
`## [YYYY-MM-DD] <작업종류> | <대상>` (작업종류: ingest, query, lint, outline, script, slides, final, publish)

### Ingest — 새 소스 처리
1. `raw/`의 소스를 읽는다 (이미지는 텍스트를 먼저 읽고 별도로 본다).
2. 핵심 내용을 사용자와 짧게 논의한다 (무엇을 강조할지, 어느 레벨에 쓸지).
3. `wiki/sources/<slug>.md` 요약 페이지 작성.
4. 관련 concepts/tools/practices 페이지를 생성·갱신 (모순·시점 규칙 준수). 보통 5~15개 페이지가 바뀐다.
5. `wiki/index.md`와 필요시 `wiki/overview.md` 갱신.
6. 이 소스로 새로 가능해진/보강되는 레슨이 있으면 `course/curriculum.md`에 메모.
7. log 기록.

### Query — 위키에 질문
1. `wiki/index.md`를 먼저 읽고 관련 페이지로 들어간다.
2. 출처 링크와 함께 답한다.
3. 재사용 가치가 있는 답(비교표, 분석)은 `wiki/syntheses/`에 저장하고 index 갱신.

### Lint — 위키 건강 점검
모순, `updated`가 6개월 넘은 `volatility: high` 페이지, 고아 페이지(인바운드 링크 없음),
페이지가 없는 언급된 개념, 근거 없는 주장, 출처 없는 슬라이드 주장을 찾아 보고하고 고칠 목록을 제안한다.

### 레슨 제작 파이프라인
각 단계 끝에 사용자 리뷰를 받는다. 승인 전에 다음 단계로 넘어가지 않는다.

```
outline → script → slides(사용자, Gemini) → final(리허설) → 촬영(사용자) → youtube
```

1. **outline** — `templates/outline.md` 복사. 학습목표 3개 이내, 섹션 흐름, 각 섹션의 근거 wiki 링크.
   가볍게 유지한다 (구조와 출처 확인이 목적). 근거가 부족하면 "필요한 소스" 목록을 사용자에게 먼저 제시한다.
2. **script** — outline을 따라 대본 작성. 화면 전환 지점에 `[S]` 헤더를 넣는다.
   예상 러닝타임(`est_minutes`)과 글자 수(`chars`)를 frontmatter에 기록.
3. **slides** — 사용자가 Gemini로 슬라이드를 만들어 Google Drive에 둔다 (5절 참고). 덱 링크를 outline.md의 `slides_url`에 기록.
4. **final** — 촬영 직전 대본 최종 수정. 완성된 슬라이드를 넘기며 소리 내어 읽는다는 가정으로
   어색한 문장, 화면과 안 맞는 설명, 길이 초과를 고친다. 바뀐 내용이 슬라이드에 영향을 주면 바뀐 `[S]` 번호를 사용자에게 알려 준다.
5. **촬영** — 사용자가 진행. 끝나면 상태를 `recorded`로.
6. **youtube** — 제목 후보 3개, 설명, 챕터 타임스탬프(대본 `[S]` 블록 기준 추정), 태그, 썸네일 문구.
7. `course/curriculum.md` 상태 갱신: `idea → outline → script → slides → final → recorded → published`.

---

## 5. 슬라이드 (Gemini + Google Drive)

- 사용자가 `script.md`를 Gemini에 넣어 슬라이드를 만든다. Claude는 슬라이드 제작·갱신을 하지 않는다.
- 덱은 Google Drive에서 관리한다. git에는 링크만 남긴다 (outline.md의 `slides_url`).
  - 강의 덱 폴더: [강의자료](https://drive.google.com/drive/folders/1rBHCYJ6bFuK7kWjr1mS9dHfqwv5RTI9U) (folder id `1rBHCYJ6bFuK7kWjr1mS9dHfqwv5RTI9U`)
  - 덱 파일명: `[L1-01] <레슨 제목>`
- Claude는 Google Drive 커넥터로 덱을 **읽기만** 한다 (final 단계에서 대본과 슬라이드가 맞는지 확인할 때).
  덱을 만들거나 고치거나 옮기지 않는다.
- 슬라이드가 만들어진 뒤 Claude가 대본을 고치면, 영향을 받는 `[S]` 번호와 바뀐 내용을 답변 끝에 목록으로 알려 준다.
  블록 추가·삭제·순서 변경으로 번호가 바뀌면 그 사실도 알린다.
- 사용자가 슬라이드에서 내용을 바꿨다고 알려 주면 `script.md`에 먼저 반영한다.
- 촬영용 PDF가 필요하면 사용자가 내려받는다.

## 6. 명령어

```bash
# 최근 작업 기록 5개
grep "^## \[" wiki/log.md | tail -5

# 레슨 상태 한눈에
grep -rh "^status:" course/*/*/outline.md | sort | uniq -c
```

내려받은 `.pptx`/`.pdf`는 git에 커밋하지 않는다 (`.gitignore`).

---

## 7. 하지 말 것
- `raw/` 파일 수정·삭제.
- 출처 없는 사실을 wiki나 슬라이드에 쓰기.
- index.md·log.md 갱신 누락.
- 사용자 승인 없이 레슨 파이프라인 단계 건너뛰기.
- 레슨 ID 재사용·변경.
- 슬라이드에서 바꾼 내용을 `script.md`에 반영하지 않기.
- 대본에 없는 내용을 슬라이드에서 새로 만들기, 또는 대본을 고치지 않고 슬라이드만 고치기.
