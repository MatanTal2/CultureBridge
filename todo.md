# CultureBridge: WhatsApp <-> Google Chat Bridge - TODO List

This document outlines the tasks required to build, test, and deploy the WhatsApp to Google Chat communication bridge.

## Phase 0: Project Setup & Foundations (Common for all bridges)

*   **[CORE]**
    *   [ ] [P1] Initialize Git repository with `main` and `dev` branches.
    *   [ ] [P1] Set up basic Python project structure (FastAPI).
        *   [ ] `src/` directory with `main.py`, `core/`, `models/`, `schemas/`, `services/`, `adapters/`.
        *   [ ] `tests/` directory.
    *   [ ] [P1] Configure `requirements.txt` (or `pyproject.toml` with Poetry/PDM).
        *   [ ] `fastapi`, `uvicorn`, `pydantic`, `python-dotenv`, `requests`
        *   [ ] `sqlalchemy` (for ORM), `psycopg2-binary` (PostgreSQL), `alembic` (migrations)
        *   [ ] `redis` (for message queue)
    *   [ ] [P1] Set up Dockerfile and `docker-compose.yml` for local development (FastAPI app, PostgreSQL, Redis).
    *   [ ] [P1] Implement basic health check endpoint (`GET /health`).
    *   [ ] [P2] Set up pre-commit hooks (e.g., black, flake8, isort).
    *   [ ] [P2] Set up basic CI pipeline (GitHub Actions) for linting and running tests.
*   **[ACCOUNTS & KEYS]**
    *   [ ] [P1] Create/configure Meta Developer Account & WhatsApp Business App.
        *   [ ] Obtain Permanent Access Token.
        *   [ ] Set up a test phone number.
        *   [ ] Note App ID, App Secret, WhatsApp Business Account ID.
    *   [ ] [P1] Create/configure Google Cloud Project & Google Chat API.
        *   [ ] Enable Google Chat API.
        *   [ ] Set up OAuth 2.0 credentials (Service Account recommended for server-to-server).
        *   [ ] Note Project ID, Service Account key file.
    *   [ ] [P1] Create Google Cloud Translation API credentials.
    *   [ ] [P1] Set up `.env` file for storing secrets locally and document environment variables needed for production.
    *   [ ] [P2] Implement a secure way to manage secrets in production (e.g., HashiCorp Vault, cloud provider's secret manager).

## Phase 1: WhatsApp Adapter Implementation

*   **[WHATSAPP_ADAPTER]** `src/adapters/whatsapp_adapter.py`
    *   [ ] [P1] **Configuration:** Load WhatsApp API token and other necessary IDs from environment variables.
    *   [ ] [P1] **Send Message Functionality:**
        *   [ ] Implement `send_text_message(to_phone_number: str, message_body: str)`.
        *   [ ] Implement `send_media_message(to_phone_number: str, media_url: str, media_type: str, caption: Optional[str])` (initially for images).
        *   [ ] Handle API responses and errors from Meta API.
        *   [ ] Logging for sent messages and API responses.
    *   [ ] [P1] **Receive Message Webhook:**
        *   [ ] Create FastAPI endpoint (`POST /webhooks/whatsapp`) to receive incoming messages from Meta.
        *   [ ] Implement webhook verification (using app secret).
        *   [ ] Parse incoming message payload (text, media, sender info, message ID).
        *   [ ] Acknowledge receipt to Meta API (HTTP 200).
        *   [ ] Logging for received messages.
    *   [ ] [P2] **Media Handling:**
        *   [ ] Logic to download incoming media from WhatsApp (if necessary for processing/forwarding).
        *   [ ] Logic to upload media to a temporary store if direct forwarding isn't possible.
    *   [ ] [P2] **Status Updates:** Implement handling for message status webhooks (sent, delivered, read).
    *   [ ] [P3] **Interactive Messages/Templates (Future):** Stub out or plan for handling.
*   **[TESTING_WHATSAPP]**
    *   [ ] [P1] Set up `ngrok` or similar for local webhook testing.
    *   [ ] [P1] Unit tests for `send_text_message` (mocking `requests`).
    *   [ ] [P1] Manual E2E test: Send a message via API call, receive it on a test WhatsApp account.
    *   [ ] [P1] Manual E2E test: Send a message from test WhatsApp account, verify it's received by the webhook and parsed.
    *   [ ] [P2] Unit tests for webhook payload parsing.

## Phase 2: Google Chat Adapter Implementation

*   **[GCHAT_ADAPTER]** `src/adapters/gchat_adapter.py`
    *   [ ] [P1] **Configuration:** Load Google Chat API credentials (service account JSON path) from environment variables.
    *   [ ] [P1] **Authentication:** Implement Google Chat API authentication using `google-api-python-client` with service account.
    *   [ ] [P1] **Send Message Functionality:**
        *   [ ] Implement `send_text_message(space_id: str, message_body: str, thread_key: Optional[str])`.
        *   [ ] Implement `send_attachment_message(space_id: str, attachment_url: str, attachment_name: str, thread_key: Optional[str])` (initially for images).
        *   [ ] Handle API responses and errors from Google Chat API.
        *   [ ] Logging for sent messages and API responses.
    *   [ ] [P1] **Receive Message Webhook:**
        *   [ ] Create FastAPI endpoint (`POST /webhooks/googlechat`) to receive incoming messages from Google Chat (requires setting up Pub/Sub or direct webhook).
        *   [ ] Parse incoming event payload (text, attachments, sender info, space ID, thread ID).
        *   [ ] Acknowledge receipt (HTTP 200).
        *   [ ] Logging for received messages.
    *   [ ] [P2] **Thread Management:** Logic to correctly reply in threads or start new ones.
    *   [ ] [P2] **Attachment Handling:** Logic to handle incoming attachments (downloading if necessary).
*   **[TESTING_GCHAT]**
    *   [ ] [P1] Set up a test Google Chat space.
    *   [ ] [P1] Unit tests for `send_text_message` (mocking Google API client).
    *   [ ] [P1] Manual E2E test: Send a message via API call, receive it in the test Google Chat space.
    *   [ ] [P1] Manual E2E test: Send a message in the test Google Chat space, verify it's received by the webhook and parsed.
    *   [ ] [P2] Unit tests for webhook payload parsing.

## Phase 3: Core Service - Bridging Logic & Data Models

*   **[CORE_MODELS]** `src/models/`
    *   [ ] [P1] Define SQLAlchemy models:
        *   [ ] `User` (CultureBridge system user, not platform user).
        *   [ ] `PlatformAccount` (stores WhatsApp numbers, Google Chat space/user IDs, linked to `User`). Fields: `id`, `user_id`, `platform_type (ENUM)`, `platform_identifier`, `metadata (JSONB)`.
        *   [ ] `BridgeConfiguration` (links two `PlatformAccount`s). Fields: `id`, `source_platform_account_id`, `target_platform_account_id`, `is_active`, `source_language`, `target_language`, `source_cultural_profile_id`, `target_cultural_profile_id`, `config_options (JSONB)`.
        *   [ ] `MessageLog` (for auditing).
        *   [ ] `CulturalProfile` (stores rules/name for a cultural context). Fields: `id`, `name`, `description`, `rules (JSONB)`.
    *   [ ] [P1] Set up Alembic for database migrations.
    *   [ ] [P1] Create initial migration.
*   **[CORE_SCHEMAS]** `src/schemas/` (Pydantic models for API I/O)
    *   [ ] [P1] Schemas for `User`, `PlatformAccount`, `BridgeConfiguration`, `CulturalProfile` (Create, Read, Update).
*   **[CORE_API_ENDPOINTS]** `src/main.py` or `src/api/endpoints/`
    *   [ ] [P2] `POST /users`: Register a new CultureBridge user.
    *   [ ] [P1] `POST /users/{user_id}/platform_accounts`: Link a platform account.
    *   [ ] [P1] `GET /users/{user_id}/platform_accounts`: List linked accounts.
    *   [ ] [P1] `POST /bridges`: Create a bridge configuration.
    *   [ ] [P1] `GET /bridges/{bridge_id}`: Get bridge details.
    *   [ ] [P2] `PUT /bridges/{bridge_id}`: Update bridge.
    *   [ ] [P2] `DELETE /bridges/{bridge_id}`: Delete bridge.
    *   [ ] [P2] `POST /cultural_profiles`: Create a cultural profile.
*   **[CORE_MESSAGE_PROCESSING]** `src/services/message_processor.py`
    *   [ ] [P1] **Message Queue Integration (Redis):**
        *   [ ] Function in adapters to push raw incoming messages (with metadata like `source_platform_identifier`, `message_content`, `media_info`) to a Redis queue.
        *   [ ] Worker process (e.g., using RQ, Celery, or custom Redis consumer) to pick messages from the queue.
    *   [ ] [P1] **Routing Logic:**
        *   [ ] In the worker:
            *   Retrieve `source_platform_identifier`.
            *   Query `BridgeConfiguration` to find active bridges for this source.
            *   For each target in the bridge:
                *   Retrieve `target_platform_account_id` and its details.
                *   Prepare message for the target platform adapter.
    *   [ ] [P1] **Basic Pass-through (No Translation/Adaptation Yet):**
        *   Logic to take a message from WhatsApp queue item and send it to the configured Google Chat target via `gchat_adapter.send_text_message`.
        *   Logic to take a message from Google Chat queue item and send it to the configured WhatsApp target via `whatsapp_adapter.send_text_message`.
    *   [ ] [P1] Logging of message processing steps.
*   **[TESTING_CORE]**
    *   [ ] [P1] Unit tests for data model interactions (CRUD operations).
    *   [ ] [P1] Unit tests for API endpoints (mocking services).
    *   [ ] [P1] Unit tests for message routing logic (mocking DB and adapters).
    *   [ ] [P2] Integration test: Full flow for WA -> GChat (text only, no translation) via queue.
    *   [ ] [P2] Integration test: Full flow for GChat -> WA (text only, no translation) via queue.

## Phase 4: Feature - Language Translation

*   **[TRANSLATION_SERVICE]** `src/services/translation_service.py`
    *   [ ] [P1] Implement `translate_text(text: str, target_language: str, source_language: Optional[str])` using Google Cloud Translation API.
    *   [ ] [P1] Handle API errors and logging.
    *   [ ] [P2] Cache translation results (e.g., in Redis) for common phrases to save costs.
*   **[CORE_MESSAGE_PROCESSING_UPDATE]**
    *   [ ] [P1] Modify `BridgeConfiguration` to include `enable_translation`, `source_language`, `target_language`.
    *   [ ] [P1] Update message processing logic: If `enable_translation` is true for the bridge, call `translation_service.translate_text` before sending to the target adapter.
*   **[TESTING_TRANSLATION]**
    *   [ ] [P1] Unit tests for `translation_service.translate_text` (mocking Google API).
    *   [ ] [P2] Integration test: WA (English) -> Translate -> GChat (Hebrew).
    *   [ ] [P2] Integration test: GChat (Hebrew) -> Translate -> WA (English).

## Phase 5: Feature - Basic Cultural Adaptation (Rule-Based)

*   **[CULTURAL_ADAPTATION_SERVICE]** `src/services/cultural_adapter_service.py`
    *   [ ] [P2] Define structure for `CulturalProfile.rules` (e.g., `{ "formality": "high", "greeting_prefix": "Dear ", "forbidden_phrases": ["lol"] }`).
    *   [ ] [P2] Implement `adapt_message(text: str, source_profile: CulturalProfile, target_profile: CulturalProfile)`:
        *   [ ] Initial simple rules: e.g., add/remove formal greetings, replace certain slang.
        *   [ ] This will be very basic initially, to be expanded later.
*   **[CORE_MESSAGE_PROCESSING_UPDATE]**
    *   [ ] [P2] Modify `BridgeConfiguration` to include `enable_cultural_adaptation`, `source_cultural_profile_id`, `target_cultural_profile_id`.
    *   [ ] [P2] Update message processing logic: If `enable_cultural_adaptation` is true, call `cultural_adapter_service.adapt_message` (after translation).
*   **[TESTING_CULTURAL_ADAPTATION]**
    *   [ ] [P2] Unit tests for `cultural_adapter_service.adapt_message` with different profiles and rules.
    *   [ ] [P3] Qualitative E2E testing: Does the adapted message "feel" right for a predefined scenario?

## Phase 6: Media & Attachment Handling Across Bridge

*   **[CORE_MESSAGE_PROCESSING_UPDATE]**
    *   [ ] [P2] **WhatsApp to Google Chat Media:**
        *   If WA message has media URL:
            *   If GChat supports direct URL embedding for that media type, use it.
            *   Else, send media URL as a text link in GChat.
    *   [ ] [P2] **Google Chat to WhatsApp Media:**
        *   If GChat message has attachment:
            *   Download attachment.
            *   If WhatsApp supports direct upload for that media type:
                *   Requires a temporary public URL or direct upload mechanism for WhatsApp. (More complex, investigate WhatsApp API capabilities for sending local files or URLs that aren't publicly accessible long-term).
                *   For now, might need to upload to a temporary public bucket and send that URL.
            *   Else, send a text message with a description and link to the attachment (if GChat provides a stable link).
*   **[TESTING_MEDIA]**
    *   [ ] [P2] E2E Test: Send image from WA -> GChat.
    *   [ ] [P2] E2E Test: Send image from GChat -> WA.
    *   [ ] [P3] Test with other media types (documents, audio) if supported by adapters.

## Phase 7: Deployment & Operations

*   **[DEVOPS]**
    *   [ ] [P2] Finalize Docker image for production.
    *   [ ] [P2] Choose hosting platform (e.g., Railway, Fly.io, AWS ECS/EKS).
    *   [ ] [P2] Set up production PostgreSQL and Redis instances.
    *   [ ] [P2] Configure environment variables on the hosting platform.
    *   [ ] [P2] Deploy application to a staging environment.
    *   [ ] [P2] Comprehensive E2E testing on staging.
    *   [ ] [P3] Set up structured logging and log aggregation (e.g., Sentry, ELK, CloudWatch Logs).
    *   [ ] [P3] Set up basic monitoring and alerting (uptime, error rates, queue depth).
    *   [ ] [P3] Deploy to production environment.
*   **[DOCUMENTATION]**
    *   [ ] [P2] Update README with setup, configuration, and deployment instructions.
    *   [ ] [P2] Ensure API documentation (FastAPI auto-generated Swagger/ReDoc) is clean and accessible.
    *   [ ] [P3] Internal documentation for developers on architecture and complex logic.

## Phase 8: Polish & Future Considerations (for this bridge)

*   [ ] [P3] Refine error handling and retry mechanisms for external API calls.
*   [ ] [P3] Investigate more robust media handling (e.g., transcoding, better temporary storage).
*   [ ] [P3] Add support for more WhatsApp message types (interactive, location).
*   [ ] [P3] Add support for more Google Chat features (cards, dialogs - may not be directly translatable but could trigger actions).
*   [ ] [P3] User interface for managing bridges and cultural profiles (separate major feature).
*   [ ] [P3] Performance optimization and load testing.

---

**Priorities:**
*   **[P1]**: Must-have for basic MVP functionality.
*   **[P2]**: Important for a usable and robust product.
*   **[P3]**: Nice-to-have or for later iterations.

**Labels/Tags:**
*   `[CORE]`
*   `[WHATSAPP_ADAPTER]`
*   `[GCHAT_ADAPTER]`
*   `[TESTING_...]`
*   `[DEVOPS]`
*   `[DOCUMENTATION]`
*   `[FEATURE_TRANSLATION]`
*   `[FEATURE_CULTURAL_ADAPT]`
*   `[FEATURE_MEDIA]`   