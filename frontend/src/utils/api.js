import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

export const api = axios.create({
  baseURL: API,
  timeout: 30000, // 30 second timeout for cold starts
});

// Global loading state
let loadingCallbacks = [];

export const onLoadingChange = (callback) => {
  loadingCallbacks.push(callback);
  return () => {
    loadingCallbacks = loadingCallbacks.filter(cb => cb !== callback);
  };
};

const notifyLoadingChange = (isLoading) => {
  loadingCallbacks.forEach(callback => callback(isLoading));
};

// Add request interceptor
api.interceptors.request.use(
  (config) => {
    notifyLoadingChange(true);
    return config;
  },
  (error) => {
    notifyLoadingChange(false);
    return Promise.reject(error);
  }
);

// Add response interceptor
api.interceptors.response.use(
  (response) => {
    notifyLoadingChange(false);
    return response;
  },
  (error) => {
    notifyLoadingChange(false);
    return Promise.reject(error);
  }
);

export const setAuthToken = (token) => {
  if (token) {
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    localStorage.setItem('token', token);
  } else {
    delete api.defaults.headers.common['Authorization'];
    localStorage.removeItem('token');
  }
};

export const getStoredAuth = () => {
  const token = localStorage.getItem('token');
  const role = localStorage.getItem('role');
  const identifier = localStorage.getItem('identifier');

  if (token) {
    setAuthToken(token);
  }

  return { token, role, identifier };
};

export const clearAuth = () => {
  localStorage.removeItem('token');
  localStorage.removeItem('role');
  localStorage.removeItem('identifier');
  delete api.defaults.headers.common['Authorization'];
};

export const saveAuth = (token, role, identifier) => {
  localStorage.setItem('token', token);
  localStorage.setItem('role', role);
  localStorage.setItem('identifier', identifier);
  setAuthToken(token);
};