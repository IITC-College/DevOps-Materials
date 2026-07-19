import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { apiFetch } from '../api'
import { useCart } from '../cart'
import { Spinner } from '../components/Loading'
import Seo from '../components/Seo'

const EMPTY_ADDRESS = {
  full_name: '',
  street: '',
  city: '',
  postal_code: '',
  country: '',
}

export default function Checkout() {
  const navigate = useNavigate()
  const { setCart } = useCart()
  const [address, setAddress] = useState(EMPTY_ADDRESS)
  const [cardNumber, setCardNumber] = useState('')
  const [error, setError] = useState('')
  const [submitting, setSubmitting] = useState(false)

  function setField(key, value) {
    setAddress((prev) => ({ ...prev, [key]: value }))
  }

  async function submit(e) {
    e.preventDefault()
    setError('')
    setSubmitting(true)
    try {
      await apiFetch('/orders/checkout', {
        method: 'POST',
        body: JSON.stringify({
          shipping_address: address,
          card_number: cardNumber,
        }),
      })
      setCart({ items: [], subtotal: 0 })
      navigate('/orders')
    } catch (err) {
      if (err.status === 402) {
        setError('Payment declined. Try a different card.')
      } else {
        setError(err.message)
      }
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <form className="form checkout-form" onSubmit={submit}>
      <Seo title="Checkout" description="Complete your Stryda Athletics demo order securely." />
      <h1>Checkout</h1>
      {error && <p className="error">{error}</p>}
      <label>
        Full name
        <input value={address.full_name} required
               onChange={(e) => setField('full_name', e.target.value)} />
      </label>
      <label>
        Street
        <input value={address.street} required
               onChange={(e) => setField('street', e.target.value)} />
      </label>
      <label>
        City
        <input value={address.city} required
               onChange={(e) => setField('city', e.target.value)} />
      </label>
      <label>
        Postal code
        <input value={address.postal_code} required
               onChange={(e) => setField('postal_code', e.target.value)} />
      </label>
      <label>
        Country
        <input value={address.country} required
               onChange={(e) => setField('country', e.target.value)} />
      </label>
      <label>
        Card number
        <input value={cardNumber} required minLength={12} maxLength={19}
               placeholder="4242424242424242"
               onChange={(e) => setCardNumber(e.target.value)} />
      </label>
      <p className="hint">
        This is a demo store — no real payment happens. A card ending in 0000
        simulates a declined payment.
      </p>
      <button className="button" type="submit" disabled={submitting}>
        {submitting ? <><Spinner small /> Processing order…</> : 'Place order securely'}
      </button>
    </form>
  )
}
