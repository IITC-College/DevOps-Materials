import { useEffect, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import { apiFetch } from '../api'
import ProductCard from '../components/ProductCard'
import Loading from '../components/Loading'
import Seo from '../components/Seo'

const CATEGORIES = [
  'running-shoes',
  'basketball-shoes',
  'training-shoes',
  'hoodies',
  'sportswear',
  'accessories',
]
const GENDERS = ['men', 'women', 'unisex']

export default function ProductList() {
  const [params, setParams] = useSearchParams()
  const [products, setProducts] = useState([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)

  const category = params.get('category') || ''
  const gender = params.get('gender') || ''
  const search = params.get('q') || ''
  const sort = params.get('sort') || 'featured'

  useEffect(() => {
    const query = new URLSearchParams()
    if (category) query.set('category', category)
    if (gender) query.set('gender', gender)
    if (search) query.set('q', search)
    setLoading(true)
    apiFetch(`/products?${query}`)
      .then((data) => {
        setProducts(data)
        setError('')
      })
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false))
  }, [category, gender, search])

  function updateFilter(key, value) {
    const next = new URLSearchParams(params)
    if (value) next.set(key, value)
    else next.delete(key)
    setParams(next)
  }

  const sortedProducts = [...products].sort((a, b) => {
    if (sort === 'price-low') return a.base_price - b.base_price
    if (sort === 'price-high') return b.base_price - a.base_price
    if (sort === 'rating') return (b.rating || 0) - (a.rating || 0)
    return 0
  })

  return (
    <div>
      <Seo title="Shop performance gear" description="Explore Stryda running shoes, basketball footwear, training apparel and performance accessories." />
      <div className="shop-header">
        <div><span className="eyebrow dark">Performance collection</span><h1>Built for the work</h1></div>
        <p>Technical footwear and apparel designed for training days, race days and everything between.</p>
      </div>
      <div className="filters">
        <label className="search-field">
          <span className="sr-only">Search products</span>
          <input value={search} placeholder="Search products…" onChange={(e) => updateFilter('q', e.target.value)} />
        </label>
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
        <select value={sort} aria-label="Sort products" onChange={(e) => updateFilter('sort', e.target.value)}>
          <option value="featured">Featured</option>
          <option value="rating">Top rated</option>
          <option value="price-low">Price: low to high</option>
          <option value="price-high">Price: high to low</option>
        </select>
      </div>
      {error && <p className="error">{error}</p>}
      {!loading && !error && <p className="results-count">{products.length} products</p>}
      {loading ? <Loading label="Loading products" cards={8} /> : (
        <div className="product-grid">
          {sortedProducts.map((p) => <ProductCard key={p.slug} product={p} />)}
        </div>
      )}
      {!loading && !error && products.length === 0 && <div className="empty-state"><h2>No matches yet</h2><p>Try removing a filter or searching for something broader.</p></div>}
    </div>
  )
}
