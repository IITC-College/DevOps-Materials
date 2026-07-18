import { useEffect, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import { apiFetch } from '../api'
import ProductCard from '../components/ProductCard'

const CATEGORIES = [
  'running-shoes',
  'basketball-shoes',
  'hoodies',
  'sportswear',
  'accessories',
]
const GENDERS = ['men', 'women', 'unisex']

export default function ProductList() {
  const [params, setParams] = useSearchParams()
  const [products, setProducts] = useState([])
  const [error, setError] = useState('')

  const category = params.get('category') || ''
  const gender = params.get('gender') || ''

  useEffect(() => {
    const query = new URLSearchParams()
    if (category) query.set('category', category)
    if (gender) query.set('gender', gender)
    apiFetch(`/products?${query}`)
      .then((data) => {
        setProducts(data)
        setError('')
      })
      .catch((err) => setError(err.message))
  }, [category, gender])

  function updateFilter(key, value) {
    const next = new URLSearchParams(params)
    if (value) next.set(key, value)
    else next.delete(key)
    setParams(next)
  }

  return (
    <div>
      <h1>Shop</h1>
      <div className="filters">
        <select
          value={category}
          onChange={(e) => updateFilter('category', e.target.value)}
        >
          <option value="">All categories</option>
          {CATEGORIES.map((c) => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>
        <select
          value={gender}
          onChange={(e) => updateFilter('gender', e.target.value)}
        >
          <option value="">Everyone</option>
          {GENDERS.map((g) => (
            <option key={g} value={g}>{g}</option>
          ))}
        </select>
      </div>
      {error && <p className="error">{error}</p>}
      <div className="product-grid">
        {products.map((p) => (
          <ProductCard key={p.slug} product={p} />
        ))}
      </div>
      {!error && products.length === 0 && <p>No products match these filters.</p>}
    </div>
  )
}
