import axios from 'axios';

const getBaseUrl = () => {
  const envUrl = import.meta.env.VITE_API_URL;
  if (!envUrl) return '/api';
  const clean = envUrl.replace(/\/+$/, '');
  return clean.endsWith('/api') ? clean : `${clean}/api`;
};

const api = axios.create({
  baseURL: getBaseUrl(),
  timeout: 30000,
  headers: { 'Content-Type': 'application/json' },
});

// Schemes
export const getSchemes = (params = {}) => api.get('/schemes', { params });
export const getSchemeDetail = (id, lang = 'te') => api.get(`/schemes/${id}`, { params: { lang } });
export const getSchemeCategories = () => api.get('/schemes/categories');

// Chat
export const sendChatMessage = (message, session_id, language = 'te') =>
  api.post('/chat', { message, session_id, language });
export const getChatHistory = (session_id) =>
  api.get('/chat/history', { params: { session_id } });
export const clearChatHistory = (session_id) =>
  api.delete('/chat/history', { params: { session_id } });

// Lessons
export const getLessons = (params = {}) => api.get('/lessons', { params });
export const getLessonDetail = (id, lang = 'te') => api.get(`/lessons/${id}`, { params: { lang } });
export const getLessonCategories = () => api.get('/lessons/categories');

// FAQs
export const getFaqs = (params = {}) => api.get('/faqs', { params });

// Eligibility
export const getEligibilityCriteria = (schemeId, lang = 'te') =>
  api.get(`/eligibility/${schemeId}`, { params: { lang } });
export const checkEligibility = (schemeId, answers) =>
  api.post(`/eligibility/${schemeId}/check`, { answers });

// Documents
export const getDocuments = (schemeId, lang = 'te') =>
  api.get(`/documents/${schemeId}`, { params: { lang } });

// Application steps
export const getApplicationSteps = (schemeId, lang = 'te') =>
  api.get(`/application/${schemeId}/steps`, { params: { lang } });

// Health check
export const healthCheck = () => api.get('/health');

export default api;
