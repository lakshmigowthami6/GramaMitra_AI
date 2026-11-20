import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ArrowLeft, CheckCircle, XCircle, ChevronRight, Award } from 'lucide-react';
import { useLanguage } from '../context/LanguageContext';
import { getLessonDetail } from '../services/api';
import './LessonDetailPage.css';

export default function LessonDetailPage() {
  const { id } = useParams();
  const { t, lang } = useLanguage();
  const [lesson, setLesson] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [quizAnswers, setQuizAnswers] = useState({});
  const [quizSubmitted, setQuizSubmitted] = useState(false);
  const [quizScore, setQuizScore] = useState(null);

  useEffect(() => {
    setLoading(true);
    getLessonDetail(id, lang)
      .then(res => setLesson(res.data))
      .catch(e => setError(e.message))
      .finally(() => setLoading(false));
  }, [id, lang]);

  if (loading) return <div className="page-loading container"><div className="spinner" /></div>;
  if (error) return <div className="container"><div className="error-banner">{error}</div></div>;
  if (!lesson) return null;

  const title = lang === 'te' ? lesson.title_te : lesson.title_en;
  const content = lang === 'te' ? lesson.content_te : lesson.content_en;
  const summary = lang === 'te' ? lesson.summary_te : lesson.summary_en;

  const handleQuizSubmit = () => {
    if (!lesson.quiz?.length) return;
    let correct = 0;
    lesson.quiz.forEach(q => {
      if (quizAnswers[q.id] === q.correct_option) correct++;
    });
    setQuizScore({ correct, total: lesson.quiz.length });
    setQuizSubmitted(true);
  };

  return (
    <div className="lesson-detail-page container">
      <Link to="/learning" className="back-link">
        <ArrowLeft size={16} /> {lang === 'te' ? '← పాఠాలకు తిరిగి' : '← Back to Lessons'}
      </Link>

      <div className="lesson-header">
        <div className="lesson-tags">
          <span className="badge badge-primary">{lesson.module_category}</span>
          {lesson.difficulty_level && (
            <span className="badge badge-success">{lesson.difficulty_level}</span>
          )}
        </div>
        <h1 className="lesson-title">{title}</h1>
        {lesson.estimated_duration_minutes && (
          <p className="lesson-duration">
            ⏱ {lesson.estimated_duration_minutes} {lang === 'te' ? 'నిమిషాలు' : 'minutes'}
          </p>
        )}
      </div>

      {/* Summary */}
      {summary && (
        <div className="lesson-summary">
          <strong>{lang === 'te' ? 'సారాంశం:' : 'Summary:'}</strong>
          <p>{summary}</p>
        </div>
      )}

      {/* Main content */}
      <div className="lesson-content">
        {content?.split('\n').map((para, i) => para.trim() ? <p key={i}>{para}</p> : <br key={i} />)}
      </div>

      {/* Key points */}
      {lesson.key_points && (
        <div className="lesson-keypoints">
          <h2>{lang === 'te' ? 'ముఖ్య విషయాలు' : 'Key Points'}</h2>
          <ul>
            {(Array.isArray(lesson.key_points)
              ? lesson.key_points
              : (lesson.key_points_te || lesson.key_points_en || '').split('\n').filter(Boolean)
            ).map((point, i) => (
              <li key={i}>
                <ChevronRight size={15} />
                <span>{typeof point === 'object' ? (lang === 'te' ? point.te : point.en) : point}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Quiz */}
      {lesson.quiz?.length > 0 && (
        <div className="lesson-quiz">
          <h2><Award size={20} /> {t('quiz')}</h2>
          <div className="quiz-questions">
            {lesson.quiz.map((q, qi) => {
              const qText = lang === 'te' ? q.question_te : q.question_en;
              const options = lang === 'te'
                ? [q.option_a_te, q.option_b_te, q.option_c_te, q.option_d_te]
                : [q.option_a_en, q.option_b_en, q.option_c_en, q.option_d_en];
              const optionKeys = ['A', 'B', 'C', 'D'];
              const userAns = quizAnswers[q.id];
              const isCorrect = quizSubmitted && userAns === q.correct_option;
              const isWrong = quizSubmitted && userAns && userAns !== q.correct_option;

              return (
                <div key={q.id} className={`quiz-question ${quizSubmitted ? (isCorrect ? 'correct' : isWrong ? 'wrong' : '') : ''}`}>
                  <p className="q-text"><strong>{qi + 1}.</strong> {qText}</p>
                  <div className="q-options">
                    {options.map((opt, oi) => opt ? (
                      <label key={oi} className={`q-option ${
                        quizSubmitted
                          ? optionKeys[oi] === q.correct_option ? 'correct-opt' : optionKeys[oi] === userAns ? 'wrong-opt' : ''
                          : userAns === optionKeys[oi] ? 'selected' : ''
                      }`}>
                        <input
                          type="radio"
                          name={`q_${q.id}`}
                          value={optionKeys[oi]}
                          checked={userAns === optionKeys[oi]}
                          onChange={() => !quizSubmitted && setQuizAnswers(a => ({ ...a, [q.id]: optionKeys[oi] }))}
                          disabled={quizSubmitted}
                        />
                        <span className="opt-key">{optionKeys[oi]}.</span> {opt}
                      </label>
                    ) : null)}
                  </div>
                  {quizSubmitted && (
                    <div className={`q-feedback ${isCorrect ? 'correct' : 'wrong'}`}>
                      {isCorrect ? <CheckCircle size={14} /> : <XCircle size={14} />}
                      {isCorrect
                        ? (lang === 'te' ? 'సరైన సమాధానం!' : 'Correct!')
                        : `${lang === 'te' ? 'సరైన సమాధానం:' : 'Correct answer:'} ${q.correct_option}`}
                      {q.explanation_te && (
                        <p className="q-explanation">{lang === 'te' ? q.explanation_te : q.explanation_en}</p>
                      )}
                    </div>
                  )}
                </div>
              );
            })}
          </div>

          {!quizSubmitted ? (
            <button
              className="btn btn-primary"
              onClick={handleQuizSubmit}
              disabled={Object.keys(quizAnswers).length < lesson.quiz.length}
            >
              {lang === 'te' ? 'సమాధానాలు సమర్పించు' : 'Submit Answers'}
            </button>
          ) : (
            <div className="quiz-result">
              <Award size={28} />
              <h3>
                {lang === 'te'
                  ? `మీ స్కోర్: ${quizScore.correct}/${quizScore.total}`
                  : `Your score: ${quizScore.correct}/${quizScore.total}`}
              </h3>
              <p>
                {quizScore.correct === quizScore.total
                  ? (lang === 'te' ? '🎉 అభినందనలు! అన్ని సమాధానాలు సరైనవి!' : '🎉 Congratulations! All answers correct!')
                  : quizScore.correct >= quizScore.total / 2
                    ? (lang === 'te' ? '👍 మంచి ప్రయత్నం! మళ్ళీ పరీక్షించుకోండి.' : '👍 Good effort! Review and try again.')
                    : (lang === 'te' ? 'మళ్ళీ పాఠం చదివి ప్రయత్నించండి.' : 'Read the lesson again and retry.')}
              </p>
              <button
                className="btn btn-secondary"
                onClick={() => { setQuizAnswers({}); setQuizSubmitted(false); setQuizScore(null); }}
              >
                {lang === 'te' ? 'మళ్ళీ ప్రయత్నించు' : 'Try Again'}
              </button>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
