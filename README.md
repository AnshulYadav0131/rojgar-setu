# 🌉 Rojgar Setu — रोजगार सेतु

> Connecting daily wage workers with local employers across rural Uttar Pradesh

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![HTML CSS JS](https://img.shields.io/badge/Frontend-HTML%20CSS%20JS-orange)

---

## 📌 Problem Statement

Millions of daily wage workers in rural UP — electricians, plumbers, masons, carpenters — have no reliable way to find local work. Small businesses and households struggle to find skilled workers nearby. Rojgar Setu bridges this gap with a simple, bilingual (Hindi + English) platform.

---

## ✨ Features

### For Workers (मजदूर)
- 📝 Register with name, phone, skills, and district
- 🔍 Browse open jobs in their district
- ⚡ One-click job application
- 🔄 Toggle availability status

### For Employers (नियोक्ता)
- 📋 Post jobs in minutes
- 📍 Location and district-based job posting
- 💰 Set daily pay upfront
- 👥 View all applicants for each job

### Platform
- 🔐 Secure JWT authentication
- 🔒 bcrypt password hashing
- 🌐 Bilingual UI — Hindi + English
- 📱 Responsive design

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12 + FastAPI |
| Database | PostgreSQL 17 |
| ORM | SQLAlchemy |
| Auth | JWT + bcrypt |
| Frontend | HTML + CSS + JavaScript |
| API Docs | Swagger UI |

---

## 📁 Project Structure
rojgarsetu/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── routers/
│   ├── auth.py
│   ├── jobs.py
│   └── users.py
└── frontend/
├── index.html
├── register.html
├── login.html
└── jobs.html
---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/AnshulYadav0131/rojgar-setu.git
cd rojgar-setu
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install fastapi uvicorn[standard] psycopg2-binary sqlalchemy python-jose[cryptography] passlib[bcrypt] python-dotenv bcrypt==4.0.1
```

**4. Create PostgreSQL database**
```bash
psql -U postgres
CREATE DATABASE rojgarsetu;
\q
```

**5. Create `.env` file**
DATABASE_URL=postgresql://postgres:YOURPASSWORD@localhost:5432/rojgarsetu
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080
**6. Run the backend**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

**7. Run the frontend**
```bash
cd frontend
python -m http.server 3000
```

**8. Open in browser**
- Frontend: http://localhost:3000
- API Docs: http://localhost:8080/docs

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /auth/register | Register new user |
| POST | /auth/login | Login and get token |
| GET | /jobs/ | Get all open jobs |
| POST | /jobs/ | Post a new job |
| POST | /jobs/{id}/apply | Apply for a job |
| GET | /jobs/{id}/applicants | Get applicants |
| GET | /users/me | Get my profile |

---

## 👨‍💻 Developer

**Anshul Yadav**
- 📧 anshulyadav011220@gmail.com
- 🐙 [GitHub](https://github.com/AnshulYadav0131)

---

> Built with ❤️ for rural India — रूरल इंडिया के लिए