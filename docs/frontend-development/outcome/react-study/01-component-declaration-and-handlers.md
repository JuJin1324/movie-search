# 컴포넌트 선언 방식 · 핸들러

## 함수 선언 방식 두 가지

React 컴포넌트는 두 가지로 선언할 수 있다.

```tsx
// 1) 함수 선언형 (function declaration)
function Configuration() { ... }

// 2) 화살표 함수 (arrow function expression)
const Configuration = () => { ... }
```

## 권장: 컴포넌트는 `function`, 내부 함수는 화살표

**컴포넌트 자체는 `function` 선언형**을 기본으로 둔다.

- **호이스팅** — `function` 선언은 위로 끌어올려져, 정의보다 위에서도 호출할 수 있다. 메인 컴포넌트를 파일 위에 두고 서브 컴포넌트를 아래에 배치하는 식으로 "읽는 순서 = 중요도 순서"가 가능하다. `const Comp = () => {}`는 호이스팅이 안 돼 정의보다 위에서 못 쓴다.
- **디버깅** — named function이라 스택 트레이스에 이름이 그대로 찍힌다.
- **의도** — "재사용 가능한 선언"이라는 신호가 강하다.

React·Next.js 공식 예제도 컴포넌트는 대부분 `function` 선언형이다.

**컴포넌트 내부의 핸들러·콜백·헬퍼는 화살표 함수**로 둔다. `this` 바인딩 이슈가 없고(lexical this) 간결하다.

```tsx
function Configuration() {
  const handleClick = () => { ... }      // 핸들러
  const items = list.map(x => x.name)    // 콜백
  return <button onClick={handleClick} />
}
```

단, `React.memo`·`forwardRef`로 감싸는 컴포넌트는 표현식이라 화살표가 불가피하다.

```tsx
const Configuration = React.memo(() => { ... })
```

| 대상 | 권장 |
|------|------|
| 페이지/일반 컴포넌트 | `function Comp() {}` |
| memo/forwardRef 래핑 | `const Comp = () => {}` (불가피) |
| 핸들러·콜백·헬퍼 | 화살표 함수 |

가장 중요한 건 **팀/프로젝트 내 일관성**이다. 이미 한쪽으로 통일돼 있으면 그 컨벤션을 따른다. ESLint `react/function-component-definition` 룰로 강제할 수 있다.

## 핸들러

핸들러는 **이벤트(사용자 동작 등)가 일어났을 때 실행할 함수**다. 화면 구조(JSX)와 동작 로직을 분리하는 역할을 한다.

```tsx
function Form() {
  const handleSubmit = (e) => {
    e.preventDefault()        // 기본 동작 막기
    // 서버 전송, 상태 변경 등...
  }
  return <form onSubmit={handleSubmit}>...</form>
}
```

로직을 JSX 안에 직접 넣을 수도 있지만, 길어지면 화면 구조와 동작이 뒤섞인다. 그래서 동작은 핸들러로 빼낸다.

**이름 컨벤션:**

| 위치 | 접두사 | 예시 |
|------|--------|------|
| 핸들러 정의 (내가 만드는 함수) | `handle` | `handleClick`, `handleSubmit` |
| props로 전달받는 핸들러 (이벤트 이름) | `on` | `onClick`, `onChange` |

```tsx
// 부모: handleSave를 정의해서 onSave로 넘김
function Page() {
  const handleSave = () => { ... }
  return <SaveButton onSave={handleSave} />
}

// 자식: onSave로 받아서 이벤트에 연결
function SaveButton({ onSave }) {
  return <button onClick={onSave}>저장</button>
}
```

이 구조는 [02-react-component.md](../movie-search/02-react-component.md)의 단방향 props 흐름과 같다 — 부모가 변경 함수를 prop으로 내려줘야 자식이 부모 상태를 바꿀 수 있다.
