import { Link } from 'react-router-dom'
import './BarCard.css'

function BarCard({ bar }) {
  return (
    <div className="bar-card">
      <Link to={`/bars/${bar.id}`} className="bar-card-link">
        <h3>{bar.name}</h3>
        {bar.address && (
          <p className="bar-address">
            {bar.address}
            {bar.city && `, ${bar.city}`}
            {bar.state && `, ${bar.state}`}
          </p>
        )}
        {bar.description && <p className="bar-description">{bar.description}</p>}
      </Link>
    </div>
  )
}

export default BarCard

