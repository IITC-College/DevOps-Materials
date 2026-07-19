import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { apiFetch } from '../api'
import ProductCard from '../components/ProductCard'
import Loading from '../components/Loading'
import Seo from '../components/Seo'
import { HERO_IMAGE } from '../productImages'

export default function Home() {
  const [featured, setFeatured] = useState([])
  const [loading, setLoading] = useState(true)
  const [email, setEmail] = useState('')
  const [subscribed, setSubscribed] = useState(false)

  useEffect(() => {
    apiFetch('/products?limit=8')
      .then(setFeatured)
      .catch(() => setFeatured([]))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div>
      <Seo
        description="Shop Stryda Athletics performance running shoes, training apparel and gym essentials designed for everyday athletes."
        image={HERO_IMAGE}
        schema={{
          '@context': 'https://schema.org',
          '@type': 'WebSite',
          name: 'Stryda Athletics',
          url: window.location.origin,
          potentialAction: {
            '@type': 'SearchAction',
            target: `${window.location.origin}/products?q={search_term_string}`,
            'query-input': 'required name=search_term_string',
          },
        }}
      />
      <section className="hero">
        <img className="hero-image" src={HERO_IMAGE} alt="Runner training outdoors" />
        <div className="hero-shade" />
        <div className="hero-content">
          <span className="eyebrow">Stryda performance / 2026</span>
          <h1>Move faster.<br />Go further.</h1>
          <p>Technical essentials built to keep up with every mile, lift and leap.</p>
          <div className="hero-actions">
            <Link to="/products" className="button">Shop the collection</Link>
            <Link to="/products?category=running-shoes" className="text-link">Explore running →</Link>
          </div>
        </div>
      </section>

      <section className="benefits" aria-label="Store benefits">
        <div><strong>Free delivery</strong><span>On orders over $100</span></div>
        <div><strong>30-day returns</strong><span>Try it. Test it. Love it.</span></div>
        <div><strong>Built to perform</strong><span>Technical gear, tested hard</span></div>
      </section>

      <section className="category-showcase" aria-labelledby="category-title">
        <div className="section-heading">
          <div>
            <span className="eyebrow dark">Find your pace</span>
            <h2 id="category-title">Shop by activity</h2>
          </div>
        </div>
        <div className="category-grid">
          <Link to="/products?category=running-shoes" className="category-tile category-running">
            <span>Road & trail</span><strong>Running</strong><i>→</i>
          </Link>
          <Link to="/products?category=basketball-shoes" className="category-tile category-court">
            <span>Own the floor</span><strong>Basketball</strong><i>→</i>
          </Link>
          <Link to="/products?category=sportswear" className="category-tile category-training">
            <span>Move without limits</span><strong>Training</strong><i>→</i>
          </Link>
        </div>
      </section>

      <div className="section-heading">
        <div>
          <span className="eyebrow dark">Curated for you</span>
          <h2>Featured gear</h2>
        </div>
        <Link to="/products" className="view-all">View all products →</Link>
      </div>
      {loading ? <Loading label="Loading featured products" cards={4} /> : (
        <div className="product-grid">
          {featured.map((p) => <ProductCard key={p.slug} product={p} />)}
        </div>
      )}

      <section className="newsletter">
        <div>
          <span className="eyebrow">The Stryda list</span>
          <h2>Training notes. New drops. No noise.</h2>
          <p>Join our fictional athlete community for product stories and early access.</p>
        </div>
        {subscribed ? <p className="newsletter-success">✓ You're on the list.</p> : (
          <form onSubmit={(event) => { event.preventDefault(); setSubscribed(true) }}>
            <label className="sr-only" htmlFor="newsletter-email">Email address</label>
            <input id="newsletter-email" type="email" value={email} required placeholder="you@example.com" onChange={(event) => setEmail(event.target.value)} />
            <button className="button" type="submit">Join now</button>
          </form>
        )}
      </section>
      <p className="photo-credit">Product and campaign photography from <a href="https://unsplash.com" target="_blank" rel="noreferrer">Unsplash</a>.</p>
    </div>
  )
}
