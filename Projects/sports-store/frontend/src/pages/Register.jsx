import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../auth'

export default function Register() {
  const { register } = useAuth()
  const navigate = useNavigate()
  const [fullName, setFullName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  async function submit(e) {
    e.preventDefault()
    setError('')
    try {
      await register(email, password, fullName)
      navigate('/products')
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <form className="form" onSubmit={submit}>
      <h1>Create Account</h1>
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
      <button className="button" type="submit">Register</button>
      <p>
        Already have an account? <Link to="/login">Login</Link>
      </p>
    </form>
  )
}
