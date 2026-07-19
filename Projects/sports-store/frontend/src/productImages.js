const PRODUCT_IMAGES = {
  'velocity-runner': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=1200&q=85',
  'velocity-runner-w': 'https://images.unsplash.com/photo-1496579538151-212636d0b01c?auto=format&fit=crop&w=1200&q=85',
  'court-master-pro': 'https://images.unsplash.com/photo-1558004282-e2b2587e3e47?auto=format&fit=crop&w=1200&q=85',
  'trailblazer-gtx': 'https://images.unsplash.com/photo-1460353581641-37baddab0fa2?auto=format&fit=crop&w=1200&q=85',
  'sprint-lite': 'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?auto=format&fit=crop&w=1200&q=85',
  'stryda-team-hoodie': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?auto=format&fit=crop&w=1200&q=85',
  'flex-training-tee': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=1200&q=85',
  'aero-running-shorts': 'https://images.unsplash.com/photo-1554139844-af2fc8ad3a3a?auto=format&fit=crop&w=1200&q=85',
  'endurance-crew-socks': 'https://images.unsplash.com/photo-1597843797221-e34b4a320b97?auto=format&fit=crop&w=1200&q=85',
  'pro-gym-duffel': 'https://images.unsplash.com/photo-1708622833152-924c6e364138?auto=format&fit=crop&w=1200&q=85',
  'apex-cross-trainer': 'https://images.unsplash.com/photo-1539185441755-769473a23570?auto=format&fit=crop&w=1200&q=85',
  'cloudstrike-runner': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=1200&q=85',
  'pivot-low': 'https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=1200&q=85',
  'core-zip-hoodie': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?auto=format&fit=crop&w=1200&q=85',
  'motion-support-bra': 'https://images.unsplash.com/photo-1538805060514-97d9cc17730c?auto=format&fit=crop&w=1200&q=85',
  'tempo-7-8-leggings': 'https://images.unsplash.com/photo-1538805060514-97d9cc17730c?auto=format&fit=crop&w=1200&q=85',
  'everyday-recovery-joggers': 'https://images.unsplash.com/photo-1506629082955-511b1aa562c8?auto=format&fit=crop&w=1200&q=85',
  'grip-training-gloves': 'https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?auto=format&fit=crop&w=1200&q=85',
  'steel-flow-bottle': 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?auto=format&fit=crop&w=1200&q=85',
  'restore-foam-roller': 'https://images.unsplash.com/photo-1599058917212-d750089bc07e?auto=format&fit=crop&w=1200&q=85',
}

const CATEGORY_IMAGES = {
  'running-shoes': PRODUCT_IMAGES['velocity-runner'],
  'basketball-shoes': PRODUCT_IMAGES['court-master-pro'],
  'training-shoes': PRODUCT_IMAGES['apex-cross-trainer'],
  hoodies: PRODUCT_IMAGES['stryda-team-hoodie'],
  sportswear: PRODUCT_IMAGES['flex-training-tee'],
  accessories: PRODUCT_IMAGES['pro-gym-duffel'],
}

export const HERO_IMAGE = 'https://images.unsplash.com/photo-1538805060514-97d9cc17730c?auto=format&fit=crop&w=1800&q=85'

export function getProductImage(product) {
  return product.image_url || PRODUCT_IMAGES[product.slug] || CATEGORY_IMAGES[product.category]
}

export function getFallbackImage(category) {
  return CATEGORY_IMAGES[category] || PRODUCT_IMAGES['velocity-runner']
}
