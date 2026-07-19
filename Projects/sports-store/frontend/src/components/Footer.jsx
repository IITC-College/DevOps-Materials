import { Link } from 'react-router-dom'

export default function Footer() {
  return (
    <footer className="site-footer">
      <div className="footer-grid">
        <div><Link to="/" className="brand">STRYDA</Link><p>Performance gear for everyday athletes. A fictional commerce experience built for learning.</p></div>
        <div><strong>Shop</strong><Link to="/products?category=running-shoes">Running</Link><Link to="/products?category=basketball-shoes">Basketball</Link><Link to="/products?category=sportswear">Training apparel</Link></div>
        <div><strong>Help</strong><Link to="/orders">Track an order</Link><span>Delivery & returns</span><span>Size guide</span></div>
        <div><strong>About</strong><span>Our story</span><span>Materials</span><span>Careers</span></div>
      </div>
      <div className="footer-bottom"><span>© 2026 Stryda Athletics</span><span>Demo store · No real payments</span></div>
    </footer>
  )
}
