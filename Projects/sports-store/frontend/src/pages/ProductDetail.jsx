import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { apiFetch } from '../api'
import { useAuth } from '../auth'

export default function ProductDetail() {
  const { slug } = useParams()
  const { user } = useAuth()
  const navigate = useNavigate()
  const [product, setProduct] = useState(null)
  const [selectedSku, setSelectedSku] = useState('')
  const [message, setMessage] = useState('')
  const [error, setError] = useState('')

  useEffect(() => {
    apiFetch(`/products/${slug}`)
      .then(setProduct)
      .catch((err) => setError(err.message))
  }, [slug])

  if (error) return <p className="error">{error}</p>
  if (!product) return <p>Loading…</p>

  const variant = product.variants.find((v) => v.sku === selectedSku)

  async function addToCart() {
    if (!user) {
      navigate('/login')
      return
    }
    setMessage('')
    setError('')
    try {
      await apiFetch('/cart/items', {
        method: 'POST',
        body: JSON.stringify({ sku: selectedSku, quantity: 1 }),
      })
      setMessage('Added to cart.')
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <div className="product-detail">
      <h1>{product.name}</h1>
      <p className="product-category">{product.category} · {product.gender}</p>
      <p>{product.description}</p>
      <div className="variant-picker">
        {product.variants.map((v) => (
          <button
            key={v.sku}
            className={`variant ${v.sku === selectedSku ? 'selected' : ''}`}
            disabled={v.stock_quantity === 0}
            onClick={() => setSelectedSku(v.sku)}
          >
            {v.color} / {v.size}
            {v.stock_quantity === 0 ? ' (out of stock)' : ''}
          </button>
        ))}
      </div>
      <p className="product-price">
        ${(variant ? variant.price : product.base_price).toFixed(2)}
      </p>
      <button className="button" disabled={!variant} onClick={addToCart}>
        {variant ? 'Add to cart' : 'Select a size'}
      </button>
      {message && <p className="success">{message}</p>}
      {error && <p className="error">{error}</p>}
    </div>
  )
}
