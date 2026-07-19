import { Link } from 'react-router-dom'
import ProductImage from './ProductImage'

function displayCategory(category) {
  return category.replaceAll('-', ' ')
}

export default function ProductCard({ product }) {
  const rating = product.rating || 4.8
  const reviews = product.review_count || 24

  return (
    <Link to={`/products/${product.slug}`} className="product-card">
      <div className="product-image-wrap">
        <ProductImage product={product} className="product-image" />
        {product.tags?.includes('new') && <span className="product-badge">New</span>}
      </div>
      <div className="product-info">
        <p className="product-category">{displayCategory(product.category)}</p>
        <h3>{product.name}</h3>
        <div className="product-rating" aria-label={`${rating} out of 5 stars, ${reviews} reviews`}>
          <span aria-hidden="true">★</span> {rating.toFixed(1)} <small>({reviews})</small>
        </div>
        <div className="product-card-bottom">
          <p className="product-price">${product.base_price.toFixed(2)}</p>
          <span className="card-arrow" aria-hidden="true">→</span>
        </div>
      </div>
    </Link>
  )
}
