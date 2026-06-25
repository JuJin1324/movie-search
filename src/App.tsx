import SearchBar from './components/SearchBar'
import MovieList from './components/MovieList'

const mockMovies = [
  { id: 1, title: '인터스텔라', year: 2014, poster: 'https://placehold.co/100x150?text=Interstellar' },
  { id: 2, title: '기생충', year: 2019, poster: 'https://placehold.co/100x150?text=Parasite' },
  { id: 3, title: '올드보이', year: 2003, poster: 'https://placehold.co/100x150?text=Oldboy' },
]

function App() {
  return (
    <div>
      <h1>Movie Search</h1>
      <SearchBar value="" onChange={() => {}} />
      <MovieList movies={mockMovies} />
    </div>
  )
}

export default App
