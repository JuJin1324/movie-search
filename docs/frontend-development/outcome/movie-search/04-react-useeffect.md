# 생명주기 — useEffect

## useEffect란

상태 변화에 반응해 부수 작업을 처리하는 훅이다. 렌더링 결과가 화면에 반영된 뒤 실행된다.

```tsx
useEffect(() => {
  // 부수 작업
  return () => {
    // 클린업 — 다음 실행 직전 또는 컴포넌트 사라질 때 실행
  }
}, [의존성])
```

## 의존성 배열 세 가지

의존성 배열은 "이 상태가 바뀔 때만 실행해라"는 실행 조건 필터다.

| 형태 | 실행 시점 |
|---|---|
| `[]` | 최초 마운트 시 1회만. 이후 어떤 상태가 바뀌어도 실행 안 함 |
| `[searchQuery]` | `searchQuery` 변경으로 인한 렌더에만 실행 |
| 없음 | 어떤 상태가 바뀌든 렌더가 발생하면 무조건 실행 |

직접 바꿔보며 Console에서 차이를 확인하는 것이 가장 빠르다.

## 클린업 패턴과 디바운스

`useEffect`에서 함수를 반환하면 React가 다음 effect 실행 직전에 그 함수를 먼저 실행한다. "이전 작업 뒷정리"용이다.

```tsx
useEffect(() => {
  const timer = setTimeout(() => {
    console.log('검색어:', searchQuery)
  }, 500)

  return () => {
    clearTimeout(timer)  // 다음 effect 실행 전에 이전 타이머 취소
  }
}, [searchQuery])
```

"인터" 5글자를 입력하면 useEffect가 5번 실행되고 클린업도 5번 찍힌다. 이건 문제가 아니라 **패턴이 정상 작동하는 증거**다.

흐름을 풀면:
```
'인' 입력 → useEffect 실행 → timer 예약
'ㅣ' 입력 → 클린업(이전 timer 취소) → useEffect 실행 → timer 예약
'ㄴ' 입력 → 클린업(이전 timer 취소) → useEffect 실행 → timer 예약
'ㅌ' 입력 → 클린업(이전 timer 취소) → useEffect 실행 → timer 예약
'ㅓ' 입력 → 클린업(이전 timer 취소) → useEffect 실행 → timer 예약
(500ms 후) → console.log('검색어: 인터') — 딱 1번만
```

useEffect 자체가 여러 번 실행되는 건 React가 설계한 정상 동작이고 가볍다. 문제가 될 수 있는 건 그 안의 작업 — API 호출이나 무거운 계산이 매 입력마다 일어나는 것이다. 클린업 + setTimeout(디바운스)이 바로 그걸 막는다.

- 디바운스 있을 때: 5번 입력 = 1번 실행
- 디바운스 없을 때: 5번 입력 = 5번 실행 → API 연동 시 실제 문제가 되는 지점

`clearTimeout`은 예약어가 아니다. 브라우저(Web API)가 전역 객체(`window`)에 미리 등록해둔 함수다. `setTimeout`이 타이머 ID를 반환하고 `clearTimeout`이 그 ID로 예약을 취소한다. Java의 `ScheduledFuture.cancel()`과 같은 구조다.
