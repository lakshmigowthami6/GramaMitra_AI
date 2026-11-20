import React, { useState, useEffect, useRef, useCallback } from 'react';
import { useSearchParams } from 'react-router-dom';
import { Send, Mic, MicOff, Volume2, VolumeX, Trash2, Plus, User, Bot, Loader } from 'lucide-react';
import { useLanguage } from '../context/LanguageContext';
import { sendChatMessage, clearChatHistory } from '../services/api';
import './ChatPage.css';

const SESSION_KEY = 'gramamitra_session_id';
const SUGGESTIONS = {
  te: [
    'రైతులకు ఏ పథకాలు ఉన్నాయి?',
    'పీఎం కిసాన్ పథకానికి నేను అర్హుడినా?',
    'పెన్షన్ పొందడానికి అవసరమైన పత్రాలు ఏమిటి?',
    'ఆయుష్మాన్ భారత్ పథకం ఏమిటి?',
    'ఆన్‌లైన్‌లో దరఖాస్తు ఎలా చేయాలి?',
    'సర్కార్ వెబ్‌సైట్ తెరుచుకోలేదు, ఏమి చేయాలి?',
    'స్మార్ట్‌ఫోన్‌లో ఇంటర్నెట్ ఎలా వాడాలి?',
    'YSR ఆరోగ్యశ్రీ పథకానికి ఎలా నమోదు చేయాలి?',
  ],
  en: [
    'What schemes are available for farmers?',
    'Am I eligible for PM-KISAN scheme?',
    'What documents are needed for pension?',
    'What is Ayushman Bharat scheme?',
    'How to apply online for a government scheme?',
    'Government website is not opening, what to do?',
    'How to use internet on a smartphone?',
    'How to register for YSR Aarogyasri scheme?',
  ]
};

function getOrCreateSessionId() {
  let sid = sessionStorage.getItem(SESSION_KEY);
  if (!sid) {
    sid = `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    sessionStorage.setItem(SESSION_KEY, sid);
  }
  return sid;
}

export default function ChatPage() {
  const { t, lang } = useLanguage();
  const [searchParams] = useSearchParams();
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState(getOrCreateSessionId);
  const [isListening, setIsListening] = useState(false);
  const [ttsEnabled, setTtsEnabled] = useState(true);
  const [speakingIdx, setSpeakingIdx] = useState(null);
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);
  const recognitionRef = useRef(null);

  // Auto-scroll
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Auto-fill from URL param
  useEffect(() => {
    const q = searchParams.get('q');
    if (q) {
      setInput(q);
      setTimeout(() => {
        handleSend(q);
      }, 300);
    }
  }, []); // eslint-disable-line

  const addMessage = useCallback((role, content, metadata = {}) => {
    setMessages(prev => [...prev, { role, content, metadata, timestamp: Date.now() }]);
  }, []);

  const handleSend = useCallback(async (overrideText) => {
    const text = (overrideText || input).trim();
    if (!text || loading) return;
    setInput('');
    addMessage('user', text);
    setLoading(true);
    try {
      const res = await sendChatMessage(text, sessionId, lang);
      const data = res.data;
      addMessage('assistant', data.answer || data.message || 'No response', {
        sources: data.sources,
        scheme_name: data.scheme_name,
        intent: data.intent,
      });
      if (ttsEnabled && data.answer) {
        speak(data.answer);
      }
    } catch (e) {
      addMessage('assistant', lang === 'te'
        ? 'క్షమించండి, ఏదో సమస్య వచ్చింది. మళ్ళీ ప్రయత్నించండి.'
        : 'Sorry, something went wrong. Please try again.',
        { error: true });
    } finally {
      setLoading(false);
    }
  }, [input, loading, sessionId, lang, ttsEnabled, addMessage]);

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleNewChat = async () => {
    if (messages.length === 0) return;
    try { await clearChatHistory(sessionId); } catch (e) { console.error(e); }
    const newSid = `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    sessionStorage.setItem(SESSION_KEY, newSid);
    setSessionId(newSid);
    setMessages([]);
    setSpeakingIdx(null);
    window.speechSynthesis?.cancel();
  };

  // Voice input
  const toggleVoice = () => {
    if (isListening) {
      recognitionRef.current?.stop();
      setIsListening(false);
      return;
    }
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      alert(lang === 'te' ? 'మీ బ్రౌజర్ వాయిస్ ఇన్‌పుట్‌కు మద్దతు ఇవ్వడం లేదు.' : 'Your browser does not support voice input.');
      return;
    }
    const recognition = new SpeechRecognition();
    recognition.lang = lang === 'te' ? 'te-IN' : 'en-IN';
    recognition.interimResults = false;
    recognition.onresult = (e) => {
      const transcript = e.results[0]?.[0]?.transcript || '';
      setInput(transcript);
    };
    recognition.onend = () => setIsListening(false);
    recognition.onerror = () => setIsListening(false);
    recognition.start();
    recognitionRef.current = recognition;
    setIsListening(true);
  };

  // Text-to-speech
  const speak = (text) => {
    if (!ttsEnabled || !window.speechSynthesis) return;
    window.speechSynthesis.cancel();
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = lang === 'te' ? 'te-IN' : 'en-IN';
    utter.rate = 0.9;
    window.speechSynthesis.speak(utter);
  };

  const toggleSpeak = (idx, text) => {
    if (speakingIdx === idx) {
      window.speechSynthesis?.cancel();
      setSpeakingIdx(null);
    } else {
      window.speechSynthesis?.cancel();
      setSpeakingIdx(idx);
      speak(text);
      window.speechSynthesis.onend = () => setSpeakingIdx(null);
    }
  };

  const suggestions = SUGGESTIONS[lang] || SUGGESTIONS.en;

  return (
    <div className="chat-page">
      {/* Sidebar */}
      <aside className="chat-sidebar">
        <div className="sidebar-header">
          <h2>{t('assistant')}</h2>
          <button className="btn btn-primary btn-sm" onClick={handleNewChat} title={t('newChat')}>
            <Plus size={16} /> {t('newChat')}
          </button>
        </div>

        <div className="suggestions-panel">
          <p className="suggestions-label">{t('suggestedQuestions')}</p>
          {suggestions.map((s, i) => (
            <button key={i} className="suggestion-item" onClick={() => { setInput(s); inputRef.current?.focus(); }}>
              {s}
            </button>
          ))}
        </div>

        <div className="sidebar-controls">
          <label className="control-toggle">
            {ttsEnabled ? <Volume2 size={16} /> : <VolumeX size={16} />}
            <span>{lang === 'te' ? 'చదివి వినిపించు' : 'Read Aloud'}</span>
            <input type="checkbox" checked={ttsEnabled} onChange={e => setTtsEnabled(e.target.checked)} />
          </label>
        </div>
      </aside>

      {/* Chat Area */}
      <div className="chat-main">
        <div className="chat-messages">
          {messages.length === 0 && (
            <div className="chat-welcome">
              <div className="welcome-icon">🙏</div>
              <h3>{lang === 'te' ? 'నమస్కారం! నేను గ్రామమిత్ర AI సహాయకుడిని.' : 'Namaskaram! I am GramaMitra AI Assistant.'}</h3>
              <p>
                {lang === 'te'
                  ? 'ప్రభుత్వ పథకాలు, అర్హత, పత్రాలు & డిజిటల్ సేవల గురించి నన్ను అడగండి.'
                  : 'Ask me about government schemes, eligibility, documents & digital services.'}
              </p>
              <div className="welcome-suggestions">
                {suggestions.slice(0, 4).map((s, i) => (
                  <button key={i} className="suggestion-pill" onClick={() => handleSend(s)}>{s}</button>
                ))}
              </div>
            </div>
          )}

          {messages.map((msg, idx) => (
            <div key={idx} className={`message-row ${msg.role}`}>
              <div className={`message-avatar ${msg.role}`}>
                {msg.role === 'user' ? <User size={16} /> : <Bot size={16} />}
              </div>
              <div className="message-bubble-wrap">
                <div className={`message-bubble ${msg.role} ${msg.metadata?.error ? 'error' : ''}`}>
                  <div className="message-text" style={{ whiteSpace: 'pre-wrap' }}>{msg.content}</div>
                  {msg.metadata?.sources?.length > 0 && (
                    <div className="message-sources">
                      <strong>{lang === 'te' ? 'మూలాలు:' : 'Sources:'}</strong>
                      {msg.metadata.sources.map((src, si) => (
                        <a key={si} href={src.url} target="_blank" rel="noopener noreferrer">
                          {src.title || src.url}
                        </a>
                      ))}
                    </div>
                  )}
                  {msg.metadata?.scheme_name && (
                    <div className="message-tag">📋 {msg.metadata.scheme_name}</div>
                  )}
                </div>
                {msg.role === 'assistant' && (
                  <button
                    className={`speak-btn ${speakingIdx === idx ? 'speaking' : ''}`}
                    onClick={() => toggleSpeak(idx, msg.content)}
                    title={t('readAloud')}
                  >
                    {speakingIdx === idx ? <VolumeX size={14} /> : <Volume2 size={14} />}
                  </button>
                )}
              </div>
            </div>
          ))}

          {loading && (
            <div className="message-row assistant">
              <div className="message-avatar assistant"><Bot size={16} /></div>
              <div className="message-bubble assistant typing">
                <Loader size={16} className="typing-spinner" />
                <span>{lang === 'te' ? 'ఆలోచిస్తున్నాను...' : 'Thinking...'}</span>
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Input */}
        <div className="chat-input-area">
          {messages.length > 0 && (
            <button className="clear-chat-btn" onClick={handleNewChat} title={t('newChat')}>
              <Trash2 size={16} />
            </button>
          )}
          <div className="input-wrapper">
            <textarea
              ref={inputRef}
              className="chat-textarea"
              rows={1}
              placeholder={t('chatPlaceholder')}
              value={input}
              onChange={e => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              disabled={loading}
            />
            <div className="input-buttons">
              <button
                className={`voice-btn ${isListening ? 'active' : ''}`}
                onClick={toggleVoice}
                title={t('voiceInput')}
              >
                {isListening ? <MicOff size={18} /> : <Mic size={18} />}
              </button>
              <button
                className="send-btn"
                onClick={() => handleSend()}
                disabled={loading || !input.trim()}
                title={t('send')}
              >
                <Send size={18} />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
