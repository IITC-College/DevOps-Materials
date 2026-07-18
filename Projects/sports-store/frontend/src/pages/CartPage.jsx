import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { apiFetch } from '../api'

export default function CartPage() {
  const [cart, setCart] = useState({ items: [], subtotal: 0 })
  const [error, setError] = useState('')

  function load() {
    apiFetch('/cart')
      .then(setCart)
      .catch((err) => setError(err.message))
  }

  useEffect(load, [])

  async function updateQuantity(sku, quantity) {
    try {
      const updated = await apiFetch(`/cart/items/${sku}`, {
        method: 'PUT',
        body: JSON.stringify({ quantity }),
      })
      setCart(updated)
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <div>
      <h1>Your Cart</h1>
      {error && <p className="error">{error}</p>}
      {cart.items.length === 0 ? (
        <p>
          Your cart is empty. <Link to="/products">Go shopping</Link>.
        </p>
      ) : (
        <>
          <table className="cart-table">
            <thead>
              <tr>
                <th>Item</th><th>Variant</th><th>Qty</th><th>Price</th><th></th>
              </tr>
            </thead>
            <tbody>
              {cart.items.map((item) => (
                <tr key={item.sku}>
                  <td>{item.name}</td>
                  <td>{item.color} / {item.size}</td>
                  <td>
                    <button onClick={() => updateQuantity(item.sku, item.quantity - 1)}>−</button>
                    {' '}{item.quantity}{' '}
                    <button onClick={() => updateQuantity(item.sku, item.quantity + 1)}>+</button>
                  </td>
                  <td>${(item.unit_price * item.quantity).toFixed(2)}</td>
                  <td>
                    <button className="link-button" onClick={() => updateQuantity(item.sku, 0)}>
                      Remove
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <p className="cart-subtotal">Subtotal: ${cart.subtotal.toFixed(2)}</p>
          <Link to="/checkout" className="button">Checkout</Link>
        </>
      )}
    </div>
  )
}
