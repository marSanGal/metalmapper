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

export const getAllBars = async () => {
  const response = await api.get('/bars')
  return response.data
}

export const getBar = async (barId) => {
  const response = await api.get(`/bars/${barId}`)
  return response.data
}

export const getBarCheckins = async (barId) => {
  const response = await api.get(`/bars/${barId}/checkins`)
  return response.data
}

export const createCheckin = async (barId, checkinData) => {
  const response = await api.post(`/bars/${barId}/checkins`, checkinData)
  return response.data
}

export const getBarRatings = async (barId) => {
  const response = await api.get(`/bars/${barId}/ratings`)
  return response.data
}

export const createRating = async (barId, ratingData) => {
  const response = await api.post(`/bars/${barId}/ratings`, ratingData)
  return response.data
}

