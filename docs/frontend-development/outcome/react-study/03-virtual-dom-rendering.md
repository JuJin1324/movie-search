# Virtual DOM과 렌더링 과정

핵심: **실제 DOM을 직접 건드리지 않고, 가벼운 복사본(Virtual DOM)에서 먼저 계산한 뒤 바뀐 부분만 실제 DOM에 반영한다.**

## 왜 Virtual DOM인가

실제 DOM 조작은 느리다. DOM이 바뀔 때마다 브라우저가 레이아웃 계산(reflow)·다시 그리기(repaint)를 하기 때문이다. 그래서 React는 메모리 상의 가벼운 객체로 DOM을 흉내 내고, 변화를 모아 계산한 뒤 실제 DOM은 최소한으로 한 번에 건드린다.

## Virtual DOM의 정체

그냥 **자바스크립트 객체**다. JSX가 이 객체로 변환된다. ([02-react-component.md](../movie-search/02-react-component.md)의 `React.createElement` 변환과 같은 결과물이다.)

```tsx
<h1 className="title">안녕</h1>
// →
{ type: 'h1', props: { className: 'title', children: '안녕' } }
```

화면 요소가 아니라 "화면이 이렇게 생겨야 한다"는 설계도다.

## 렌더링 3단계

```
① Render          ② Reconciliation        ③ Commit
   가상 트리 생성  →  바뀐 부분 계산(diff)  →  실제 DOM 반영
```

- **① Render** — state/props가 바뀌면 컴포넌트 함수를 재실행해 새 Virtual DOM 트리를 만든다. 실제 DOM은 아직 안 건드린다.
- **② Reconciliation(diffing)** — 이전 Virtual DOM과 새 Virtual DOM을 비교해 "무엇이 바뀌었는지"만 찾는다.
- **③ Commit** — 찾은 변경분만 실제 DOM에 적용한다.

[05-react-core-flow.md](../movie-search/05-react-core-flow.md)의 "상태 변화 → 리렌더" 화살표가 바로 이 ①→③ 과정이다.

## diffing 휴리스틱

전체 트리를 1:1로 다 비교하면 느리므로(O(n³)), React는 추정 규칙으로 O(n)까지 줄인다.

- **규칙 1 — 타입이 다르면 통째로 교체.** `<div>` → `<span>`이면 div 트리 전체를 버리고 새로 만든다.
- **규칙 2 — 리스트는 `key`로 식별.** 실무에서 가장 중요하다.

```tsx
// 나쁨: 순서 바뀌면 비효율 + 버그 (엉뚱한 요소 재사용)
{items.map((item, i) => <li key={i}>{item}</li>)}

// 좋음: 고유 id 사용
{items.map(item => <li key={item.id}>{item}</li>)}
```

`key`가 있으면 "이 항목은 위치가 바뀐 것이지 새로 생긴 게 아니다"를 React가 알 수 있다.

## Fiber

React 16부터의 렌더링 엔진. **렌더링 작업을 잘게 쪼개서 중단·재개할 수 있게** 한 구조다.

- 기존: 렌더링을 시작하면 끝까지 멈출 수 없어, 긴 작업 시 화면이 멈춘다.
- Fiber: 작업을 조각내, 급한 일(사용자 입력 등)이 오면 잠시 양보한다.

덕분에 React 18의 동시성 기능(`useTransition`, `Suspense` 등 우선순위 기반 렌더링)이 가능해졌다.

## 정리

```
state/props 변경
  → 컴포넌트 재실행 → 새 Virtual DOM        (Render)
  → 이전 vs 새 Virtual DOM 비교             (Reconciliation/diffing)
  → 바뀐 부분만 실제 DOM 반영               (Commit)
```

한 줄 요약: **가상 트리에서 미리 계산해, 실제 DOM은 꼭 필요한 만큼만 건드린다.** 그래서 우리는 "DOM을 어떻게 바꿀지"를 명령하지 않고 "화면이 어떤 모습이어야 하는지"만 선언하면 된다.
