# CultureBridge - Technical Specification Document

## Project Overview
CultureBridge is a communication service designed to bridge cultural and digital divides by providing seamless message translation and adaptation across different platforms and cultural contexts.

### One-Line Pitch
A communication service that translates and bridges messages across cultural and digital divides — e.g., from email to WhatsApp, adapted to tone and context.

## Target Users
1. Parents from diverse communities
2. Educators and school staff (public schools & ultra-Orthodox institutions)
3. Cultural mediators and social workers

## Problem Statement

### Pain Points
- Communication barriers between cultural groups due to:
  - Language differences
  - Tone variations
  - Preferred communication tools (e.g., email vs. WhatsApp)
- Results in:
  - Misunderstandings
  - Delays
  - Complete message breakdowns

### Evidence
Real-world cases of miscommunication between sectors such as:
- National-religious ("Mamad") communities
- Ultra-Orthodox ("Beit Yaakov") communities
- Particularly in educational and family-related contexts

## Solution & Value Proposition

### Core Features
- Intelligent message relay service/API that:
  - Translates platform format (email ↔ WhatsApp)
  - Adapts cultural-linguistic context
  - Ensures tone, intent, and structure match recipient's cultural norms
  - Maintains communication style appropriateness

### Key Outcome Metrics
1. Reduction in misunderstandings
2. Improved response rates
3. Enhanced trust between communities

### Competitive Advantage
- Human-aware, context-sensitive mediation
- Focus on cultural accuracy and emotional tone
- Beyond literal translation

## Technical Architecture

### Development Workflow
#### Git Flow Strategy
- `main`: Production-ready code (PR-only merges)
- `dev`: Integration branch for completed features
- `feature/*`: Individual developer tasks/experiments

### Component Breakdown

#### 1. Gmail Integration (Dev A)
Responsibilities:
- OAuth2 setup with Gmail API
- Email monitoring (polling/Gmail watch)
- Message parsing (subject/body)
- Reply handling
- API Endpoints:
  - GET /email-inbox
  - POST /send-email

#### 2. WhatsApp Integration (Dev B)
Responsibilities:
- Meta Developer Account & App setup
- WhatsApp Cloud API configuration
- Message sending via REST API
- Webhook implementation
- API Endpoints:
  - POST /send-whatsapp
  - POST /webhook (incoming messages)

#### 3. Server & Router (Dev C)
Responsibilities:
- Express/FastAPI application development
- User mapping (Gmail ↔ WhatsApp)
- Service integration
- Message logging
- Optional frontend/log viewer

### Technical Stack

#### Backend (Core API + Routing)
- Language Options:
  - Python (FastAPI/Flask)
  - Node.js (Express.js)
- Runtime: Docker (optional)
- API Type: RESTful

#### Gmail Integration
- Service: Gmail API
- Authentication: OAuth2 (Google Cloud Console)
- Libraries:
  - Python: google-api-python-client
  - Node.js: googleapis

#### WhatsApp Integration
- Service: WhatsApp Business Cloud API (Meta)
- Transport: HTTPS webhooks + REST API
- Authentication: Permanent token (Meta Dev Console)
- Tools: Postman, axios/requests

#### Message Routing/Processing
- State Storage:
  - PoC: JSON file/in-memory map
  - Production: Firebase/SQLite/PostgreSQL
- Data Mapping: user-email ↔ WhatsApp number

#### DevOps/CI (Optional)
- Version Control: Git + GitHub
- CI: GitHub Actions
- Hosting Options:
  - Quick: Render/Railway/Fly.io
  - Manual: VPS (DigitalOcean)
  - Development: ngrok for webhook testing

#### Optional Dashboard/Log Viewer
- Frontend Options:
  - Next.js
  - React
  - Plain HTML
- UI Libraries:
  - TailwindCSS
  - Bootstrap

## Development Guidelines
1. Use GitHub with main branch and short-lived feature branches
2. Maintain communication via Discord/Slack
3. Keep messages concise and frequent
4. Document all API endpoints and integration points
5. Implement proper error handling and logging
6. Follow security best practices for API keys and authentication

## Next Steps
1. Set up development environment
2. Create necessary accounts:
   - Gmail API access
   - WhatsApp Business API
3. Initialize project repository
4. Begin component development in parallel
5. Regular integration testing
6. Documentation updates 