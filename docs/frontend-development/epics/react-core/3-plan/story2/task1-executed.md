# Task 1 완료 — useState 연결

## 무엇을 했는가

`App.tsx`에 `searchQuery` 상태를 선언하고 `SearchBar`의 `value`·`onChange`에 연결했다.

- `useState('')` import 추가
- `const [searchQuery, setSearchQuery] = useState('')` 선언
- `<SearchBar value={searchQuery} onChange={setSearchQuery} />`로 교체

## 근거·결정 사항

- **상태 위치**: `App`에 선언. `SearchBar`가 검색어를 소유하지 않고 부모에서 받는 구조 — Story 1에서 `onChange: (value: string) => void`로 props를 설계한 것이 이 결정을 자연스럽게 만들었다.
- **`onChange` 인자**: `setSearchQuery`를 그대로 전달. `SearchBar`의 `onChange` 타입이 `(value: string) => void`이고 `setSearchQuery`가 그 시그니처와 일치해 래핑 불필요.

## 결과

- `src/App.tsx` 업데이트
- 브라우저에서 검색창 입력 시 화면 갱신 확인
- React DevTools에서 `searchQuery` 상태 변경·리렌더 흐름 확인

## 다음 행동

Task 2 — 학습 노트 작성 + Q&A 핑퐁
