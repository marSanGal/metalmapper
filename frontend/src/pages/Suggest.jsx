import { useState } from 'react'
import { useAuth } from '../context/AuthContext'
import { createSuggestion } from '../api/suggestions'
import './Suggest.css'

function Suggest() {
  const { user } = useAuth()
  const [formData, setFormData] = useState({
    name: '',
    address: '',
    city: '',
    state: '',
    zip_code: '',
    description: '',
  })
  const [error, setError] = useState('')
  const [success, setSuccess] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setSuccess('')
    setLoading(true)

    try {
      // TODO: Implement create suggestion API call
      await createSuggestion(formData)
      setSuccess('Suggestion submitted successfully!')
      setFormData({
        name: '',
        address: '',
        city: '',
        state: '',
        zip_code: '',
        description: '',
      })
    } catch (err) {
      setError(err.message || 'Failed to submit suggestion')
    } finally {
      setLoading(false)
    }
  }

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    })
  }

  if (!user) {
    return (
      <div className="suggest-page">
        <p>Please log in to suggest a bar.</p>
      </div>
    )
  }

  return (
    <div className="suggest-page">
      <h1>Suggest a Bar</h1>
      {error && <div className="error-message">{error}</div>}
      {success && <div className="success-message">{success}</div>}
      <form onSubmit={handleSubmit} className="suggest-form">
        <div className="form-group">
          <label htmlFor="name">Bar Name *</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="address">Address</label>
          <input
            type="text"
            id="address"
            name="address"
            value={formData.address}
            onChange={handleChange}
          />
        </div>
        <div className="form-row">
          <div className="form-group">
            <label htmlFor="city">City</label>
            <input
              type="text"
              id="city"
              name="city"
              value={formData.city}
              onChange={handleChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="state">State</label>
            <input
              type="text"
              id="state"
              name="state"
              value={formData.state}
              onChange={handleChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="zip_code">ZIP Code</label>
            <input
              type="text"
              id="zip_code"
              name="zip_code"
              value={formData.zip_code}
              onChange={handleChange}
            />
          </div>
        </div>
        <div className="form-group">
          <label htmlFor="description">Description</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleChange}
            rows="4"
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Submitting...' : 'Submit Suggestion'}
        </button>
      </form>
    </div>
  )
}

export default Suggest

