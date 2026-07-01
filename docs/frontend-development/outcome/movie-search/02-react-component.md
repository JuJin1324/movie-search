# 함수 컴포넌트 · JSX · Props

## 함수 컴포넌트

React에서 UI를 만드는 기본 단위는 **함수**다. HTML을 반환하는 함수 하나가 곧 컴포넌트다.

```tsx
function MovieCard({ title, year }: MovieCardProps) {
  return <p>{title} ({year})</p>
}
```

Java/Spring으로 대응하면 — 메서드가 값을 계산해서 반환하듯, 컴포넌트는 props를 받아서 UI를 반환한다. "UI를 만드는 함수"라고 이해하면 가장 가깝다.

## JSX

JSX는 JavaScript 안에 HTML처럼 생긴 문법을 쓸 수 있게 해주는 확장이다. 빌드 시 `React.createElement()` 호출로 변환된다.

```tsx
// JSX
return <div><p>{title}</p></div>

// 변환 후
return React.createElement('div', null,
  React.createElement('p', null, title)
)
```

중괄호 `{}` 안에 JavaScript 표현식을 넣을 수 있다 — `{title}`, `{year + 1}`, `{movies.map(...)}` 모두 가능. Java의 템플릿 엔진(Thymeleaf의 `${}`)과 비슷한 역할이다.

## Props

부모 컴포넌트가 자식에게 데이터를 넘기는 방법이다.

```tsx
// 부모: 값을 넘긴다
<MovieCard title="인터스텔라" year={2014} poster={url} />

// 자식: 구조분해로 받는다
function MovieCard({ title, year, poster }: MovieCardProps) { ... }
```

Java로 대응하면 — Command DTO와 구조가 거의 같다. 호출자(부모)가 데이터를 담아 넘기고, 받는 쪽(자식)은 읽기만 한다. TypeScript의 `type`으로 props 구조를 정의하는 것은 Command DTO 클래스를 정의하는 것과 같은 역할이다.

**단방향**이라는 점이 핵심이다 — 부모 → 자식으로만 흐른다. 자식이 부모의 데이터를 직접 바꿀 수 없고, 바꾸려면 부모가 변경 함수를 prop으로 내려줘야 한다(`onChange`처럼).

**React는 컴포넌트를 호출할 때 항상 단일 객체를 첫 번째 인자로 넘긴다.** JSX 속성들(`title="인터스텔라" year={2014}`)을 하나의 객체로 묶어서 `MovieCard({ title: "인터스텔라", year: 2014 })`처럼 호출하는 것이 React의 고정 방식이다. 두 번째 인자는 존재하지 않는다.

따라서 `function MovieCard(title: string, year: number)`처럼 매개변수를 여러 개로 쪼개면, `title`에는 React가 넘긴 객체 전체(`{ title, year, poster }`)가 들어가고 `year`는 `undefined`가 된다 — React가 인자를 하나만 넘기기 때문이다.

`function MovieCard({ title, year }: MovieCardProps)`의 구조분해는 "파라미터가 여러 개"가 아니라, **단일 객체를 받아서 필요한 키만 꺼내 쓰는 문법**이다.

지금 `App`에서 `<SearchBar value="" onChange={() => {}} />`로 빈 함수를 넘긴 것은 의도적이다. `SearchBar`가 `onChange` prop을 타입으로 요구하므로 일단 채워뒀지만, 실제 동작은 Story 2에서 `useState`로 `searchQuery` 상태를 선언하고 그 변경 함수를 여기에 연결할 때 완성된다.

## 컴포지션

작은 컴포넌트를 조합해 큰 화면을 만드는 방식이다.

```tsx
function App() {
  return (
    <div>
      <SearchBar value="" onChange={() => {}} />
      <MovieList movies={mockMovies} />
    </div>
  )
}
```

`MovieList`가 `MovieCard`를 내부에서 렌더링하고, `App`이 `MovieList`를 조합하는 계층 구조. Java의 객체 합성(composition over inheritance)과 같은 개념이다.

**순환 참조 주의:** 컴포넌트가 다른 컴포넌트를 import해서 렌더링하는 것은 Java 클래스 참조와 같은 구조다. 순환 문제도 두 층위에서 발생할 수 있다.

- **모듈 순환 import** — `A.tsx`가 `B.tsx`를 import하고 `B.tsx`가 다시 `A.tsx`를 import하면 번들러 경고 또는 런타임에 `undefined`가 된다. Java 순환 의존성과 같다.
- **컴포넌트 트리 순환** — 컴포넌트가 자기 자신을 렌더링하면 무한 루프로 스택 오버플로우가 난다. 댓글 트리처럼 재귀 구조가 필요한 경우에는 반드시 종료 조건이 있어야 한다.

React 컴포넌트 트리는 부모 → 자식 단방향으로 설계하는 것이 기본이며, 순환 구조가 생기면 설계가 잘못된 신호로 봐야 한다.

**타입 공유 문제 — 임시 처리:** 현재 `Movie` 타입이 `MovieList.tsx` 안에 선언되어 있고 `export`가 없다. 그래서 `App.tsx`의 `mockMovies`는 타입 선언 없이 객체 리터럴로만 작성되어 있고, TypeScript가 구조를 보고 타입을 추론하는 상태다. 공유 타입 파일(`src/types/movie.ts`)로 옮기는 것은 에픽 #6(API 연동)에서 실제 TMDB API 응답 타입을 정의할 때 같이 처리하는 것이 자연스러운 시점이다.
