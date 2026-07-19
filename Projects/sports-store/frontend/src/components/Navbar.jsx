import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../auth'
import { useCart } from '../cart'

export default function Navbar() {
  const { user, logout } = useAuth()
  const { itemCount } = useCart()
  const navigate = useNavigate()

  return (
    <header className="navbar">
      <Link to="/" className="brand">STRYDA</Link>
      <nav>
        <Link to="/products">Shop</Link>
        <Link to="/cart" className="cart-link" aria-label={`Cart with ${itemCount} items`}>
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <path d="M3 4h2l2.1 10.1a2 2 0 0 0 2 1.6h7.8a2 2 0 0 0 2-1.6L20 8H6M10 20a1 1 0 1 1-2 0 1 1 0 0 1 2 0Zm8 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z" />
          </svg>
          <span>Cart</span>
          {itemCount > 0 && <span className="cart-count">{itemCount > 99 ? '99+' : itemCount}</span>}
        </Link>
        {user ? (
          <>
            <Link to="/orders">Orders</Link>
            <span className="nav-user">{user.full_name}</span>
            <button
              className="link-button"
              onClick={() => {
                logout()
                navigate('/')
              }}
            >
              Logout
            </button>
          </>
        ) : (
          <Link to="/login">Login</Link>
        )}
      </nav>
    </header>
  )
}
