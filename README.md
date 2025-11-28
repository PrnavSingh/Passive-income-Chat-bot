Passive Income Chat Bot

Simple chat bot that suggests passive income ideas and resources.
Frontend: HTML/JS. Backend: Python API (FastAPI recommended). Small, easy to run — perfect for a GitHub demo.

Demo
	•	Lightweight prototype for idea-sharing (rental income, dividend investing, digital products, affiliate marketing).
	•	Not financial advice — include a disclaimer in the repo.

⸻

Key info

Item	Value
Project	Passive Income Chat Bot
Stack	HTML (frontend) · Python API (FastAPI) · SQLite (optional)
Status	Minimal demo for GitHub


⸻

Short features
	•	Single-page HTML chat UI.
	•	/api/chat endpoint returning rule-based replies.
	•	Conversation history stored in SQLite (optional).
	•	Easy to extend with ML/NLP or external APIs.

⸻

Repo layout

Path	Purpose
frontend/index.html	Chat UI (static)
backend/app.py	Minimal FastAPI backend
backend/requirements.txt	Python deps
README.md	This file


⸻

Quick start (3 steps)
	1.	Clone:

git clone <repo-url>
cd passive-income-chat-bot

	2.	Backend (FastAPI minimal):

python -m venv venv
source venv/bin/activate    # or .\venv\Scripts\activate on Windows
pip install fastapi uvicorn

Create backend/app.py (minimal example):

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3, datetime

app = FastAPI()
DB = "chat_history.db"

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY, user_id TEXT, role TEXT, text TEXT, ts TEXT)""")
    conn.close()
init_db()

class ChatReq(BaseModel):
    user_id: str
    message: str

def store(user_id, role, text):
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO messages (user_id, role, text, ts) VALUES (?, ?, ?, ?)",
                 (user_id, role, text, datetime.datetime.utcnow().isoformat()))
    conn.commit(); conn.close()

def generate_reply(msg: str):
    m = msg.lower()
    if "rental" in m: return "Consider long-term rentals or short-term (Airbnb). Want pros/cons?"
    if "dividend" in m: return "Dividend investing focuses on stable companies—I can list resources."
    if "course" in m or "digital" in m: return "Digital products need topic, platform, marketing. Want checklist?"
    return "Ideas: rental income, dividend stocks, digital products, affiliate marketing. Which interests you?"

@app.post("/api/chat")
def chat(req: ChatReq):
    if not req.message.strip(): return {"reply":"Please type a message."}
    store(req.user_id, "user", req.message)
    r = generate_reply(req.message)
    store(req.user_id, "bot", r)
    return {"reply": r}

Run:

uvicorn backend.app:app --reload --port 8000

	3.	Frontend:

	•	Open frontend/index.html in a browser (or serve it).
	•	Ensure fetch calls point to http://localhost:8000/api/chat.

Example frontend fetch:

fetch('http://localhost:8000/api/chat', {
  method:'POST',
  headers:{'Content-Type':'application/json'},
  body: JSON.stringify({user_id:'guest', message: 'Tell me about dividend income'})
})
.then(r=>r.json()).then(d=>console.log(d.reply))


⸻

API (concise)

Method	Endpoint	Body	Returns
POST	/api/chat	{ user_id, message }	{ reply }


⸻

Config & env (optional)

Var	Example
PORT	8000
DATABASE (path)	chat_history.db


⸻

Notes & next steps
	•	Repo is intentionally small for GitHub. Add ML intent classification, LLM integration, or richer knowledge base later.
	•	Add CORS if serving frontend from another origin.
	•	Add a short disclaimer (not financial advice).

⸻

License & contact
	•	License: MIT (suggested)
	•	Contact: pranav@example.com (replace with real email)

⸻

If you want, I can:
	•	Convert this README into a ready README.md file for your repo, or
	•	Create a minimal docker-compose.yml for one-click run. Which do you prefer?
