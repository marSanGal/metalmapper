import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { getBar } from '../api/bars'
import './BarDetail.css'

function BarDetail() {
  const { id } = useParams()
  const [bar, setBar] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    loadBar()
  }, [id])

  const loadBar = async () => {
    try {
      setLoading(true)
      // TODO: Implement get bar API call
      const data = await getBar(id)
      setBar(data)
    } catch (err) {
      setError(err.message || 'Failed to load bar')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div className="bar-detail-page">Loading bar details...</div>
  }

  if (error) {
    return <div className="bar-detail-page error">Error: {error}</div>
  }

  if (!bar) {
    return <div className="bar-detail-page">Bar not found</div>
  }

  return (
    <div className="bar-detail-page">
      <h1>{bar.name}</h1>
      {bar.address && (
        <p className="bar-address">
          {bar.address}
          {bar.city && `, ${bar.city}`}
          {bar.state && `, ${bar.state}`}
          {bar.zip_code && ` ${bar.zip_code}`}
        </p>
      )}
      {bar.description && <p className="bar-description">{bar.description}</p>}
      {/* TODO: Add checkins and ratings sections */}
    </div>
  )
}

export default BarDetail

