# Story 3 — 실행 기록: 학습 노트

선행: [../stories.md](../stories.md) §Story 3

## 무엇을 했는가

Story 2에서 구성한 개발 환경(Vite + React + TypeScript + VSCode 설정)을 백엔드 개발자 관점의 대비 구조로 정리한 학습 노트를 작성했다. 실제 파일을 보며 생긴 궁금증(파일 역할·package.json 구조)을 이번 에픽 안에서 함께 정리했다.

- `problems/frontend-development/outcome/vite-react-ts-setup.md` 작성
  - 각 도구의 역할(Vite·React·TypeScript)
  - VSCode 설정(extensions.json·settings.json·ESLint vs Prettier)
  - 프로젝트 파일 구조(main.tsx·App.tsx·index.css·App.css·package.json)

## 근거·결정 사항

**구성: 도구별 역할 → VSCode 설정 → 파일 구조 순서**
Story 3 완료 기준(도구 역할 + VSCode 설정)에 파일 구조 섹션을 추가했다. 파일 역할은 "셋업 결과물이 무엇인지"에 해당해 다음 에픽(React 핵심) 진입 전에 알아야 할 배경지식 수준이므로 이번 에픽 안에서 닫았다.

**백엔드 대비 구조 유지**
- Vite ↔ Gradle/Maven (빌드 도구)
- npm·package.json ↔ 의존성 관리·pom.xml
- TypeScript ↔ Java 타입 시스템
- ESLint·Prettier ↔ Checkstyle·SpotBugs
- main.tsx ↔ Spring Boot Application 클래스 (진입점, 거의 안 건드림 — Provider 추가 시 손댐)

## 결과

- `outcome/vite-react-ts-setup.md` 생성
- 미커밋 상태

## 다음 행동

- 사용자 확인 후 커밋
- Story 3 완료 → 에픽 #1 닫힘, 백로그 완료 이동
