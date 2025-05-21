# CultureBridge - Technical Specification Document

## Project Overview
CultureBridge is a multi-platform communication bridge service designed to connect WhatsApp, Google chat, and SMS, providing seamless message translation and adaptation across different platforms and cultural contexts.

### One-Line Pitch
A communication bridge service that translates and adapts messages between WhatsApp, Google chat, and SMS platforms, ensuring cultural context and tone are preserved across all channels.

## Target Users
1. Parents from diverse communities
2. Educators and school staff (public schools & ultra-Orthodox institutions)
3. Cultural mediators and social workers
4. Community organizations
5. Healthcare providers

## Problem Statement

### Pain Points
- Communication barriers between cultural groups due to:
  - Language differences
  - Tone variations
  - Preferred communication tools (WhatsApp vs Google chat vs SMS)
  - Platform limitations
- Results in:
  - Misunderstandings
  - Delays
  - Complete message breakdowns
  - Missed communications

### Evidence
Real-world cases of miscommunication between sectors such as:
- National-religious ("Mamad") communities
- Ultra-Orthodox ("Beit Yaakov") communities
- Particularly in educational, healthcare, and family-related contexts

## Solution & Value Proposition

### Core Features
- Multi-platform message bridge service that:
  - Connects WhatsApp, Google chat, and SMS platforms
  - Translates and adapts messages to appropriate cultural context
  - Maintains conversation threads across platforms
  - Handles platform-specific features (attachments, media, etc.)
  - Ensures tone, intent, and structure match recipient's cultural norms
  - Maintains communication style appropriateness
  - Provides delivery status tracking
  - Supports group conversations

### Key Outcome Metrics
1. Reduction in misunderstandings
2. Improved response rates
3. Enhanced trust between communities
4. Number of successful message translations
5. User satisfaction ratings
6. Platform coverage statistics
7. Message delivery success rates

### Competitive Advantage
- Human-aware, context-sensitive mediation
- Focus on cultural accuracy and emotional tone
- Beyond literal translation
- Seamless multi-platform integration
- Automated cultural adaptation
- Platform-agnostic message handling
- Unified communication experience

## Technical Architecture

### Development Workflow
#### Git Flow Strategy
- `main`: Production-ready code (PR-only merges)
- `dev`: Integration branch for completed features
- `feature/*`: Individual developer tasks/experiments

### Component Breakdown

#### 1. Platform Integrations
##### WhatsApp Integration
- Meta Developer Account & App setup
- WhatsApp Cloud API configuration
- Message receiving and processing
- Media handling
- Group chat support
- API Endpoints:
  - POST /webhook (incoming messages)
  - POST /send-whatsapp
  - GET /whatsapp-status

##### Google chat Integration
- Google Chat API integration
- Message sending and receiving
- Attachment handling
- Thread management
- API Endpoints:
  - POST /send-chat
  - GET /chat-status
  - POST /chat-webhook

##### SMS Integration
- Twilio API integration
- Message sending and receiving
- Delivery status tracking
- API Endpoints:
  - POST /send-sms
  - GET /sms-status
  - POST /sms-webhook

#### 2. Core Service
Responsibilities:
- FastAPI application development
- User mapping (WhatsApp ↔ Google chat ↔ SMS)
- Service integration
- Message logging
- Cultural context database
- Translation service integration
- Message routing
- API Endpoints:
  - GET /health
  - GET /stats
  - POST /configure
  - GET /platform-status

### Technical Stack

#### Backend (Core API + Services)
- Language: Python
- Framework: FastAPI
- Runtime: Docker
- API Type: RESTful

#### Platform Integrations
##### WhatsApp
- Service: WhatsApp Business Cloud API (Meta)
- Transport: HTTPS webhooks + REST API
- Authentication: Permanent token (Meta Dev Console)
- Libraries:
  - python-whatsapp-sdk
  - requests

##### Google chat
- Service: Google Chat API
- Authentication: OAuth2 (Google Cloud Console)
- Libraries:
  - google-api-python-client
  - python-dotenv

##### SMS
- Service: Twilio API
- Authentication: Account SID + Auth Token
- Libraries:
  - twilio
  - requests

#### Message Processing
- State Storage:
  - Development: SQLite
  - Production: PostgreSQL
- Data Mapping: user-platform ↔ platform
- Translation Service: Google Cloud Translation API
- Cultural Context: Custom database
- Message Queue: Redis

#### DevOps/CI
- Version Control: Git + GitHub
- CI: GitHub Actions
- Hosting: Railway/Fly.io
- Development: ngrok for webhook testing

#### Monitoring & Logging
- Application Logs: Python logging
- Error Tracking: Sentry
- Performance Monitoring: Prometheus + Grafana
- Platform Status Monitoring: Custom dashboard

## Development Guidelines
1. Use GitHub with main branch and short-lived feature branches
2. Maintain communication via Discord/Slack
3. Keep messages concise and frequent
4. Document all API endpoints and integration points
5. Implement proper error handling and logging
6. Follow security best practices for API keys and authentication
7. Write unit tests for all components
8. Maintain comprehensive documentation
9. Implement platform-specific error handling
10. Ensure message delivery tracking

## Next Steps
1. Set up development environment
2. Create necessary accounts:
   - WhatsApp Business API
   - Google Chat API access
   - Twilio API access
3. Initialize project repository
4. Implement platform integrations in parallel
5. Develop core routing service
6. Implement cultural context processing
7. Set up monitoring and logging
8. Deploy to production
9. Regular integration testing
10. Documentation updates 