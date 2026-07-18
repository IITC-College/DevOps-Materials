import { useEffect, useState } from 'react'
import { apiFetch } from '../api'

const STATUS_LABELS = {
  paid: 'Paid',
  pending: 'Pending',
  payment_failed: 'Payment failed',
}

export default function Orders() {
  const [orders, setOrders] = useState([])
  const [error, setError] = useState('')

  useEffect(() => {
    apiFetch('/orders')
      .then(setOrders)
      .catch((err) => setError(err.message))
  }, [])

  return (
    <div>
      <h1>Your Orders</h1>
      {error && <p className="error">{error}</p>}
      {orders.length === 0 && !error && <p>No orders yet.</p>}
      {orders.map((order) => (
        <div key={order.order_number} className="order-card">
          <div className="order-header">
            <strong>{order.order_number}</strong>
            <span className={`status status-${order.status}`}>
              {STATUS_LABELS[order.status] || order.status}
            </span>
          </div>
          <ul>
            {order.items.map((item) => (
              <li key={item.sku}>
                {item.name} ({item.color}/{item.size}) × {item.quantity}
              </li>
            ))}
          </ul>
          <p>
            Total: ${order.pricing.total.toFixed(2)}
            {order.pricing.shipping > 0
              ? ` (incl. $${order.pricing.shipping.toFixed(2)} shipping)`
              : ' (free shipping)'}
          </p>
        </div>
      ))}
    </div>
  )
}
