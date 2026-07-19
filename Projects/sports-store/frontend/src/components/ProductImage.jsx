import { useEffect, useState } from 'react'
import { getFallbackImage, getProductImage } from '../productImages'

export default function ProductImage({ product, className = '', eager = false }) {
  const [src, setSrc] = useState(() => getProductImage(product))

  useEffect(() => {
    setSrc(getProductImage(product))
  }, [product])

  return (
    <img
      className={className}
      src={src}
      alt={`${product.name} by ${product.brand || 'Stryda'}`}
      loading={eager ? 'eager' : 'lazy'}
      decoding="async"
      onError={() => {
        const fallback = getFallbackImage(product.category)
        if (src !== fallback) setSrc(fallback)
      }}
    />
  )
}
