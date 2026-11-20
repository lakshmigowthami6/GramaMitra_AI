import React, { useEffect, useState, useCallback } from 'react';
import { ChevronDown, ChevronUp, Search, HelpCircle } from 'lucide-react';
import { useLanguage } from '../context/LanguageContext';
import { getFaqs } from '../services/api';
import './FaqPage.css';

export default function FaqPage() {
  const { t, lang } = useLanguage();
  const [faqs, setFaqs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [openIdx, setOpenIdx] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');

  const fetchFaqs = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const params = { lang };
      if (searchQuery) params.q = searchQuery;
      if (selectedCategory !== 'all') params.category = selectedCategory;
      const res = await getFaqs(params);
      setFaqs(res.data.faqs || []);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  }, [lang, searchQuery, selectedCategory]);

  useEffect(() => { fetchFaqs(); }, [fetchFaqs]);

  const categories = [...new Set(faqs.map(f => f.category).filter(Boolean))];

  const filteredFaqs = faqs.filter(faq => {
    const q = lang === 'te' ? faq.question_te : faq.question_en;
    const a = lang === 'te' ? faq.answer_te : faq.answer_en;
    if (!searchQuery) return true;
    const lq = searchQuery.toLowerCase();
    return q?.toLowerCase().includes(lq) || a?.toLowerCase().includes(lq);
  });

  return (
    <div className="faq-page container">
      <div className="page-header">
        <h1><HelpCircle size={28} /> {t('faqTitle')}</h1>
        <p>{t('faqDesc')}</p>
      </div>

      <div className="faq-search-row">
        <div className="search-input-wrap" style={{ flex: 1 }}>
          <Search size={18} className="search-icon" />
          <input
            type="text"
            className="search-input"
            placeholder={lang === 'te' ? 'ప్రశ్న వెతకండి...' : 'Search a question...'}
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
          />
        </div>
        <select
          className="gov-filter"
          value={selectedCategory}
          onChange={e => setSelectedCategory(e.target.value)}
        >
          <option value="all">{t('allCategories')}</option>
          {categories.map(c => <option key={c} value={c}>{c}</option>)}
        </select>
      </div>

      {loading ? (
        <div className="page-loading"><div className="spinner" /></div>
      ) : error ? (
        <div className="error-banner">{error}</div>
      ) : filteredFaqs.length === 0 ? (
        <div className="page-loading"><p>{t('noResults')}</p></div>
      ) : (
        <div className="faq-list">
          {filteredFaqs.map((faq, idx) => {
            const question = lang === 'te' ? faq.question_te : faq.question_en;
            const answer = lang === 'te' ? faq.answer_te : faq.answer_en;
            const isOpen = openIdx === idx;
            return (
              <div key={faq.id || idx} className={`faq-item ${isOpen ? 'open' : ''}`}>
                <button className="faq-question" onClick={() => setOpenIdx(isOpen ? null : idx)}>
                  <span>{question}</span>
                  {isOpen ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
                </button>
                {isOpen && (
                  <div className="faq-answer">
                    <p style={{ whiteSpace: 'pre-wrap' }}>{answer}</p>
                    {faq.category && (
                      <span className="badge badge-primary" style={{ marginTop: '0.5rem', display: 'inline-block' }}>
                        {faq.category}
                      </span>
                    )}
                    {faq.official_url && (
                      <a href={faq.official_url} target="_blank" rel="noopener noreferrer" className="faq-link">
                        {lang === 'te' ? 'అధికారిక వెబ్‌సైట్ →' : 'Official website →'}
                      </a>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
