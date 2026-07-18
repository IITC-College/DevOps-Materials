import { Link } from 'react-router-dom'

const CATEGORY_ICONS = {
  'running-shoes': '👟',
  'basketball-shoes': '🏀',
  hoodies: '🧥',
  sportswear: '👕',
  accessories: '🎒',
}

export default function ProductCard({ product }) {
  return (
    <Link to={`/products/${product.slug}`} className="product-card">
      <div className="product-image" aria-hidden="true">
        {CATEGORY_ICONS[product.category] || '🏷️'}
      </div>
      <div className="product-info">
        <h3>{product.name}</h3>
        <p className="product-category">{product.category}</p>
        <p className="product-price">${product.base_price.toFixed(2)}</p>
      </div>
    </Link>
  )
}
