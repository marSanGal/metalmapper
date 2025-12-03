import { useState, useEffect } from 'react'
import { useAuth } from '../context/AuthContext'
import { getCurrentUser } from '../api/auth'
import './Profile.css'

function Profile() {
  const { user } = useAuth()
  const [userData, setUserData] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadUserData()
  }, [])

  const loadUserData = async () => {
    try {
      setLoading(true)
      // TODO: Implement get current user API call
      const data = await getCurrentUser()
      setUserData(data)
    } catch (err) {
      console.error('Failed to load user data:', err)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div className="profile-page">Loading profile...</div>
  }

  return (
    <div className="profile-page">
      <h1>Profile</h1>
      {userData && (
        <div className="profile-info">
          <p><strong>Username:</strong> {userData.username}</p>
          <p><strong>Email:</strong> {userData.email}</p>
          {userData.created_at && (
            <p><strong>Member since:</strong> {new Date(userData.created_at).toLocaleDateString()}</p>
          )}
        </div>
      )}
      {/* TODO: Add user checkins and ratings */}
    </div>
  )
}

export default Profile

