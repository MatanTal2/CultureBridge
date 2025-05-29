# CultureBridge – Seamless Messaging Across Worlds

## 1‑Line Pitch
A communication service that translates and bridges messages across cultural and digital divides — e.g., from email to WhatsApp, adapted to tone and context.

## Target Users
- Parents from diverse communities
- Educators and school staff (e.g., public schools & ultra‑Orthodox institutions)
- Cultural mediators and social workers

## Problem
### Pain Point
Significant barriers in communication between cultural groups due to differences in language, tone, and preferred communication tools (e.g., email vs. WhatsApp). This often leads to misunderstandings, delays, or complete message breakdowns.

### Evidence
Real‑life cases of miscommunication between sectors such as the national‑religious (“Mamad”) and ultra‑Orthodox (“Beit Yaakov”) communities, particularly in educational and family‑related contexts.

## Solution & Value
### Core Feature
An intelligent message‑relay service or API that translates both platform format (email ↔ WhatsApp) and cultural‑linguistic context. It ensures tone, intent, and structure match the recipient’s cultural norms and communication style.

### Key Outcome Metrics
- Reduction in misunderstandings
- Improved response rates
- Enhanced trust between communities

### Why This Is Better
Not just a technical bridge — it includes human‑aware, context‑sensitive mediation. Unlike typical chatbots or translation tools, this focuses on cultural accuracy and emotional tone, not just literal meaning.

## 🚀 Git Flow – Team Setup

### Branch Strategy

| Branch      | Purpose                                          |
|-------------|--------------------------------------------------|
| `main`      | Production‑ready code (only merged via PR)       |
| `dev`       | Integration branch for completed features        |
| `feature/*` | Individual developer tasks or experiments        |

## ✅ 1. Break the Project into Clear Components

| Area                   | Task Owner | Responsibility                                                                   |
|------------------------|-----------|----------------------------------------------------------------------------------|
| 🔗 **Gmail Integration**    | Dev A      | Authenticate to Gmail, poll for new emails, parse them, send replies            |
| 📲 **WhatsApp Integration** | Dev B      | Set up WhatsApp Cloud API, send/receive messages, handle webhook                |
| 🧠 **Message Routing & Server** | Dev C      | Bridge between Gmail & WhatsApp, map users, log messages, deploy API            |

## ✅ 2. Task Breakdown per Developer

### 👨‍💻 Dev A – Gmail Handler
- Set up OAuth2 with Gmail API  
- Watch for new emails from specific sender (polling or Gmail watch)  
- Parse subject/body and reply to messages  
- Provide API endpoints: `GET /email-inbox`, `POST /send-email`  

### 👩‍💻 Dev B – WhatsApp Handler
- Set up Meta Developer Account & App  
- Configure WhatsApp Cloud API (token, test number, phone ID)  
- Send message to number using REST API  
- Set up webhook to receive incoming WhatsApp messages  
- Provide API endpoints: `POST /send-whatsapp`, webhook `POST /webhook`  

### 👨‍💻 Dev C – Server + Router
- Build small Express / FastAPI app  
- Maintain map of Gmail ↔ WhatsApp user (in‑memory or JSON file)  
- Connect Dev A and Dev B services  
- Log each message direction for debugging  
- *Optional*: simple frontend/log viewer  

## ✅ 3. Recommended Workflow
- Use GitHub with a `main` branch and short‑lived feature branches  
- Use Discord/Slack to stay synced  
- Keep messages short and frequent (“email from A received”, “sent to B”)  

> **Next steps:** Explore limitations of Gmail and WhatsApp APIs.  
> Sign up for the necessary services (Gmail account & WhatsApp Business).

---

# 🧱 Tech Stack Breakdown

## 🔙 Backend (Core API + Routing)
| Item       | Choice                            |
|------------|-----------------------------------|
| **Language** | Python **or** Node.js (quick prototyping) |
| **Framework** | Python: FastAPI / Flask<br>Node.js: Express.js |
| **Runtime** | Docker (optional, for easy deployment/sharing) |
| **API Type** | RESTful |

## 📥 Gmail Integration
| Item   | Choice |
|--------|--------|
| **Service** | Gmail API |
| **Auth** | OAuth2 (Google Cloud Console) |
| **Library** | Python: `google-api-python-client`<br>Node.js: `googleapis` |

## 📲 WhatsApp Integration
| Item   | Choice |
|--------|--------|
| **Service** | WhatsApp Business Cloud API |
| **Transport** | HTTPS webhooks + REST API |
| **Auth** | Permanent token (Meta Dev Console) |
| **Tooling** | Postman for quick tests, `axios` / `requests` in code |

## 🧠 Message Routing / Processing
| Item   | Choice |
|--------|--------|
| **State Storage** | PoC: JSON file or in‑memory map<br>Scale: Firebase, SQLite, or PostgreSQL |
| **Data Mapping** | user‑email ↔ WhatsApp number |

## 🛠 DevOps / CI (Optional for Hackathon)
| Item   | Choice |
|--------|--------|
| **Version Control** | Git + GitHub |
| **CI** | GitHub Actions (tests, lint, validate) |
| **Hosting** | Fast: Render, Railway, or Fly.io<br>Manual: VPS (e.g., DigitalOcean), `ngrok` for webhook testing |

## 🌍 Optional Dashboard / Log Viewer
| Item | Choice |
|------|--------|
| **Frontend Framework** | Next.js, React, **or** plain HTML |
| **UI Library** | TailwindCSS **or** Bootstrap |

---

*Prepared for fast Proof‑of‑Concept development by a small team.*
