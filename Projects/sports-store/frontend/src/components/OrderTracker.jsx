const STEPS = ['Order confirmed', 'Preparing', 'Shipped', 'Delivered']

function progressFor(order) {
  if (order.status === 'payment_failed') return -1
  if (order.status === 'pending') return 0
  const ageMinutes = Math.max(0, (Date.now() - new Date(order.created_at).getTime()) / 60000)
  if (ageMinutes < 2) return 1
  if (ageMinutes < 10) return 2
  return 3
}

export default function OrderTracker({ order }) {
  const progress = progressFor(order)
  if (progress < 0) {
    return <p className="tracking-failed">Tracking unavailable until payment succeeds.</p>
  }

  return (
    <div className="order-tracker" aria-label="Order progress">
      {STEPS.map((step, index) => (
        <div className={`tracking-step ${index <= progress ? 'complete' : ''}`} key={step}>
          <span className="tracking-dot">{index < progress ? '✓' : index + 1}</span>
          <span>{step}</span>
        </div>
      ))}
    </div>
  )
}
