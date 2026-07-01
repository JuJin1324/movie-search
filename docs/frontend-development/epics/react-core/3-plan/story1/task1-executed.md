# Task 1 완료 — 컴포넌트 구현

## 무엇을 했는가

`src/components/` 아래 세 컴포넌트를 생성하고 `App.tsx`에서 컴포지션으로 조합했다.

- `SearchBar.tsx` — `value`·`onChange` props 수신, 검색어 입력 UI
- `MovieCard.tsx` — `title`·`year`·`poster` props 수신, 영화 한 건 카드
- `MovieList.tsx` — `movies` 배열 props 수신, `MovieCard`를 목록으로 렌더링
- `App.tsx` — mock 데이터 3건 + 세 컴포넌트 컴포지션

## 근거·결정 사항

- **컴포넌트 파일 배치**: `src/components/` 단일 폴더. ADR 후보였던 기능 단위 분리는 에픽 #4(커스텀 훅) 이후 재판단.
- **`Movie` 타입**: `MovieList`와 `MovieCard`가 같은 타입을 쓰므로 `MovieList.tsx` 안에 선언. 에픽 #6(API 연동)에서 공유 타입 파일로 옮기는 것이 자연스러운 시점.
- **`SearchBar` onChange**: `(e: React.ChangeEvent) => void` 대신 `(value: string) => void`로 래핑. 부모가 이벤트 객체를 직접 다루지 않아도 되는 구조.
- **poster mock**: `placehold.co` 플레이스홀더 사용. 실제 TMDB API 연동은 에픽 #6 범위.

## 결과

- `src/components/SearchBar.tsx`
- `src/components/MovieCard.tsx`
- `src/components/MovieList.tsx`
- `src/App.tsx` (업데이트)
- 브라우저에서 mock 데이터 3건 렌더링 확인 완료

## 다음 행동

Task 2 — 학습 노트 작성 + Q&A 핑퐁
