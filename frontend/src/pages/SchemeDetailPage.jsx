import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import {
  ArrowLeft, ExternalLink, CheckCircle, AlertTriangle,
  FileText, List, Shield, Calendar
} from 'lucide-react';
import { useLanguage } from '../context/LanguageContext';
import { getSchemeDetail, checkEligibility } from '../services/api';
import './SchemeDetailPage.css';

export default function SchemeDetailPage() {
  const { id } = useParams();
  const { t, lang } = useLanguage();
  const [scheme, setScheme] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('overview');
  const [eligAnswers, setEligAnswers] = useState({});
  const [eligResult, setEligResult] = useState(null);
  const [checkingElig, setCheckingElig] = useState(false);

  useEffect(() => {
    setLoading(true);
    getSchemeDetail(id, lang)
      .then(res => setScheme(res.data))
      .catch(e => setError(e.message))
      .finally(() => setLoading(false));
  }, [id, lang]);

  const handleEligCheck = async () => {
    setCheckingElig(true);
    try {
      const res = await checkEligibility(id, eligAnswers);
      setEligResult(res.data);
    } catch (e) {
      setEligResult({ error: e.message });
    } finally {
      setCheckingElig(false);
    }
  };

  if (loading) return <div className="page-loading container"><div className="spinner" /><p>{t('loading')}</p></div>;
  if (error) return <div className="container"><div className="error-banner">{t('error')}: {error}</div></div>;
  if (!scheme) return null;

  const name = lang === 'te' ? scheme.name_te : scheme.name_en;
  const desc = lang === 'te' ? scheme.description_te : scheme.description_en;
  const benefits = lang === 'te' ? scheme.benefits_summary_te : scheme.benefits_summary_en;
  const notes = lang === 'te' ? scheme.important_notes_te : scheme.important_notes_en;
  const beneficiaries = lang === 'te' ? scheme.target_beneficiaries_te : scheme.target_beneficiaries_en;

  const tabs = [
    { id: 'overview', label: lang === 'te' ? 'సారాంశం' : 'Overview' },
    { id: 'eligibility', label: lang === 'te' ? 'అర్హత' : 'Eligibility' },
    { id: 'documents', label: lang === 'te' ? 'పత్రాలు' : 'Documents' },
    { id: 'steps', label: lang === 'te' ? 'దరఖాస్తు' : 'Application' },
  ];

  return (
    <div className="scheme-detail-page container">
      <Link to="/schemes" className="back-link">
        <ArrowLeft size={16} /> {t('backToSchemes')}
      </Link>

      {/* Header */}
      <div className="detail-header">
        <div className="detail-tags">
          <span className="badge badge-primary">{scheme.category}</span>
          <span className="badge badge-success">{scheme.state_or_central}</span>
          {scheme.last_verified_at && (
            <span className="verified-date">
              <Calendar size={12} /> {lang === 'te' ? 'ధృవీకరించబడింది:' : 'Verified:'} {scheme.last_verified_at}
            </span>
          )}
        </div>
        <h1 className="detail-title">{name}</h1>
        {beneficiaries && (
          <p className="detail-beneficiaries">
            <Shield size={15} />
            {lang === 'te' ? 'ఎవరికి:' : 'For:'} {beneficiaries}
          </p>
        )}
        {scheme.official_url && (
          <a href={scheme.official_url} target="_blank" rel="noopener noreferrer" className="btn btn-primary">
            <ExternalLink size={16} /> {t('officialWebsite')}
          </a>
        )}
      </div>

      {/* Benefits Banner */}
      {benefits && (
        <div className="benefits-banner">
          <CheckCircle size={20} />
          <div>
            <strong>{t('benefits')}:</strong>
            <p>{benefits}</p>
          </div>
        </div>
      )}

      {/* Important Notes */}
      {notes && (
        <div className="notes-banner">
          <AlertTriangle size={20} />
          <div>
            <strong>{t('importantNotes')}:</strong>
            <p>{notes}</p>
          </div>
        </div>
      )}

      {/* Tabs */}
      <div className="detail-tabs">
        {tabs.map(tab => (
          <button
            key={tab.id}
            className={`tab-btn ${activeTab === tab.id ? 'active' : ''}`}
            onClick={() => setActiveTab(tab.id)}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Tab Content */}
      <div className="tab-content">
        {/* Overview */}
        {activeTab === 'overview' && (
          <div className="tab-panel">
            <h2>{lang === 'te' ? 'పథకం గురించి' : 'About the Scheme'}</h2>
            <p className="detail-desc">{desc}</p>
          </div>
        )}

        {/* Eligibility */}
        {activeTab === 'eligibility' && (
          <div className="tab-panel">
            <h2><CheckCircle size={18} /> {t('eligibilityCriteria')}</h2>
            {scheme.criteria?.length > 0 ? (
              <>
                <div className="criteria-list">
                  {scheme.criteria.map((c, i) => {
                    const question = lang === 'te' ? c.question_te : c.question_en;
                    const explanation = lang === 'te' ? c.explanation_te : c.explanation_en;
                    return (
                      <div key={i} className="criterion-item">
                        <div className="criterion-question">
                          <span className="criterion-num">{i + 1}</span>
                          <div>
                            <p>{question}</p>
                            {explanation && <p className="criterion-explanation">{explanation}</p>}
                            {c.is_mandatory && (
                              <span className="badge badge-warning">{t('mandatory')}</span>
                            )}
                          </div>
                        </div>
                        <div className="criterion-answer">
                          <button
                            className={`answer-btn ${eligAnswers[c.rule_code] === 'true' ? 'selected yes' : ''}`}
                            onClick={() => setEligAnswers(a => ({ ...a, [c.rule_code]: 'true' }))}
                          >{t('yes')}</button>
                          <button
                            className={`answer-btn ${eligAnswers[c.rule_code] === 'false' ? 'selected no' : ''}`}
                            onClick={() => setEligAnswers(a => ({ ...a, [c.rule_code]: 'false' }))}
                          >{t('no')}</button>
                        </div>
                      </div>
                    );
                  })}
                </div>
                <button
                  className="btn btn-primary"
                  onClick={handleEligCheck}
                  disabled={checkingElig || Object.keys(eligAnswers).length === 0}
                >
                  {checkingElig ? <><div className="spinner" style={{width:16,height:16}} /> {t('loading')}</> : t('checkEligibility')}
                </button>
                {eligResult && (
                  <div className={`elig-result ${eligResult.is_eligible ? 'eligible' : 'not-eligible'}`}>
                    {eligResult.is_eligible ? <CheckCircle size={24} /> : <AlertTriangle size={24} />}
                    <div>
                      <strong>{eligResult.is_eligible ? t('eligible') : t('notEligible')}</strong>
                      {eligResult.message && <p>{eligResult.message}</p>}
                      {eligResult.failed_criteria?.length > 0 && (
                        <ul>
                          {eligResult.failed_criteria.map((fc, i) => <li key={i}>{fc}</li>)}
                        </ul>
                      )}
                    </div>
                  </div>
                )}
              </>
            ) : (
              <p className="empty-state">{lang === 'te' ? 'అర్హత వివరాలు అందుబాటులో లేవు' : 'Eligibility details not available'}</p>
            )}
          </div>
        )}

        {/* Documents */}
        {activeTab === 'documents' && (
          <div className="tab-panel">
            <h2><FileText size={18} /> {t('requiredDocuments')}</h2>
            {scheme.documents?.length > 0 ? (
              <div className="documents-list">
                {scheme.documents.map((doc, i) => {
                  const docName = lang === 'te' ? doc.document_name_te : doc.document_name_en;
                  const purpose = lang === 'te' ? doc.purpose_te : doc.purpose_en;
                  const authority = lang === 'te' ? doc.issuing_authority_te : doc.issuing_authority_en;
                  const tips = lang === 'te' ? doc.preparation_tips_te : doc.preparation_tips_en;
                  return (
                    <div key={i} className="document-card">
                      <div className="doc-header">
                        <FileText size={18} />
                        <h3>{docName}</h3>
                        {doc.is_mandatory ? (
                          <span className="badge badge-warning">{t('mandatory')}</span>
                        ) : (
                          <span className="badge">{t('optional')}</span>
                        )}
                      </div>
                      {purpose && <p><strong>{t('purpose')}:</strong> {purpose}</p>}
                      {authority && <p><strong>{t('issuedBy')}:</strong> {authority}</p>}
                      {tips && <div className="doc-tips"><strong>{t('tips')}:</strong> {tips}</div>}
                    </div>
                  );
                })}
              </div>
            ) : (
              <p className="empty-state">{lang === 'te' ? 'పత్రాల వివరాలు అందుబాటులో లేవు' : 'Document details not available'}</p>
            )}
          </div>
        )}

        {/* Application Steps */}
        {activeTab === 'steps' && (
          <div className="tab-panel">
            <h2><List size={18} /> {t('applicationSteps')}</h2>
            {scheme.steps?.length > 0 ? (
              <div className="steps-list">
                {scheme.steps.map((step, i) => {
                  const title = lang === 'te' ? step.title_te : step.title_en;
                  const description = lang === 'te' ? step.description_te : step.description_en;
                  const portal = lang === 'te' ? step.portal_or_offline_te : step.portal_or_offline_en;
                  const caution = lang === 'te' ? step.caution_warning_te : step.caution_warning_en;
                  return (
                    <div key={i} className="step-card">
                      <div className="step-num">{step.step_number}</div>
                      <div className="step-body">
                        <h3>{title}</h3>
                        <p>{description}</p>
                        {portal && <p className="step-portal"><strong>{lang === 'te' ? 'ఎక్కడ:' : 'Where:'}</strong> {portal}</p>}
                        {caution && (
                          <div className="step-caution">
                            <AlertTriangle size={14} /> {caution}
                          </div>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            ) : (
              <p className="empty-state">{lang === 'te' ? 'దరఖాస్తు దశలు అందుబాటులో లేవు' : 'Application steps not available'}</p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
