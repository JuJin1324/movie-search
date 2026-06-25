import MovieCard from './MovieCard'

type Movie = {
  id: number
  title: string
  year: number
  poster: string
}

type MovieListProps = {
  movies: Movie[]
}

function MovieList({ movies }: MovieListProps) {
  return (
    <div>
      {movies.map((movie) => (
        <MovieCard
          key={movie.id}
          title={movie.title}
          year={movie.year}
          poster={movie.poster}
        />
      ))}
    </div>
  )
}

export default MovieList
