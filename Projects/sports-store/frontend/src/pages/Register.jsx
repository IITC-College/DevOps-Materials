import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../auth'
import { Spinner } from '../components/Loading'
import Seo from '../components/Seo'

export default function Register() {
  const { register } = useAuth()
  const navigate = useNavigate()
  const [fullName, setFullName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [submitting, setSubmitting] = useState(false)

  async function submit(e) {
    e.preventDefault()
    setError('')
    setSubmitting(true)
    try {
      await register(email, password, fullName)
      navigate('/products')
    } catch (err) {
      setError(err.message)
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <form className="form" onSubmit={submit}>
      <Seo title="Create an account" description="Create your Stryda Athletics account for faster checkout and order tracking." />
      <span className="eyebrow dark">Join Stryda</span><h1>Create account</h1>
      {error && <p className="error">{error}</p>}
      <label>
        Full name
        <input value={fullName} required
               onChange={(e) => setFullName(e.target.value)} />
      </label>
      <label>
        Email
        <input type="email" value={email} required
               onChange={(e) => setEmail(e.target.value)} />
      </label>
      <label>
        Password (min 8 characters)
        <input type="password" value={password} required minLength={8}
               onChange={(e) => setPassword(e.target.value)} />
      </label>
      <button className="button" type="submit" disabled={submitting}>{submitting ? <><Spinner small /> Creating account…</> : 'Create account'}</button>
      <p>
        Already have an account? <Link to="/login">Login</Link>
      </p>
    </form>
  )
}
