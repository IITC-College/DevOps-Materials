export function Spinner({ small = false }) {
  return <span className={`spinner ${small ? 'spinner-small' : ''}`} aria-hidden="true" />
}

export default function Loading({ label = 'Loading', cards = 0 }) {
  if (cards) {
    return (
      <div className="product-grid loading-grid" role="status" aria-label={label}>
        {Array.from({ length: cards }, (_, index) => (
          <div className="skeleton-card" key={index}>
            <div className="skeleton skeleton-image" />
            <div className="skeleton skeleton-line short" />
            <div className="skeleton skeleton-line" />
            <div className="skeleton skeleton-line price" />
          </div>
        ))}
      </div>
    )
  }

  return (
    <div className="loading-state" role="status">
      <Spinner />
      <span>{label}</span>
    </div>
  )
}
