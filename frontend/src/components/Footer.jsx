import React from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import './Footer.css';

export default function Footer() {
  const { t } = useLanguage();
  return (
    <footer className="footer">
      <div className="container footer-inner">
        <div className="footer-links">
          <Link to="/">{t('home')}</Link>
          <Link to="/schemes">{t('schemes')}</Link>
          <Link to="/assistant">{t('assistant')}</Link>
          <Link to="/learning">{t('learning')}</Link>
          <Link to="/faq">{t('faq')}</Link>
        </div>
        <p className="footer-text">{t('footer')}</p>
        <p className="footer-disclaimer">
          {t('lang') === 'te'
            ? 'ఈ వ్యవస్థ ప్రభుత్వ పథకాల గురించి సాధారణ సమాచారాన్ని అందిస్తుంది. అధికారిక నిర్ణయాల కోసం సంబంధిత ప్రభుత్వ కార్యాలయాన్ని సంప్రదించండి.'
            : 'This system provides general information about government schemes. For official decisions, contact the relevant government office.'}
        </p>
      </div>
    </footer>
  );
}
