# గ్రామమిత్ర AI | GramaMitra AI
### AI-Powered Digital Literacy & E-Governance Assistant

> Community Service Project — Konanki Village, Martur Mandal, Bapatla District, Andhra Pradesh

---

## 📋 Project Overview

GramaMitra AI is a Telugu-first, AI-powered web application designed to help rural citizens of Konanki Village access government welfare schemes, check eligibility, understand required documents, and improve their digital literacy.

**Problem Addressed:** 50+ residents surveyed in Konanki Village face difficulty accessing online government services due to language barriers, limited digital literacy, and confusing government portals.

---

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.11+
- Node.js 18+ (npm)
- Git

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd digital-literacy
```

### 2. Backend Setup
```powershell
# Create and activate virtual environment
python -m venv backend\venv
backend\venv\Scripts\activate

# Install Python packages
pip install flask flask-cors flask-sqlalchemy python-dotenv google-genai gunicorn pytest

# Configure environment variables
# Edit backend\.env and add your GEMINI_API_KEY (optional but recommended)

# Seed the database with government schemes, FAQs, and lessons
cd backend
python seed\seed_runner.py
cd ..
```

### 3. Frontend Setup
```powershell
cd frontend
npm install --legacy-peer-deps --ignore-scripts
node node_modules\esbuild\install.js   # Run esbuild postinstall manually
cd ..
```

### 4. Start the Application

**Terminal 1 — Backend:**
```powershell
cd backend
.\venv\Scripts\python.exe run.py
# Flask runs on http://127.0.0.1:5000
```

**Terminal 2 — Frontend:**
```powershell
cd frontend
npm run dev
# Vite dev server runs on http://localhost:3000
```

Open your browser to **http://localhost:3000**

---

## 🌐 Application Modules

| Module | URL | Description |
|--------|-----|-------------|
| Home | `/` | Welcome page with quick actions and featured schemes |
| AI Assistant | `/assistant` | AI chatbot for government scheme questions (Telugu + English) |
| Government Schemes | `/schemes` | Browse, search, and filter all schemes |
| Scheme Detail | `/schemes/:id` | Full detail with eligibility checker |
| Digital Learning | `/learning` | Digital literacy lessons with quizzes |
| Help & FAQ | `/faq` | Frequently asked questions |

---

## 🛠️ Technology Stack

### Frontend
- React 18, Vite 5, React Router 6
- Axios for API calls
- Lucide React icons
- CSS Modules (no Tailwind)
- Web Speech API (voice input + read-aloud)

### Backend
- Python 3.11, Flask 3
- Flask-CORS, Flask-SQLAlchemy
- SQLite (dev) / PostgreSQL (production)
- Google Gemini API (AI responses)

### AI Pipeline
```
User Input
→ Language & Intent Detection
→ Session Context Retrieval
→ Knowledge Base Retrieval (RAG)
→ Gemini API (if configured)
→ Response Validation
→ Telugu / English Response
```

---

## 📡 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| GET | `/api/schemes` | List schemes (filter by category, q, state_or_central) |
| GET | `/api/schemes/:id` | Scheme detail with criteria, documents, steps |
| GET | `/api/schemes/categories` | Available categories |
| GET | `/api/faqs` | FAQs (filter by category, q) |
| GET | `/api/lessons` | Digital literacy lessons |
| GET | `/api/lessons/:id` | Lesson detail with quiz |
| POST | `/api/chat` | Send chat message → AI response |
| DELETE | `/api/chat/history` | Clear conversation history |
| GET | `/api/eligibility/:id` | Eligibility criteria for a scheme |
| POST | `/api/eligibility/:id/check` | Check eligibility with user answers |

---

## 🔑 Environment Variables

### `backend/.env`
```env
FLASK_ENV=development
SECRET_KEY=change-this-in-production
PORT=5000
DATABASE_URL=sqlite:///gramamitra.db
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
GEMINI_API_KEY=your-gemini-api-key-here
```

> **Note:** The app works without a Gemini API key — it falls back to database-driven responses.
> Get a free Gemini API key at [Google AI Studio](https://aistudio.google.com/).

---

## 🗄️ Database Schema

| Table | Records | Description |
|-------|---------|-------------|
| `government_scheme` | 6 | Verified AP + Central schemes |
| `faq` | 6 | Community FAQs in Telugu + English |
| `digital_literacy_lesson` | 4 | Smartphone, Internet, Safety lessons |
| `eligibility_criterion` | ~16 | Per-scheme eligibility rules |
| `required_document` | ~18 | Document checklists per scheme |
| `application_step` | ~18 | Step-by-step application guides |
| `official_source` | 6 | Verified government portal sources |
| `user_session` | dynamic | Session management |
| `conversation_history` | dynamic | Chat history per session |

---

## 🚢 Deployment

### Frontend (Vercel)
```bash
# Build
cd frontend
npm run build

# Deploy to Vercel
vercel --prod
# Set environment variable: VITE_API_URL=https://your-backend.render.com
```

### Backend (Render)
1. Create a new **Web Service** on Render
2. Connect your GitHub repo
3. Set:
   - **Build Command:** `pip install -r backend/requirements.txt`
   - **Start Command:** `gunicorn -w 4 -b 0.0.0.0:$PORT run:flask_app`
   - **Root Directory:** `backend`
4. Add environment variables from `.env`
5. For production, switch `DATABASE_URL` to a PostgreSQL connection string

### Update frontend to point to production backend
In `frontend/vite.config.js`, the proxy is for dev only. For production, set:
```js
// In .env.production:
VITE_API_BASE_URL=https://your-backend.render.com/api
```
Then update `frontend/src/services/api.js`:
```js
const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '/api',
  ...
});
```

---

## 📁 Project Structure

```
digital-literacy/
├── backend/
│   ├── app/
│   │   ├── __init__.py        # Flask app factory
│   │   ├── config.py          # Configuration
│   │   ├── extensions.py      # DB, CORS extensions
│   │   ├── models/            # SQLAlchemy ORM models
│   │   ├── routes/            # API blueprints
│   │   ├── services/          # AI, session, retrieval services
│   │   ├── agent/             # AI pipeline modules
│   │   ├── tools/             # Tool functions for AI
│   │   └── utils/             # Validators, error handlers
│   ├── seed/
│   │   ├── seed_runner.py     # Main seed script
│   │   ├── seed_schemes.py    # Government scheme data
│   │   ├── seed_faqs.py       # FAQ data
│   │   └── seed_lessons.py    # Digital literacy lessons
│   ├── instance/
│   │   └── gramamitra.db      # SQLite database (auto-created)
│   ├── venv/                  # Python virtual environment
│   ├── .env                   # Environment variables (not committed)
│   ├── requirements.txt       # Python dependencies
│   └── run.py                 # Flask entry point
├── frontend/
│   ├── src/
│   │   ├── main.jsx           # React entry point
│   │   ├── App.jsx            # Router + routes
│   │   ├── context/
│   │   │   └── LanguageContext.jsx  # Telugu/English toggle
│   │   ├── components/
│   │   │   ├── Navbar.jsx     # Navigation bar
│   │   │   ├── Footer.jsx     # Footer
│   │   │   ├── Layout.jsx     # Page layout wrapper
│   │   │   └── SchemeCard.jsx # Reusable scheme card
│   │   ├── pages/
│   │   │   ├── HomePage.jsx   # Landing page
│   │   │   ├── SchemesPage.jsx         # Scheme list + search
│   │   │   ├── SchemeDetailPage.jsx    # Scheme detail + eligibility
│   │   │   ├── ChatPage.jsx            # AI chatbot
│   │   │   ├── LessonsPage.jsx         # Digital literacy lessons
│   │   │   ├── LessonDetailPage.jsx    # Lesson + quiz
│   │   │   └── FaqPage.jsx             # FAQ accordion
│   │   ├── services/
│   │   │   └── api.js         # Axios API client
│   │   └── styles/
│   │       └── global.css     # Global styles
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
└── README.md
```

---

## 🌟 Features

- ✅ **Telugu-first UI** — All content in Telugu + English toggle
- ✅ **AI Chatbot** — Context-aware answers with session memory
- ✅ **Voice Input** — Speak questions in Telugu or English
- ✅ **Read Aloud** — AI answers read aloud via Web Speech API
- ✅ **Scheme Explorer** — Browse, search, filter government schemes
- ✅ **Eligibility Checker** — Interactive eligibility questionnaire
- ✅ **Document Checklists** — Verified document lists per scheme
- ✅ **Application Guides** — Step-by-step guidance
- ✅ **Digital Lessons** — Lessons with knowledge quizzes
- ✅ **FAQ Accordion** — Searchable FAQ database
- ✅ **Mobile Responsive** — Works on mobile, tablet, desktop
- ✅ **Offline fallback** — Works without Gemini API key
- ✅ **RAG Architecture** — AI grounded in verified database content

---

## 🔧 Troubleshooting

**npm install fails on Windows:**
```powershell
npm install --legacy-peer-deps --ignore-scripts
node node_modules\esbuild\install.js
```

**Flask: "module 'app' has no attribute 'app_context'":**
- Fixed in `backend/app/__init__.py` — variable renamed to `flask_app` to avoid shadowing the `app` module.

**Gemini API not configured:**
- The app falls back gracefully. Add `GEMINI_API_KEY` to `backend/.env` for full AI responses.

**Database empty:**
```powershell
cd backend
.\venv\Scripts\python.exe seed\seed_runner.py
```

---

## 📜 License

This project is developed for community service purposes for Konanki Village, Martur Mandal, Bapatla District, Andhra Pradesh, India.

---

*Built with ❤️ for the digital empowerment of rural communities in Andhra Pradesh.*
