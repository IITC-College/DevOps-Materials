import { useEffect } from 'react'

const SITE_NAME = 'Stryda Athletics'

function setMeta(selector, attributes) {
  let element = document.head.querySelector(selector)
  if (!element) {
    element = document.createElement('meta')
    document.head.appendChild(element)
  }
  Object.entries(attributes).forEach(([key, value]) => element.setAttribute(key, value))
}

export default function Seo({ title, description, image, type = 'website', schema }) {
  useEffect(() => {
    const fullTitle = title ? `${title} | ${SITE_NAME}` : `${SITE_NAME} | Performance sportswear`
    const canonicalUrl = `${window.location.origin}${window.location.pathname}`
    document.title = fullTitle

    setMeta('meta[name="description"]', { name: 'description', content: description })
    setMeta('meta[name="robots"]', { name: 'robots', content: 'index,follow' })
    setMeta('meta[property="og:title"]', { property: 'og:title', content: fullTitle })
    setMeta('meta[property="og:description"]', { property: 'og:description', content: description })
    setMeta('meta[property="og:type"]', { property: 'og:type', content: type })
    setMeta('meta[property="og:url"]', { property: 'og:url', content: canonicalUrl })
    setMeta('meta[name="twitter:card"]', { name: 'twitter:card', content: 'summary_large_image' })
    if (image) {
      setMeta('meta[property="og:image"]', { property: 'og:image', content: image })
      setMeta('meta[name="twitter:image"]', { name: 'twitter:image', content: image })
    }

    let canonical = document.head.querySelector('link[rel="canonical"]')
    if (!canonical) {
      canonical = document.createElement('link')
      canonical.rel = 'canonical'
      document.head.appendChild(canonical)
    }
    canonical.href = canonicalUrl

    const scriptId = 'page-structured-data'
    document.getElementById(scriptId)?.remove()
    if (schema) {
      const script = document.createElement('script')
      script.id = scriptId
      script.type = 'application/ld+json'
      script.textContent = JSON.stringify(schema)
      document.head.appendChild(script)
    }

    return () => document.getElementById(scriptId)?.remove()
  }, [title, description, image, type, schema])

  return null
}
