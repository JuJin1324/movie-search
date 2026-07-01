# Task 2 완료 — 학습 노트 + Q&A

## 무엇을 했는가

`02-react-component.md` 학습 노트를 작성하고, Q&A 핑퐁으로 내용을 보충했다.

## Q&A에서 보충된 내용

- `onChange={() => {}}` 빈 함수는 의도적 — Story 2에서 useState와 연결될 자리
- Command DTO와 props의 대응 관계 추가
- React가 컴포넌트를 단일 객체로 호출하는 방식 + 구조분해와의 구분 명확화
- `Movie` 타입이 `MovieList.tsx` 안에만 있어 `App.tsx`의 `mockMovies`가 타입 추론 상태 — 에픽 #6에서 공유 타입으로 이동 예정
- 컴포넌트 간 순환 참조 위험 (모듈 순환 import / 컴포넌트 트리 순환) 추가

## 결과

- `problems/frontend-development/outcome/02-react-component.md` 완성

## 다음 행동

Story 1 완료. 커밋 후 Story 2(상태 — useState) 진입 전 plan-tasks.
