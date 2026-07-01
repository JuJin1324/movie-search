# Story 2 — Task 목록

선행: [../stories.md](../stories.md) §Story 2

## 전체 흐름

```mermaid
flowchart LR
    T1["Task 1<br/>Vite 초기화 +<br/>보일러플레이트 정리"]
    T2["Task 2<br/>ESLint·Prettier +<br/>VSCode 프로젝트 설정"]

    T1 --> T2
```

Task 1이 "앱이 브라우저에 뜨는 상태"를 만든다. Task 2가 "개발 도구가 레포에 묶인 상태"를 만든다. 둘 다 movie-search 레포에 커밋되어 Story 2가 닫힌다.

---

## Task 1 — Vite + React + TS 초기화 + 보일러플레이트 정리

### 목표

`movie-search` 레포에 Vite + React + TypeScript 프로젝트를 초기화하고, `npm run dev` 로 브라우저에 첫 화면이 뜨는 것까지 확인한다. 불필요한 보일러플레이트를 걷어내 "영화 검색 앱의 시작점"임이 보이는 최소 상태로 만든다.

### 핵심 작업

- `npm create vite@latest . -- --template react-ts` 실행 (기존 README.md 보존)
- `npm install` → `npm run dev` → 브라우저 확인
- 보일러플레이트 정리: `App.tsx`에서 Vite 기본 카운터 UI 제거, 앱 제목("Movie Search") 표시 수준으로 교체; `App.css` / `index.css` 불필요한 스타일 제거

### 이 Task에서 하지 않을 것

- ESLint·Prettier 설정 변경 (템플릿 기본값 유지, Task 2에서 정비)
- VSCode `.vscode/` 설정 (Task 2)
- 실제 검색 기능 구현

### 완료 기준

- `npm run dev` 실행 시 브라우저에 "Movie Search" 화면이 뜨는 상태
- `src/` 아래 Vite 기본 카운터 UI 코드가 없는 상태
- movie-search 레포에 커밋된 상태

---

## Task 2 — ESLint·Prettier + VSCode 프로젝트 설정

### 목표

`movie-search` 레포에 ESLint·Prettier 설정을 정비하고, VSCode가 React + TypeScript 코드를 올바르게 인식·포매팅할 수 있도록 프로젝트 단위 설정을 추가한다.

### 핵심 작업

- Prettier 설치 및 `.prettierrc` 작성 (Vite 템플릿에 미포함)
- ESLint + Prettier 충돌 방지 — `eslint-config-prettier` 추가 (필요 시)
- `.vscode/extensions.json` — ESLint·Prettier 권장 확장 목록
- `.vscode/settings.json` — 저장 시 자동 포매팅(`editor.formatOnSave: true`), 기본 포매터 Prettier 지정, ESLint 자동 수정

### 이 Task에서 하지 않을 것

- VSCode 전역 설정 변경 (개발 환경 관리 프로젝트 영역)
- TypeScript `tsconfig` 수정
- 린트 규칙 세부 커스터마이징 (기본값 유지)

### 완료 기준

- VSCode에서 `.tsx` 파일 저장 시 Prettier 포매팅이 자동 적용되는 상태
- ESLint 오류가 VSCode Problems 패널에 표시되는 상태
- `.vscode/extensions.json`·`.vscode/settings.json`·`.prettierrc`가 movie-search 레포에 커밋된 상태

---

## 다음 사이클

Task 1·2 완료 후 Story 2가 닫힌다. 다음은 **Story 3 — 학습 노트** (비코딩). Story 3은 plan-tasks 없이 바로 execute-task로 진입한다.
