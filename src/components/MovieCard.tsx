type MovieCardProps = {
  title: string
  year: number
  poster: string
}

function MovieCard({ title, year, poster }: MovieCardProps) {
  return (
    <div>
      <img src={poster} alt={title} width={100} />
      <p>{title} ({year})</p>
    </div>
  )
}

export default MovieCard
