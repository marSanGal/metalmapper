import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import './Header.css'

function Header() {
  const { user, logout } = useAuth()
  const navigate = useNavigate()
  const [menuOpen, setMenuOpen] = useState(false)

  const handleLogout = () => {
    logout()
    navigate('/login')
    setMenuOpen(false)
  }

  const toggleMenu = () => {
    setMenuOpen(!menuOpen)
  }

  const closeMenu = () => {
    setMenuOpen(false)
  }

  return (
    <header className="header">
      <div className="header-container">
        <Link to="/bars" className="logo" onClick={closeMenu}>
          MetalMapper
        </Link>
        <button 
          className={`hamburger ${menuOpen ? 'active' : ''}`}
          onClick={toggleMenu}
          aria-label="Toggle menu"
        >
          <span></span>
          <span></span>
          <span></span>
        </button>
        <nav className={`nav ${menuOpen ? 'open' : ''}`}>
          <Link to="/bars" onClick={closeMenu}>Bars</Link>
          {user ? (
            <>
              <Link to="/suggest" onClick={closeMenu}>Suggest</Link>
              <Link to="/profile" onClick={closeMenu}>Profile</Link>
              {user.is_admin && <Link to="/admin" onClick={closeMenu}>Admin</Link>}
              <button onClick={handleLogout} className="logout-btn">
                Logout
              </button>
            </>
          ) : (
            <>
              <Link to="/login" onClick={closeMenu}>Login</Link>
              <Link to="/register" onClick={closeMenu}>Register</Link>
            </>
          )}
        </nav>
        <div className={`menu-overlay ${menuOpen ? 'active' : ''}`} onClick={closeMenu}></div>
      </div>
    </header>
  )
}

export default Header

