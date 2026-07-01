# Task 1 완료 — useEffect 동작 확인

## 무엇을 했는가

`App.tsx`에 `useEffect`를 추가해 의존성 배열 세 가지 경우와 클린업 패턴을 브라우저 Console에서 직접 확인했다.

- `useEffect` import 추가
- `[searchQuery]` 의존성 + `setTimeout` + `clearTimeout` 클린업 패턴 적용
- 의존성 배열을 `[]` / `[searchQuery]` / 없음으로 직접 바꿔보며 실행 시점 차이 확인

## 근거·결정 사항

- **최종 코드는 `[searchQuery]` + 클린업**: 세 가지를 모두 코드에 남기지 않고, 실제 동작하는 패턴 하나를 두고 주석으로 비교 형태를 병기. 직접 바꿔보며 확인하는 방식이 학습에 더 효과적.
- **`clearTimeout`**: 예약어가 아니라 브라우저 Web API 전역 함수. `setTimeout`이 반환한 타이머 ID를 받아 예약을 취소한다.

## 결과

- `src/App.tsx` 업데이트
- Console에서 의존성 배열 세 가지 실행 시점 차이 확인
- 클린업 함수(이전 타이머 취소) 동작 확인

## 다음 행동

Task 2 — 학습 노트 완성 + Q&A 핑퐁 (`04-react-useeffect.md` 초안 작성됨)
