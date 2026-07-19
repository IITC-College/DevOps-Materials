import { useState } from 'react'
import { Link } from 'react-router-dom'
import { apiFetch } from '../api'
import { useCart } from '../cart'
import ProductImage from '../components/ProductImage'
import Loading from '../components/Loading'
import Seo from '../components/Seo'

export default function CartPage() {
  const { cart, setCart, loading } = useCart()
  const [error, setError] = useState('')
  const [updatingSku, setUpdatingSku] = useState('')

  async function updateQuantity(sku, quantity) {
    try {
      setUpdatingSku(sku)
      const updated = await apiFetch(`/cart/items/${sku}`, {
        method: 'PUT',
        body: JSON.stringify({ quantity }),
      })
      setCart(updated)
    } catch (err) {
      setError(err.message)
    } finally {
      setUpdatingSku('')
    }
  }

  if (loading) return <Loading label="Loading your cart" />

  return (
    <div className="cart-page">
      <Seo title="Your cart" description="Review the performance gear in your Stryda shopping cart." />
      <div className="shop-header"><div><span className="eyebrow dark">Your selection</span><h1>Shopping cart</h1></div><p>{cart.items.length ? `${cart.items.length} unique products, ready when you are.` : 'Your next personal best starts here.'}</p></div>
      {error && <p className="error">{error}</p>}
      {cart.items.length === 0 ? (
        <div className="empty-state"><div className="empty-icon">🛒</div><h2>Your cart is ready for a workout</h2><p>Add footwear, apparel or accessories to get started.</p><Link to="/products" className="button">Explore the collection</Link></div>
      ) : (
        <div className="cart-layout">
          <div className="cart-items">{cart.items.map((item) => <article className="cart-item" key={item.sku}><div className="cart-item-image"><ProductImage product={item} /></div><div className="cart-item-copy"><h2>{item.name}</h2><p>{item.color} / {item.size}</p><button className="link-button remove" disabled={updatingSku === item.sku} onClick={() => updateQuantity(item.sku, 0)}>Remove</button></div><div className="quantity-control"><button aria-label={`Decrease ${item.name} quantity`} disabled={updatingSku === item.sku} onClick={() => updateQuantity(item.sku, item.quantity - 1)}>−</button><span>{item.quantity}</span><button aria-label={`Increase ${item.name} quantity`} disabled={updatingSku === item.sku} onClick={() => updateQuantity(item.sku, item.quantity + 1)}>+</button></div><strong>${(item.unit_price * item.quantity).toFixed(2)}</strong></article>)}</div>
          <aside className="cart-summary"><h2>Order summary</h2><div><span>Subtotal</span><strong>${cart.subtotal.toFixed(2)}</strong></div><div><span>Estimated delivery</span><strong>{cart.subtotal >= 100 ? 'Free' : '$5.00'}</strong></div><div className="summary-total"><span>Total</span><strong>${(cart.subtotal + (cart.subtotal >= 100 ? 0 : 5)).toFixed(2)}</strong></div>{cart.subtotal < 100 && <p className="shipping-progress">Add ${(100 - cart.subtotal).toFixed(2)} more for free delivery.</p>}<Link to="/checkout" className="button checkout-button">Secure checkout →</Link><p className="secure-note">🔒 Secure demo checkout · 30-day returns</p></aside>
        </div>
      )}
    </div>
  )
}
