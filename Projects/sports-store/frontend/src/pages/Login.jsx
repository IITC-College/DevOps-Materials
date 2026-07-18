import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../auth'

export default function Login() {
  const { login } = useAuth()
  const navigate = useNavigate()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  async function submit(e) {
    e.preventDefault()
    setError('')
    try {
      await login(email, password)
      navigate('/products')
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <form className="form" onSubmit={submit}>
      <h1>Login</h1>
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
      <button className="button" type="submit">Login</button>
      <p>
        New here? <Link to="/register">Create an account</Link>
      </p>
    </form>
  )
}
