# Task 2 완료 — 학습 노트 + Q&A

## 무엇을 했는가

Task 1에서 직접 경험한 useState 동작을 바탕으로 학습 노트를 작성하고, Q&A 핑퐁으로 보충했다.

## Q&A 요약

- **새로고침하면 값이 남아야 하는 거 아님?** — useState가 값을 유지하는 범위는 리렌더까지다. 새로고침은 앱 재시작이라 초기화된다. 지속이 필요하면 localStorage 등 브라우저 저장소를 써야 한다.
- **setSearchQuery를 onChange에 그냥 넘길 수 있는 이유?** — setSearchQuery는 `(value: string) => void` 시그니처를 가진 함수일 뿐이다. JavaScript의 일급 함수 개념이 적용된 것으로, Java의 메서드 참조(`this::setState`)와 같은 구조다.

## 결과

- `problems/frontend-development/outcome/03-react-usestate.md` 작성

## 다음 행동

Story 3 진입 전 story3/tasks.md 작성 (별도 사이클)
