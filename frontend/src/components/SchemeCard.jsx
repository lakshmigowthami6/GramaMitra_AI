import React from 'react';
import { Link } from 'react-router-dom';
import { ExternalLink, ChevronRight, Calendar } from 'lucide-react';
import './SchemeCard.css';

const CATEGORY_COLORS = {
  Agriculture: '#34a853',
  'Social Security': '#1a73e8',
  Education: '#f9ab00',
  Healthcare: '#ea4335',
  Housing: '#9c27b0',
  'Women Welfare': '#e91e63',
  default: '#5f6368',
};

export default function SchemeCard({ scheme, lang = 'te' }) {
  const name = lang === 'te' ? scheme.name_te : scheme.name_en;
  const desc = lang === 'te' ? scheme.description_te : scheme.description_en;
  const color = CATEGORY_COLORS[scheme.category] || CATEGORY_COLORS.default;

  return (
    <div className="scheme-card card">
      <div className="scheme-card-header" style={{ borderLeft: `4px solid ${color}` }}>
        <span className="badge" style={{ background: `${color}18`, color }}>
          {scheme.category}
        </span>
        <span className="scheme-gov-tag">{scheme.state_or_central}</span>
      </div>

      <h3 className="scheme-card-name">{name}</h3>
      <p className="scheme-card-desc">
        {desc && desc.length > 140 ? desc.substring(0, 140) + '…' : desc}
      </p>

      {scheme.benefits_summary_en && (
        <div className="scheme-benefit">
          <span className="benefit-label">
            {lang === 'te' ? 'ప్రయోజనం:' : 'Benefit:'}
          </span>
          <span>
            {(lang === 'te' ? scheme.benefits_summary_te : scheme.benefits_summary_en)?.substring(0, 90)}…
          </span>
        </div>
      )}

      {scheme.last_verified_at && (
        <p className="scheme-verified">
          <Calendar size={12} />
          {lang === 'te' ? 'ధృవీకరించబడింది:' : 'Verified:'} {scheme.last_verified_at}
        </p>
      )}

      <div className="scheme-card-footer">
        <Link to={`/schemes/${scheme.id}`} className="btn btn-primary btn-sm">
          {lang === 'te' ? 'వివరాలు చూడండి' : 'View Details'}
          <ChevronRight size={15} />
        </Link>
        {scheme.official_url && (
          <a
            href={scheme.official_url}
            target="_blank"
            rel="noopener noreferrer"
            className="btn btn-secondary btn-sm"
          >
            <ExternalLink size={14} />
            {lang === 'te' ? 'పోర్టల్' : 'Portal'}
          </a>
        )}
      </div>
    </div>
  );
}
