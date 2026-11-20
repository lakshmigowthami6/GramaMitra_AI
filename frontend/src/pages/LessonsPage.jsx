import React, { useEffect, useState, useCallback } from 'react';
import { Link } from 'react-router-dom';
import { BookOpen, ChevronRight, Clock, Award } from 'lucide-react';
import { useLanguage } from '../context/LanguageContext';
import { getLessons, getLessonCategories } from '../services/api';
import './LessonsPage.css';

const LEVEL_COLORS = { Beginner: '#34a853', Intermediate: '#f9ab00', Advanced: '#ea4335' };

export default function LessonsPage() {
  const { t, lang } = useLanguage();
  const [lessons, setLessons] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedCat, setSelectedCat] = useState('all');

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const [lessonsRes, catsRes] = await Promise.all([
        getLessons({ lang, ...(selectedCat !== 'all' ? { category: selectedCat } : {}) }),
        getLessonCategories()
      ]);
      setLessons(lessonsRes.data.lessons || []);
      setCategories(catsRes.data || []);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  }, [lang, selectedCat]);

  useEffect(() => { fetchData(); }, [fetchData]);

  return (
    <div className="lessons-page container">
      <div className="page-header">
        <h1><BookOpen size={28} /> {t('lessonsTitle')}</h1>
        <p>{t('lessonsDesc')}</p>
      </div>

      <div className="category-tabs">
        {categories.map(cat => (
          <button
            key={cat.id}
            className={`cat-tab ${selectedCat === cat.id ? 'active' : ''}`}
            onClick={() => setSelectedCat(cat.id)}
          >
            {lang === 'te' ? cat.name_te : cat.name_en}
          </button>
        ))}
      </div>

      {loading ? (
        <div className="page-loading"><div className="spinner" /></div>
      ) : error ? (
        <div className="error-banner">{error}</div>
      ) : lessons.length === 0 ? (
        <div className="page-loading"><p>{t('noResults')}</p></div>
      ) : (
        <div className="lessons-grid">
          {lessons.map((lesson, idx) => {
            const title = lang === 'te' ? lesson.title_te : lesson.title_en;
            const desc = lang === 'te' ? lesson.description_te : lesson.description_en;
            const levelColor = LEVEL_COLORS[lesson.difficulty_level] || '#5f6368';
            return (
              <Link key={lesson.id} to={`/learning/${lesson.id}`} className="lesson-card card">
                <div className="lesson-card-num">{String(idx + 1).padStart(2, '0')}</div>
                <div className="lesson-card-body">
                  <div className="lesson-card-tags">
                    <span className="badge" style={{ background: `${levelColor}18`, color: levelColor }}>
                      {lesson.difficulty_level}
                    </span>
                    <span className="badge badge-primary">{lesson.module_category}</span>
                  </div>
                  <h3 className="lesson-card-title">{title}</h3>
                  <p className="lesson-card-desc">
                    {desc?.substring(0, 110)}{desc?.length > 110 ? '…' : ''}
                  </p>
                  <div className="lesson-card-footer">
                    {lesson.estimated_duration_minutes && (
                      <span className="lesson-meta">
                        <Clock size={13} /> {lesson.estimated_duration_minutes} {lang === 'te' ? 'నిమిషాలు' : 'min'}
                      </span>
                    )}
                    {lesson.has_quiz && (
                      <span className="lesson-meta">
                        <Award size={13} /> {lang === 'te' ? 'క్విజ్ అందుబాటులో ఉంది' : 'Quiz available'}
                      </span>
                    )}
                    <span className="lesson-start">
                      {t('startLesson')} <ChevronRight size={15} />
                    </span>
                  </div>
                </div>
              </Link>
            );
          })}
        </div>
      )}
    </div>
  );
}
