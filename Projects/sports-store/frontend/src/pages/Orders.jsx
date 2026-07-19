import { useEffect, useState } from 'react'
import { apiFetch } from '../api'
import Loading from '../components/Loading'
import OrderTracker from '../components/OrderTracker'
import Seo from '../components/Seo'

const STATUS_LABELS = {
  paid: 'Paid',
  pending: 'Pending',
  payment_failed: 'Payment failed',
}

export default function Orders() {
  const [orders, setOrders] = useState([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    apiFetch('/orders')
      .then(setOrders)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <Loading label="Loading your orders" />

  return (
    <div className="orders-page">
      <Seo title="Orders and tracking" description="Review and track your Stryda Athletics demo orders." />
      <div className="shop-header"><div><span className="eyebrow dark">Account</span><h1>Orders & tracking</h1></div><p>Follow each fictional order from confirmation to delivery.</p></div>
      {error && <p className="error">{error}</p>}
      {orders.length === 0 && !error && <div className="empty-state"><div className="empty-icon">📦</div><h2>No orders yet</h2><p>Your completed orders and delivery progress will appear here.</p></div>}
      {orders.map((order) => (
        <div key={order.order_number} className="order-card">
          <div className="order-header">
            <strong>{order.order_number}</strong>
            <span className={`status status-${order.status}`}>
              {STATUS_LABELS[order.status] || order.status}
            </span>
          </div>
          <div className="order-meta"><span>Placed {new Date(order.created_at).toLocaleDateString(undefined, { dateStyle: 'medium' })}</span><span>Tracking STRY-{order.order_number.slice(-6)}</span><span>Delivering to {order.shipping_address.city}</span></div>
          <OrderTracker order={order} />
          <div className="order-items">{order.items.map((item) => <div key={item.sku}><span>{item.name} <small>{item.color} / {item.size} × {item.quantity}</small></span><strong>${(item.unit_price * item.quantity).toFixed(2)}</strong></div>)}</div>
          <div className="order-total"><span>{order.pricing.shipping > 0 ? `Includes $${order.pricing.shipping.toFixed(2)} delivery` : 'Free delivery'}</span><strong>Total ${order.pricing.total.toFixed(2)}</strong></div>
        </div>
      ))}
    </div>
  )
}
