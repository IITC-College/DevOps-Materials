import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../auth'
import { Spinner } from '../components/Loading'
import Seo from '../components/Seo'

export default function Login() {
  const { login } = useAuth()
  const navigate = useNavigate()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [submitting, setSubmitting] = useState(false)

  async function submit(e) {
    e.preventDefault()
    setError('')
    setSubmitting(true)
    try {
      await login(email, password)
      navigate('/products')
    } catch (err) {
      setError(err.message)
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <form className="form" onSubmit={submit}>
      <Seo title="Sign in" description="Sign in to your Stryda Athletics account to manage your cart and orders." />
      <span className="eyebrow dark">Welcome back</span><h1>Sign in</h1>
      {error && <p className="error">{error}</p>}
      <label>
        Email
        <input type="email" value={email} required
               onChange={(e) => setEmail(e.target.value)} />
      </label>
      <label>
        Password
        <input type="password" value={password} required
               onChange={(e) => setPassword(e.target.value)} />
      </label>
      <button className="button" type="submit" disabled={submitting}>{submitting ? <><Spinner small /> Signing in…</> : 'Sign in'}</button>
      <p>
        New here? <Link to="/register">Create an account</Link>
      </p>
    </form>
  )
}
