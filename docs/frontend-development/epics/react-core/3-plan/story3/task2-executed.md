# Task 2 완료 — 학습 노트 + Q&A

## 무엇을 했는가

Task 1에서 직접 경험한 useEffect 동작을 바탕으로 학습 노트를 작성하고, Q&A 핑퐁으로 보충했다.

## Q&A 요약

- **useEffect가 5번 호출돼도 성능 문제 없나?** — useEffect 자체가 자주 실행되는 건 가볍다. 문제는 그 안의 작업(API 호출 등)이 5번 일어나는 것이고, 클린업 + 디바운스가 그걸 막는다.
- **clearTimeout은 예약어인가?** — 아니다. 브라우저 Web API가 전역 객체에 등록해둔 함수다.
- **의존성 배열 없음 = 매 렌더마다?** — 더 정확히는 "어떤 상태가 바뀌든 렌더가 발생하면 무조건 실행". 배열은 실행 조건을 거는 필터다.
- **useEffect의 두 번째 인자** — 의존성 배열은 `useEffect`의 두 번째 매개변수. 세 번째 인자는 없다.

## 결과

- `problems/frontend-development/outcome/04-react-useeffect.md` 작성

## 다음 행동

Story 4 — 학습 노트 검토·정리 (비코딩, plan-tasks 없이 바로 execute-task)
