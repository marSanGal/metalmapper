import axios from 'axios'

const API_URL = '/api'

// Create axios instance with default config
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export const getAllSuggestions = async () => {
  const response = await api.get('/admin/suggestions')
  return response.data
}

export const approveSuggestion = async (suggestionId) => {
  const response = await api.post(`/admin/suggestions/${suggestionId}/approve`)
  return response.data
}

export const rejectSuggestion = async (suggestionId) => {
  const response = await api.post(`/admin/suggestions/${suggestionId}/reject`)
  return response.data
}

