import React, { createContext, useContext, useState, useCallback } from 'react';

const translations = {
  te: {
    appName: 'గ్రామమిత్ర AI',
    appTagline: 'డిజిటల్ అక్షరాస్యత & ఈ-గవర్నెన్స్ సహాయకుడు',
    home: 'హోమ్',
    schemes: 'పథకాలు',
    assistant: 'AI సహాయకుడు',
    eligibility: 'అర్హత తనిఖీ',
    documents: 'పత్రాలు',
    learning: 'డిజిటల్ నేర్చుకోండి',
    faq: 'సహాయం & FAQ',
    search: 'శోధించు...',
    seeAll: 'అన్నీ చూడండి',
    readMore: 'మరిన్ని వివరాలు',
    loading: 'లోడ్ అవుతోంది...',
    error: 'ఏదో సమస్య వచ్చింది',
    retry: 'మళ్ళీ ప్రయత్నించండి',
    noResults: 'ఫలితాలు కనుగొనబడలేదు',
    welcomeTitle: 'గ్రామమిత్ర AI కు స్వాగతం',
    welcomeDesc: 'ప్రభుత్వ పథకాలు, అర్హత, పత్రాలు & డిజిటల్ సేవల గురించి సులభంగా తెలుసుకోండి.',
    heroBtn1: 'AI తో మాట్లాడండి',
    heroBtn2: 'పథకాలు చూడండి',
    schemesTitle: 'ప్రభుత్వ పథకాలు',
    schemesDesc: 'కేంద్ర & ఆంధ్రప్రదేశ్ ప్రభుత్వ పథకాలు అన్వేషించండి',
    chatPlaceholder: 'మీ ప్రశ్న ఇక్కడ టైప్ చేయండి...',
    send: 'పంపండి',
    newChat: 'కొత్త చాట్',
    suggestedQuestions: 'సూచించిన ప్రశ్నలు',
    lessonsTitle: 'డిజిటల్ అక్షరాస్యత పాఠాలు',
    lessonsDesc: 'స్మార్ట్‌ఫోన్, ఇంటర్నెట్ & ఆన్‌లైన్ సేవలు నేర్చుకోండి',
    faqTitle: 'తరచుగా అడిగే ప్రశ్నలు',
    faqDesc: 'మీ సందేహాలకు సమాధానాలు',
    category: 'విభాగం',
    allCategories: 'అన్ని విభాగాలు',
    benefits: 'ప్రయోజనాలు',
    eligibilityCriteria: 'అర్హత నిబంధనలు',
    requiredDocuments: 'అవసరమైన పత్రాలు',
    applicationSteps: 'దరఖాస్తు దశలు',
    officialWebsite: 'అధికారిక వెబ్‌సైట్',
    lastVerified: 'చివరిగా ధృవీకరించబడింది',
    importantNotes: 'ముఖ్య గమనికలు',
    yes: 'అవును',
    no: 'కాదు',
    checkEligibility: 'అర్హత తనిఖీ చేయండి',
    eligible: 'మీరు అర్హులు!',
    notEligible: 'మీరు అర్హులు కాదు',
    footer: '© 2025 గ్రామమిత్ర AI - కొనంకి గ్రామం, మార్తూరు మండలం, బాపట్ల జిల్లా, ఆంధ్రప్రదేశ్',
    changeLang: 'English',
    backToSchemes: '← పథకాలకు తిరిగి',
    startLesson: 'పాఠం ప్రారంభించండి',
    quiz: 'క్విజ్',
    next: 'తదుపరి',
    previous: 'మునుపటి',
    voiceInput: 'గొంతు ద్వారా',
    readAloud: 'చదవండి',
    purpose: 'ఉద్దేశ్యం',
    issuedBy: 'జారీ సంస్థ',
    tips: 'సూచనలు',
    mandatory: 'తప్పనిసరి',
    optional: 'ఐచ్ఛికం',
  },
  en: {
    appName: 'GramaMitra AI',
    appTagline: 'Digital Literacy & E-Governance Assistant',
    home: 'Home',
    schemes: 'Schemes',
    assistant: 'AI Assistant',
    eligibility: 'Eligibility Check',
    documents: 'Documents',
    learning: 'Digital Learning',
    faq: 'Help & FAQ',
    search: 'Search...',
    seeAll: 'See All',
    readMore: 'Read More',
    loading: 'Loading...',
    error: 'Something went wrong',
    retry: 'Try Again',
    noResults: 'No results found',
    welcomeTitle: 'Welcome to GramaMitra AI',
    welcomeDesc: 'Easily learn about government schemes, eligibility, documents & digital services.',
    heroBtn1: 'Chat with AI',
    heroBtn2: 'Browse Schemes',
    schemesTitle: 'Government Schemes',
    schemesDesc: 'Explore Central & Andhra Pradesh Government schemes',
    chatPlaceholder: 'Type your question here...',
    send: 'Send',
    newChat: 'New Chat',
    suggestedQuestions: 'Suggested Questions',
    lessonsTitle: 'Digital Literacy Lessons',
    lessonsDesc: 'Learn about smartphones, internet & online services',
    faqTitle: 'Frequently Asked Questions',
    faqDesc: 'Find answers to common questions',
    category: 'Category',
    allCategories: 'All Categories',
    benefits: 'Benefits',
    eligibilityCriteria: 'Eligibility Criteria',
    requiredDocuments: 'Required Documents',
    applicationSteps: 'Application Steps',
    officialWebsite: 'Official Website',
    lastVerified: 'Last Verified',
    importantNotes: 'Important Notes',
    yes: 'Yes',
    no: 'No',
    checkEligibility: 'Check Eligibility',
    eligible: 'You are eligible!',
    notEligible: 'You are not eligible',
    footer: '© 2025 GramaMitra AI - Konanki Village, Martur Mandal, Bapatla District, Andhra Pradesh',
    changeLang: 'తెలుగు',
    backToSchemes: '← Back to Schemes',
    startLesson: 'Start Lesson',
    quiz: 'Quiz',
    next: 'Next',
    previous: 'Previous',
    voiceInput: 'Voice Input',
    readAloud: 'Read Aloud',
    purpose: 'Purpose',
    issuedBy: 'Issued By',
    tips: 'Tips',
    mandatory: 'Mandatory',
    optional: 'Optional',
  }
};

const LanguageContext = createContext();

export function LanguageProvider({ children }) {
  const [lang, setLang] = useState('te');

  const toggleLang = useCallback(() => {
    setLang(prev => prev === 'te' ? 'en' : 'te');
  }, []);

  const t = useCallback((key) => {
    return translations[lang]?.[key] || translations.en?.[key] || key;
  }, [lang]);

  return (
    <LanguageContext.Provider value={{ lang, setLang, toggleLang, t }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useLanguage() {
  const context = useContext(LanguageContext);
  if (!context) throw new Error('useLanguage must be used within LanguageProvider');
  return context;
}
