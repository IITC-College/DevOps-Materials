import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react'
import { apiFetch } from './api'
import { useAuth } from './auth'

const EMPTY_CART = { items: [], subtotal: 0 }
const CartContext = createContext(null)

export function CartProvider({ children }) {
  const { user } = useAuth()
  const [cart, setCart] = useState(EMPTY_CART)
  const [loading, setLoading] = useState(false)

  const refreshCart = useCallback(async () => {
    if (!user) {
      setCart(EMPTY_CART)
      return EMPTY_CART
    }
    setLoading(true)
    try {
      const next = await apiFetch('/cart')
      setCart(next)
      return next
    } finally {
      setLoading(false)
    }
  }, [user])

  useEffect(() => {
    refreshCart().catch(() => setCart(EMPTY_CART))
  }, [refreshCart])

  const itemCount = useMemo(
    () => cart.items.reduce((total, item) => total + item.quantity, 0),
    [cart.items],
  )

  return (
    <CartContext.Provider value={{ cart, setCart, refreshCart, itemCount, loading }}>
      {children}
    </CartContext.Provider>
  )
}

export function useCart() {
  return useContext(CartContext)
}
