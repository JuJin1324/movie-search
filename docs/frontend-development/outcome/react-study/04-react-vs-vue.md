# React vs Vue.js 비교

| 구분 | React | Vue.js |
|------|-------|--------|
| 정체 | 라이브러리 (UI만) | 프레임워크 (틀 제공) |
| 문법 | JSX (JS 안에 HTML) | 템플릿 (HTML 안에 문법) |
| 상태 변경 | 수동 (`setState`) | 자동 감지 (반응형) |
| 자유도 | 높음 (직접 조합) | 적당 (공식 정답 제공) |
| 진영 | Meta + 큰 생태계 | 커뮤니티 |

## 라이브러리 vs 프레임워크

**React**는 UI 렌더링만 책임지고 라우팅·상태관리·폼 처리는 직접 골라 조합한다. 자유롭지만 초반 결정이 많다.
**Vue**는 공식 라우터(Vue Router)·상태관리(Pinia)가 정해져 있어 "정답이 있는" 느낌이라 빠르게 시작하기 쉽다.

## 코드 작성 방식

```tsx
// React — JSX (JavaScript 중심)
function Counter() {
  const [count, setCount] = useState(0)
  return <button onClick={() => setCount(count + 1)}>{count}</button>
}
```

```vue
<!-- Vue — 템플릿 (HTML 중심) -->
<template>
  <button @click="count++">{{ count }}</button>
</template>
<script setup>
import { ref } from 'vue'
const count = ref(0)
</script>
```

React는 JS 안에 HTML이 들어오고, Vue는 HTML/JS/CSS가 한 파일에 영역별로 나뉜다.

## 상태 관리 철학 — 가장 큰 차이

- **React**: 상태가 바뀌면 개발자가 `setCount`로 명시적으로 알려야 하고, 컴포넌트 함수를 통째로 재실행한다. ("수동·명시적")
- **Vue**: 데이터를 자동 추적해, 값이 바뀌면 관련 부분만 알아서 다시 그린다. `count++`로 직접 바꿔도 갱신된다. ("자동·반응형")

둘 다 Virtual DOM을 쓰지만([03-virtual-dom-rendering.md](03-virtual-dom-rendering.md)) 변화 감지 방식이 다르다.

## 선택 기준

- **React**: 생태계·일자리·확장성이 가장 큼. 큰 규모, 자유로운 구조. React Native로 앱까지.
- **Vue**: 학습 곡선이 완만하고 생산성이 좋음. 중소 규모, HTML 친숙한 팀.

한 줄 요약: **React = "JS로 다 짠다, 자유롭지만 직접 조립" / Vue = "HTML 템플릿 기반, 정해진 틀로 빠르게"**. 채용·생태계 규모는 React 우세, 입문 편의성은 Vue 강점.
