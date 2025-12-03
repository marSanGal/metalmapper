import { useState, useEffect } from 'react'
import { useAuth } from '../context/AuthContext'
import { getAllSuggestions, approveSuggestion, rejectSuggestion } from '../api/admin'
import './Admin.css'

function Admin() {
  const { user } = useAuth()
  const [suggestions, setSuggestions] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    if (user && user.is_admin) {
      loadSuggestions()
    }
  }, [user])

  const loadSuggestions = async () => {
    try {
      setLoading(true)
      // TODO: Implement get all suggestions API call
      const data = await getAllSuggestions()
      setSuggestions(data)
    } catch (err) {
      setError(err.message || 'Failed to load suggestions')
    } finally {
      setLoading(false)
    }
  }

  const handleApprove = async (suggestionId) => {
    try {
      // TODO: Implement approve suggestion API call
      await approveSuggestion(suggestionId)
      loadSuggestions()
    } catch (err) {
      setError(err.message || 'Failed to approve suggestion')
    }
  }

  const handleReject = async (suggestionId) => {
    try {
      // TODO: Implement reject suggestion API call
      await rejectSuggestion(suggestionId)
      loadSuggestions()
    } catch (err) {
      setError(err.message || 'Failed to reject suggestion')
    }
  }

  if (!user || !user.is_admin) {
    return (
      <div className="admin-page">
        <p>Access denied. Admin privileges required.</p>
      </div>
    )
  }

  if (loading) {
    return <div className="admin-page">Loading suggestions...</div>
  }

  return (
    <div className="admin-page">
      <h1>Admin - Bar Suggestions</h1>
      {error && <div className="error-message">{error}</div>}
      {suggestions.length === 0 ? (
        <p>No suggestions to review.</p>
      ) : (
        <div className="suggestions-list">
          {suggestions.map((suggestion) => (
            <div key={suggestion.id} className="suggestion-card">
              <h3>{suggestion.name}</h3>
              {suggestion.address && (
                <p>
                  {suggestion.address}
                  {suggestion.city && `, ${suggestion.city}`}
                  {suggestion.state && `, ${suggestion.state}`}
                  {suggestion.zip_code && ` ${suggestion.zip_code}`}
                </p>
              )}
              {suggestion.description && <p>{suggestion.description}</p>}
              <p className="status">Status: {suggestion.status}</p>
              {suggestion.status === 'pending' && (
                <div className="admin-actions">
                  <button
                    onClick={() => handleApprove(suggestion.id)}
                    className="approve-btn"
                  >
                    Approve
                  </button>
                  <button
                    onClick={() => handleReject(suggestion.id)}
                    className="reject-btn"
                  >
                    Reject
                  </button>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default Admin

