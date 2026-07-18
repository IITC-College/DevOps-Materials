import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { apiFetch } from '../api'
import ProductCard from '../components/ProductCard'

export default function Home() {
  const [featured, setFeatured] = useState([])

  useEffect(() => {
    apiFetch('/products?limit=4')
      .then(setFeatured)
      .catch(() => setFeatured([]))
  }, [])

  return (
    <div>
      <section className="hero">
        <h1>Move Faster. Go Further.</h1>
        <p>Performance sportswear engineered for every stride.</p>
        <Link to="/products" className="button">Shop the collection</Link>
      </section>
      <h2>Featured</h2>
      <div className="product-grid">
        {featured.map((p) => (
          <ProductCard key={p.slug} product={p} />
        ))}
      </div>
    </div>
  )
}
