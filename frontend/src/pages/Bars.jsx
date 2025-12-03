import { useState, useEffect } from 'react'
import { getAllBars } from '../api/bars'
import BarCard from '../components/BarCard'
import './Bars.css'

function Bars() {
  const [bars, setBars] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    loadBars()
  }, [])

  const loadBars = async () => {
    try {
      setLoading(true)
      // TODO: Implement get all bars API call
      const data = await getAllBars()
      setBars(data)
    } catch (err) {
      setError(err.message || 'Failed to load bars')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div className="bars-page">Loading bars...</div>
  }

  if (error) {
    return <div className="bars-page error">Error: {error}</div>
  }

  return (
    <div className="bars-page">
      <h1>Metal Bars</h1>
      <div className="bars-grid">
        {bars.length === 0 ? (
          <p>No bars found.</p>
        ) : (
          bars.map((bar) => <BarCard key={bar.id} bar={bar} />)
        )}
      </div>
    </div>
  )
}

export default Bars

