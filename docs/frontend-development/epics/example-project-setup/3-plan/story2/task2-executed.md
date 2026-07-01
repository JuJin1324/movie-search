# Task 2 — 실행 기록: ESLint·Prettier + VSCode 프로젝트 설정

선행: [tasks.md](tasks.md) §Task 2

## 무엇을 했는가

`movie-search` 레포에 Prettier를 추가하고, ESLint와의 충돌을 방지한 뒤, VSCode가 저장 시 자동 포매팅·린트 수정을 수행하도록 프로젝트 단위 설정을 추가했다.

- `prettier`, `eslint-config-prettier` 설치 (`npm install --save-dev prettier eslint-config-prettier`)
- `.prettierrc` 작성
- `eslint.config.js`에 `prettier` 추가 (충돌 방지)
- `.vscode/extensions.json`, `.vscode/settings.json` 작성

## 근거·결정 사항

**Prettier 추가 이유**
Vite 템플릿은 ESLint(코드 품질·버그 패턴 검사)만 포함하고 코드 포매터는 없다. Prettier는 들여쓰기·따옴표·줄 길이 등 스타일을 자동으로 통일해주는 포매터로, 저장 시 자동 적용되면 스타일 논쟁 없이 코드 형태를 일관되게 유지할 수 있다. `eslint-config-prettier`는 ESLint 규칙 중 Prettier와 충돌하는 포매팅 관련 규칙을 끄기 위해 함께 설치.

**Prettier 규칙 — 기본값 위주로 최소화**
`.prettierrc`에 `singleQuote: true`, `semi: false`, `tabWidth: 2`, `trailingComma: es5`, `printWidth: 100`만 지정. Vite 템플릿이 이미 single quote 스타일을 쓰고 있어 일관성을 맞췄다. 세부 규칙 커스터마이징은 이 Task의 범위 밖.

**eslint-config-prettier 위치 — 배열 맨 끝**
ESLint flat config에서 `prettier`는 앞선 규칙들이 켜놓은 포매팅 관련 규칙을 덮어 꺼야 하므로 배열 마지막에 배치.

**extensions.json — 3개 권장 확장**
`esbenp.prettier-vscode`(포매터), `dbaeumer.vscode-eslint`(린터), `ms-vscode.vscode-typescript-next`(TS 언어 지원). 전역 설치와 무관하게 이 레포를 열면 설치 권장 팝업이 뜬다.

**settings.json — `source.fixAll.eslint: "explicit"`**
저장 시 ESLint 자동 수정을 `"always"` 대신 `"explicit"`으로 설정. 저장 시마다 전체 수정이 의도치 않게 실행되는 것을 막고, 명시적 액션(저장)에만 반응하게 한다.

## 결과

- `.prettierrc`, `eslint.config.js`(prettier 추가), `.vscode/extensions.json`, `.vscode/settings.json` 생성·수정
- `package.json` devDependencies에 `prettier`, `eslint-config-prettier` 추가
- 미커밋 상태

## 다음 행동

- 사용자가 VSCode에서 `.tsx` 저장 시 Prettier 자동 포매팅·ESLint Problems 패널 확인
- 확인 후 커밋
