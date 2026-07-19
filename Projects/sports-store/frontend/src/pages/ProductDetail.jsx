import { useEffect, useState } from 'react'
import { Link, useNavigate, useParams } from 'react-router-dom'
import { apiFetch } from '../api'
import { useAuth } from '../auth'
import ProductImage from '../components/ProductImage'
import ProductCard from '../components/ProductCard'
import Loading from '../components/Loading'
import Seo from '../components/Seo'
import { useCart } from '../cart'
import { getProductImage } from '../productImages'

export default function ProductDetail() {
  const { slug } = useParams()
  const { user } = useAuth()
  const navigate = useNavigate()
  const { setCart } = useCart()
  const [product, setProduct] = useState(null)
  const [selectedSku, setSelectedSku] = useState('')
  const [message, setMessage] = useState('')
  const [error, setError] = useState('')
  const [recommendations, setRecommendations] = useState([])
  const [adding, setAdding] = useState(false)

  useEffect(() => {
    apiFetch(`/products/${slug}`)
      .then((data) => {
        setProduct(data)
        return apiFetch(`/products?category=${data.category}&limit=5`)
      })
      .then((items) => setRecommendations(items.filter((item) => item.slug !== slug).slice(0, 4)))
      .catch((err) => setError(err.message))
  }, [slug])

  if (error && !product) return <p className="error">{error}</p>
  if (!product) return <Loading label="Loading product" />

  const variant = product.variants.find((v) => v.sku === selectedSku)

  async function addToCart() {
    if (!user) {
      navigate('/login')
      return
    }
    setMessage('')
    setError('')
    setAdding(true)
    try {
      const updatedCart = await apiFetch('/cart/items', {
        method: 'POST',
        body: JSON.stringify({ sku: selectedSku, quantity: 1 }),
      })
      setCart(updatedCart)
      setMessage('Added to cart.')
    } catch (err) {
      setError(err.message)
    } finally {
      setAdding(false)
    }
  }

  return (
    <>
      <Seo
        title={product.name}
        description={product.description}
        image={getProductImage(product)}
        type="product"
        schema={{
          '@context': 'https://schema.org', '@type': 'Product', name: product.name,
          image: [getProductImage(product)], description: product.description, sku: product.variants[0]?.sku,
          brand: { '@type': 'Brand', name: product.brand || 'Stryda' },
          aggregateRating: { '@type': 'AggregateRating', ratingValue: product.rating || 4.8, reviewCount: product.review_count || 24 },
          offers: { '@type': 'Offer', priceCurrency: 'USD', price: product.base_price, availability: 'https://schema.org/InStock' },
        }}
      />
      <div className="breadcrumbs"><Link to="/">Home</Link><span>/</span><Link to="/products">Shop</Link><span>/</span><span>{product.name}</span></div>
      <div className="product-detail">
      <div className="product-detail-media">
        <ProductImage product={product} className="product-detail-image" eager />
      </div>
      <div className="product-detail-info">
        <p className="product-category">{product.category.replaceAll('-', ' ')} · {product.gender}</p>
        <h1>{product.name}</h1>
        <div className="product-rating detail-rating"><span>★</span> {(product.rating || 4.8).toFixed(1)} <small>({product.review_count || 24} verified reviews)</small></div>
        <p className="product-description">{product.description}</p>
        <ul className="feature-list">
          {(product.features || ['Performance-tested construction', 'Comfort designed for all-day movement', 'Backed by our 30-day return policy']).map((feature) => <li key={feature}>{feature}</li>)}
        </ul>
        <p className="picker-label">Choose color / size</p>
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
        <p className="product-price detail-price">
          ${(variant ? variant.price : product.base_price).toFixed(2)}
        </p>
        <button className="button add-to-cart" disabled={!variant || adding} onClick={addToCart}>
          {adding ? 'Adding…' : variant ? 'Add to cart' : 'Select a size'}
        </button>
        <div className="purchase-notes"><span>🚚 Free delivery over $100</span><span>↩ 30-day easy returns</span><span>🔒 Secure demo checkout</span></div>
        {message && <p className="success">{message}</p>}
        {error && <p className="error">{error}</p>}
      </div>
      </div>
      {recommendations.length > 0 && <section className="recommendations"><div className="section-heading"><div><span className="eyebrow dark">Keep exploring</span><h2>You may also like</h2></div></div><div className="product-grid">{recommendations.map((item) => <ProductCard key={item.slug} product={item} />)}</div></section>}
    </>
  )
}
