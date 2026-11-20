import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { MessageCircle, BookOpen, Search, Mic, ChevronRight, Award, Users, Star } from 'lucide-react';
import { useLanguage } from '../context/LanguageContext';
import { getSchemes, getLessons } from '../services/api';
import SchemeCard from '../components/SchemeCard';
import './HomePage.css';

const SUGGESTIONS = [
  { te: 'రైతులకు ఏ ప్రభుత్వ పథకాలు ఉన్నాయి?', en: 'What government schemes are available for farmers?' },
  { te: 'పీఎం కిసాన్ పథకానికి నేను అర్హుడినా?', en: 'Am I eligible for PM-KISAN scheme?' },
  { te: 'పెన్షన్ పొందడానికి ఏ పత్రాలు కావాలి?', en: 'What documents are needed for pension?' },
  { te: 'ఆయుష్మాన్ భారత్ పథకం గురించి చెప్పండి', en: 'Tell me about Ayushman Bharat scheme' },
  { te: 'స్మార్ట్‌ఫోన్ ఎలా వాడాలో నేర్పండి', en: 'Teach me how to use a smartphone' },
];

export default function HomePage() {
  const { t, lang } = useLanguage();
  const [featuredSchemes, setFeaturedSchemes] = useState([]);
  const [lessonsCount, setLessonsCount] = useState(0);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    Promise.all([
      getSchemes({ lang, limit: 3 }),
      getLessons({ lang })
    ]).then(([schemesRes, lessonsRes]) => {
      setFeaturedSchemes(schemesRes.data.schemes?.slice(0, 3) || []);
      setLessonsCount(lessonsRes.data.count || 0);
    }).catch(console.error).finally(() => setLoading(false));
  }, [lang]);

  return (
    <div className="home-page">
      {/* Hero */}
      <section className="hero">
        <div className="container hero-inner">
          <div className="hero-text">
            <div className="hero-badge">
              <Star size={14} />
              <span>{lang === 'te' ? 'కొనంకి గ్రామం కోసం' : 'For Konanki Village'}</span>
            </div>
            <h1 className="hero-title">{t('welcomeTitle')}</h1>
            <p className="hero-desc">{t('welcomeDesc')}</p>
            <div className="hero-buttons">
              <Link to="/assistant" className="btn btn-primary btn-lg">
                <MessageCircle size={20} />
                {t('heroBtn1')}
              </Link>
              <Link to="/schemes" className="btn btn-secondary btn-lg">
                <Search size={20} />
                {t('heroBtn2')}
              </Link>
            </div>
          </div>
          <div className="hero-visual">
            <div className="hero-card">
              <div className="hero-card-header">
                <div className="chat-avatar">AI</div>
                <span>{lang === 'te' ? 'గ్రామమిత్ర సహాయకుడు' : 'GramaMitra Assistant'}</span>
              </div>
              <div className="hero-chat-bubble ai">
                {lang === 'te'
                  ? 'నమస్కారం! నేను మీకు ప్రభుత్వ పథకాలు, అర్హత మరియు పత్రాల గురించి సహాయపడతాను.'
                  : 'Namaskaram! I can help you with government schemes, eligibility and documents.'}
              </div>
              <div className="hero-chat-bubble user">
                {lang === 'te' ? 'పీఎం కిసాన్ కోసం ఎలా దరఖాస్తు చేయాలి?' : 'How to apply for PM-KISAN?'}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Quick Actions */}
      <section className="quick-actions container">
        <div className="actions-grid">
          {[
            { to: '/assistant', icon: <MessageCircle size={28} />, color: '#1a73e8',
              title: lang === 'te' ? 'AI సహాయకుడు' : 'AI Assistant',
              desc: lang === 'te' ? 'ప్రభుత్వ పథకాల గురించి ప్రశ్నలు అడగండి' : 'Ask questions about government schemes' },
            { to: '/schemes', icon: <Search size={28} />, color: '#34a853',
              title: lang === 'te' ? 'పథకాలు వెతకండి' : 'Find Schemes',
              desc: lang === 'te' ? 'మీకు వర్తించే పథకాలు కనుగొనండి' : 'Find schemes that apply to you' },
            { to: '/learning', icon: <BookOpen size={28} />, color: '#f9ab00',
              title: lang === 'te' ? 'డిజిటల్ పాఠాలు' : 'Digital Lessons',
              desc: lang === 'te' ? 'స్మార్ట్‌ఫోన్ & ఇంటర్నెట్ నేర్చుకోండి' : 'Learn smartphone & internet basics' },
            { to: '/faq', icon: <Users size={28} />, color: '#ea4335',
              title: lang === 'te' ? 'సహాయం & FAQ' : 'Help & FAQ',
              desc: lang === 'te' ? 'తరచుగా అడిగే ప్రశ్నలకు సమాధానాలు' : 'Answers to common questions' },
          ].map(action => (
            <Link key={action.to} to={action.to} className="action-card card" style={{ '--color': action.color }}>
              <div className="action-icon" style={{ background: `${action.color}18`, color: action.color }}>
                {action.icon}
              </div>
              <h3 className="action-title">{action.title}</h3>
              <p className="action-desc">{action.desc}</p>
              <ChevronRight className="action-arrow" size={18} />
            </Link>
          ))}
        </div>
      </section>

      {/* AI Suggestions */}
      <section className="suggestions-section container">
        <h2 className="section-title">
          <MessageCircle size={22} />
          {t('suggestedQuestions')}
        </h2>
        <div className="suggestions-list">
          {SUGGESTIONS.map((s, i) => (
            <Link key={i} to={`/assistant?q=${encodeURIComponent(s[lang] || s.en)}`} className="suggestion-pill">
              {s[lang] || s.en}
            </Link>
          ))}
        </div>
      </section>

      {/* Featured Schemes */}
      <section className="featured-schemes container">
        <div className="section-header">
          <h2 className="section-title">
            <Award size={22} />
            {lang === 'te' ? 'ముఖ్యమైన పథకాలు' : 'Featured Schemes'}
          </h2>
          <Link to="/schemes" className="see-all-link">
            {t('seeAll')} →
          </Link>
        </div>
        {loading ? (
          <div className="page-loading"><div className="spinner" /></div>
        ) : (
          <div className="schemes-grid">
            {featuredSchemes.map(scheme => (
              <SchemeCard key={scheme.id} scheme={scheme} lang={lang} />
            ))}
          </div>
        )}
      </section>

      {/* Stats Banner */}
      <section className="stats-banner">
        <div className="container stats-inner">
          {[
            { num: '6+', label: lang === 'te' ? 'ప్రభుత్వ పథకాలు' : 'Govt Schemes' },
            { num: lessonsCount || '5+', label: lang === 'te' ? 'డిజిటల్ పాఠాలు' : 'Digital Lessons' },
            { num: '24/7', label: lang === 'te' ? 'AI సహాయకుడు' : 'AI Assistant' },
            { num: '50+', label: lang === 'te' ? 'కొనంకి నివాసులు' : 'Konanki Residents' },
          ].map(stat => (
            <div key={stat.label} className="stat-item">
              <span className="stat-num">{stat.num}</span>
              <span className="stat-label">{stat.label}</span>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
