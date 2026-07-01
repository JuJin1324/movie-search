import { useState, useEffect } from 'react'
import SearchBar from './components/SearchBar'
import MovieList from './components/MovieList'

const mockMovies = [
  { id: 1, title: '인터스텔라', year: 2014, poster: 'https://placehold.co/100x150?text=Interstellar' },
  { id: 2, title: '기생충', year: 2019, poster: 'https://placehold.co/100x150?text=Parasite' },
  { id: 3, title: '올드보이', year: 2003, poster: 'https://placehold.co/100x150?text=Oldboy' },
]

function App() {
  const [searchQuery, setSearchQuery] = useState('')

  // 의존성 배열 비교 (직접 바꿔보며 Console 확인):
  // []            → 마운트 시 1회만 실행
  // [searchQuery] → searchQuery가 바뀔 때마다 실행
  // 없음          → 매 렌더마다 실행
  useEffect(() => {
    const timer = setTimeout(() => {
      console.log('검색어:', searchQuery)
    }, 500)

    return () => {
      clearTimeout(timer)
      console.log('클린업 — 이전 타이머 취소')
    }
  }, [searchQuery])

  return (
    <div>
      <h1>Movie Search</h1>
      <SearchBar value={searchQuery} onChange={setSearchQuery} />
      <MovieList movies={mockMovies} />
    </div>
  )
}

export default App
