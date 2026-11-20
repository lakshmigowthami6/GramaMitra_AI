import React, { useState } from 'react';
import { Link, NavLink } from 'react-router-dom';
import { Menu, X, Globe, MessageCircle, BookOpen, HelpCircle, Home, ChevronRight } from 'lucide-react';
import { useLanguage } from '../context/LanguageContext';
import './Navbar.css';

export default function Navbar() {
  const { t, toggleLang, lang } = useLanguage();
  const [menuOpen, setMenuOpen] = useState(false);

  const navLinks = [
    { to: '/', label: t('home'), icon: <Home size={18} /> },
    { to: '/schemes', label: t('schemes'), icon: <ChevronRight size={18} /> },
    { to: '/assistant', label: t('assistant'), icon: <MessageCircle size={18} /> },
    { to: '/learning', label: t('learning'), icon: <BookOpen size={18} /> },
    { to: '/faq', label: t('faq'), icon: <HelpCircle size={18} /> },
  ];

  return (
    <header className="navbar">
      <div className="navbar-inner container">
        <Link to="/" className="navbar-brand" onClick={() => setMenuOpen(false)}>
          <div className="brand-icon">గ్రా</div>
          <div className="brand-text">
            <span className="brand-name">{t('appName')}</span>
            <span className="brand-tagline">{t('appTagline')}</span>
          </div>
        </Link>

        <nav className={`navbar-nav ${menuOpen ? 'open' : ''}`} role="navigation">
          {navLinks.map(link => (
            <NavLink
              key={link.to}
              to={link.to}
              end={link.to === '/'}
              className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}
              onClick={() => setMenuOpen(false)}
            >
              {link.icon}
              <span>{link.label}</span>
            </NavLink>
          ))}
        </nav>

        <div className="navbar-actions">
          <button
            className="lang-btn"
            onClick={toggleLang}
            title={lang === 'te' ? 'Switch to English' : 'తెలుగులో చూడండి'}
            aria-label="Toggle language"
          >
            <Globe size={16} />
            <span>{t('changeLang')}</span>
          </button>
          <button
            className="menu-btn"
            onClick={() => setMenuOpen(o => !o)}
            aria-label="Toggle menu"
            aria-expanded={menuOpen}
          >
            {menuOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
      </div>

      {menuOpen && <div className="nav-overlay" onClick={() => setMenuOpen(false)} />}
    </header>
  );
}
