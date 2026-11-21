import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { Analytics } from '@vercel/analytics/react';
import Layout from './components/Layout';
import HomePage from './pages/HomePage';
import SchemesPage from './pages/SchemesPage';
import SchemeDetailPage from './pages/SchemeDetailPage';
import ChatPage from './pages/ChatPage';
import LessonsPage from './pages/LessonsPage';
import LessonDetailPage from './pages/LessonDetailPage';
import FaqPage from './pages/FaqPage';

export default function App() {
  return (
    <>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<HomePage />} />
          <Route path="/schemes" element={<SchemesPage />} />
          <Route path="/schemes/:id" element={<SchemeDetailPage />} />
          <Route path="/assistant" element={<ChatPage />} />
          <Route path="/learning" element={<LessonsPage />} />
          <Route path="/learning/:id" element={<LessonDetailPage />} />
          <Route path="/faq" element={<FaqPage />} />
        </Route>
      </Routes>
      <Analytics />
    </>
  );
}
