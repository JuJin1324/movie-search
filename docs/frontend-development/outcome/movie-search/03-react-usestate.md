# 상태 — useState

## 변수로는 왜 안 되나

아래처럼 일반 변수를 쓰면 입력해도 화면이 바뀌지 않는다.

```tsx
function App() {
  let searchQuery = ''

  return (
    <SearchBar
      value={searchQuery}
      onChange={(value) => { searchQuery = value }}
    />
  )
}
```

이유는 두 가지다.

첫째, **React는 변수가 바뀐 것을 모른다.** `searchQuery = value`로 값을 바꿔도 React 입장에서는 아무 신호도 오지 않는다. 화면을 다시 그려야 할 이유가 없다.

둘째, **다음 렌더에서 변수가 초기화된다.** React가 어떤 이유로 `App`을 다시 렌더링하면 함수 전체가 다시 실행되고 `let searchQuery = ''`로 돌아간다. 이전에 입력한 값이 사라진다.

## useState가 하는 일

```tsx
const [searchQuery, setSearchQuery] = useState('')
```

`useState`는 두 가지를 해결한다.

**값을 렌더 사이에 유지한다.** `searchQuery`는 일반 변수가 아니라 React가 관리하는 저장소에 들어간다. 함수가 다시 실행돼도 이전 값이 그대로 남아 있다.

**`setSearchQuery`를 호출하면 React가 리렌더를 예약한다.** 값을 바꾸는 동시에 "이 컴포넌트 다시 그려라"는 신호를 React에게 보낸다. React는 다음 렌더에서 `searchQuery`를 새 값으로 읽어 화면을 갱신한다.

Java/Spring으로 대응하면 — `setSearchQuery`는 setter가 아니라 이벤트 발행에 가깝다. 값을 저장하는 동시에 "상태 변경됨" 이벤트를 발행하고, React(이벤트 리스너)가 리렌더로 응답하는 구조다.

## 리렌더 흐름

```
사용자 입력
  → SearchBar의 onChange 호출
  → setSearchQuery(value)
  → React: "App 상태 바뀜, 리렌더 예약"
  → App 함수 재실행
  → searchQuery = 새 값
  → SearchBar value={searchQuery} 로 다시 렌더링
  → 화면 갱신
```

이 흐름에서 `SearchBar`가 상태를 직접 갖지 않는다는 점이 중요하다. `SearchBar`는 값을 받아서 보여주고(`value`), 입력이 생기면 부모에게 알릴 뿐(`onChange`)이다. 상태는 `App`이 소유한다.

## useState가 값을 유지하는 범위

`useState`가 값을 유지하는 범위는 **React가 컴포넌트를 다시 실행하는 것** 까지다. 새로고침(F5)은 리렌더가 아니라 앱 재시작이라서 다르다.

| 상황 | useState 값 유지? |
|---|---|
| 상태 변경으로 인한 리렌더 | ✅ 유지 |
| 부모 리렌더로 자식도 재실행 | ✅ 유지 |
| 브라우저 새로고침 | ❌ 초기화 |
| 탭 닫고 다시 열기 | ❌ 초기화 |

새로고침은 브라우저가 페이지 전체를 버리고 처음부터 다시 로드하는 것이다. React 앱 자체가 종료됐다 다시 시작되므로 `useState('')`의 초기값부터 다시 시작한다.

새로고침 후에도 값을 남기려면 `localStorage`나 URL 파라미터처럼 브라우저 저장소에 별도로 써야 한다. `useState`만으로는 안 된다.

## setSearchQuery는 함수다

`setSearchQuery`는 특별한 것이 아니라 `(value: string) => void` 시그니처를 가진 함수다. 그래서 같은 시그니처를 요구하는 `onChange` prop에 그대로 넘길 수 있다.

```tsx
// 직접 전달
onChange={setSearchQuery}

// 래핑해서 전달 — 같은 결과
onChange={(value) => setSearchQuery(value)}
```

이것이 가능한 이유는 JavaScript/TypeScript가 함수를 **일급 객체(first-class citizen)** 로 다루기 때문이다. 함수를 변수에 담고, 인자로 넘기고, 반환값으로 돌려줄 수 있다 — 함수형 프로그래밍의 일급 함수 개념이 그대로 적용된 것이다.

Java로 비유하면 `Consumer<String>` 타입 파라미터에 `this::setState` 메서드 참조를 넘기는 구조와 같다. Java 8 이전에는 익명 클래스로 감싸야 했던 것을 람다·메서드 참조로 쓸 수 있게 된 것처럼, React에서도 함수를 직접 prop으로 전달한다.

## 현재 코드

```tsx
function App() {
  const [searchQuery, setSearchQuery] = useState('')

  return (
    <div>
      <h1>Movie Search</h1>
      <SearchBar value={searchQuery} onChange={setSearchQuery} />
      <MovieList movies={mockMovies} />
    </div>
  )
}
```

`onChange={setSearchQuery}`는 래핑 없이 그대로 전달한다. `SearchBar`의 `onChange` 타입이 `(value: string) => void`이고, `setSearchQuery`의 시그니처가 `(value: string) => void`와 일치하기 때문이다.
