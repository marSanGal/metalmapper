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

export const getSuggestions = async () => {
  const response = await api.get('/suggestions')
  return response.data
}

export const createSuggestion = async (suggestionData) => {
  const response = await api.post('/suggestions', suggestionData)
  return response.data
}

