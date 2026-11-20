import React, { useEffect, useState, useCallback } from 'react';
import { Search, Filter, RefreshCw } from 'lucide-react';
import { useLanguage } from '../context/LanguageContext';
import { getSchemes, getSchemeCategories } from '../services/api';
import SchemeCard from '../components/SchemeCard';
import './SchemesPage.css';

export default function SchemesPage() {
  const { t, lang } = useLanguage();
  const [schemes, setSchemes] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [governmentType, setGovernmentType] = useState('');

  const fetchCategories = useCallback(async () => {
    try {
      const res = await getSchemeCategories();
      setCategories(res.data);
    } catch (e) { console.error(e); }
  }, []);

  const fetchSchemes = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const params = { lang };
      if (searchQuery) params.q = searchQuery;
      if (selectedCategory && selectedCategory !== 'all') params.category = selectedCategory;
      if (governmentType) params.state_or_central = governmentType;
      const res = await getSchemes(params);
      setSchemes(res.data.schemes || []);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  }, [lang, searchQuery, selectedCategory, governmentType]);

  useEffect(() => { fetchCategories(); }, [fetchCategories]);
  useEffect(() => { fetchSchemes(); }, [fetchSchemes]);

  const handleSearch = (e) => {
    e.preventDefault();
    fetchSchemes();
  };

  return (
    <div className="schemes-page container">
      <div className="page-header">
        <h1>{t('schemesTitle')}</h1>
        <p>{t('schemesDesc')}</p>
      </div>

      {/* Search & Filters */}
      <form className="search-bar" onSubmit={handleSearch}>
        <div className="search-input-wrap">
          <Search size={18} className="search-icon" />
          <input
            type="text"
            placeholder={lang === 'te' ? 'పథకం పేరు వెతకండి...' : 'Search scheme name...'}
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
            className="search-input"
          />
        </div>
        <button type="submit" className="btn btn-primary">{t('search').replace('...', '')}</button>
      </form>

      <div className="filters-row">
        <div className="filter-group">
          <Filter size={16} />
          <span>{t('category')}:</span>
          <div className="filter-pills">
            {categories.map(cat => (
              <button
                key={cat.id}
                className={`filter-pill ${selectedCategory === cat.id ? 'active' : ''}`}
                onClick={() => setSelectedCategory(cat.id)}
              >
                {lang === 'te' ? cat.name_te : cat.name_en}
              </button>
            ))}
          </div>
        </div>
        <select
          className="gov-filter"
          value={governmentType}
          onChange={e => setGovernmentType(e.target.value)}
        >
          <option value="">{lang === 'te' ? 'అన్ని ప్రభుత్వాలు' : 'All Governments'}</option>
          <option value="Central Government">{lang === 'te' ? 'కేంద్ర ప్రభుత్వం' : 'Central Government'}</option>
          <option value="State Government">{lang === 'te' ? 'రాష్ట్ర ప్రభుత్వం' : 'State Government'}</option>
        </select>
      </div>

      {/* Results */}
      {loading ? (
        <div className="page-loading"><div className="spinner" /><p>{t('loading')}</p></div>
      ) : error ? (
        <div className="error-banner">
          <span>{t('error')}: {error}</span>
          <button className="btn btn-sm btn-secondary" onClick={fetchSchemes}>
            <RefreshCw size={14} /> {t('retry')}
          </button>
        </div>
      ) : schemes.length === 0 ? (
        <div className="no-results">
          <Search size={48} />
          <p>{t('noResults')}</p>
        </div>
      ) : (
        <>
          <p className="result-count">
            {lang === 'te' ? `${schemes.length} పథకాలు కనుగొనబడ్డాయి` : `${schemes.length} schemes found`}
          </p>
          <div className="schemes-list-grid">
            {schemes.map(scheme => (
              <SchemeCard key={scheme.id} scheme={scheme} lang={lang} />
            ))}
          </div>
        </>
      )}
    </div>
  );
}
