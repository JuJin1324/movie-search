# Task 1 — 실행 기록: Vite + React + TS 초기화 + 보일러플레이트 정리

선행: [tasks.md](tasks.md) §Task 1

## 무엇을 했는가

`movie-search` 레포(README만 있는 초기 상태)에 Vite + React + TypeScript 프로젝트를 초기화하고, `npm run dev`로 브라우저 첫 화면을 확인한 뒤 Vite 전용 보일러플레이트를 걷어냈다.

- `npm create vite@latest . -- --template react-ts` 실행
- `npm install` → `npm run dev` → 브라우저 기본 화면 확인
- 보일러플레이트 정리 (아래 결정 사항 참고)

## 근거·결정 사항

**린터 선택 — ESLint (Oxlint 미선택)**
Vite 초기화 시 Oxlint를 제안받았다. Oxlint는 Rust 기반으로 속도는 빠르지만 ESLint 규칙의 subset만 커버하고 VSCode 확장 생태계가 아직 미성숙하다. 학습 목적이라 업계 표준 흐름을 먼저 익히는 게 맞다고 판단해 ESLint를 선택.

**보일러플레이트 정리 범위**
- `App.tsx` — 카운터·로고·링크 전부 제거, `<h1>Movie Search</h1>` 단일 구조로 교체
- `App.css` — Vite 전용 스타일 전체 제거 (빈 파일 유지, import는 그대로)
- `index.css` — 전역 CSS 변수·타이포그래피 유지, `code, .counter` 묶음 규칙에서 `.counter` 제거
- `src/assets/` — `hero.png`, `react.svg`, `vite.svg` 삭제 (App.tsx에서 참조 없음)

## 결과

- `npm run dev` → 브라우저에 "Movie Search" 제목 화면 표시
- `src/` 아래 Vite 기본 카운터·로고 코드 없음
- 미커밋 상태 (커밋은 사용자 검토 후)

## 다음 행동

- 사용자가 브라우저 확인 → 커밋
- Task 2 진입: ESLint·Prettier + VSCode 프로젝트 설정
