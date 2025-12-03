import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext'
import Header from './components/Header'
import Login from './pages/Login'
import Register from './pages/Register'
import Bars from './pages/Bars'
import BarDetail from './pages/BarDetail'
import Profile from './pages/Profile'
import Suggest from './pages/Suggest'
import Admin from './pages/Admin'
import './App.css'

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="App">
          <Header />
          <main className="main-content">
            <Routes>
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/bars" element={<Bars />} />
              <Route path="/bars/:id" element={<BarDetail />} />
              <Route path="/profile" element={<Profile />} />
              <Route path="/suggest" element={<Suggest />} />
              <Route path="/admin" element={<Admin />} />
              <Route path="/" element={<Navigate to="/bars" replace />} />
            </Routes>
          </main>
        </div>
      </Router>
    </AuthProvider>
  )
}

export default App

