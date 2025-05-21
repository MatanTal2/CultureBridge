| Component                      | Recommended Tools / Languages                  |
| ------------------------------ | ---------------------------------------------- |
| Backend API                    | Python + FastAPI                               |
| Platform Integration           | WhatsApp SDK, Google API Client, Twilio SDK    |
| Translation                    | Google Cloud Translation API + optional NLP    |
| Cultural Adaptation            | Custom logic + optional LLMs (GPT/HuggingFace) |
| State Storage                  | Redis + PostgreSQL                             |
| Message Queue                  | Redis                                          |
| Containerization               | Docker                                         |
| CI/CD                          | GitHub Actions                                 |
| Hosting                        | Railway, Fly.io, or Heroku for simplicity      |
| Monitoring                     | Prometheus + Grafana + Sentry                  |
| Webhook Testing                | Ngrok                                          |
| Testing                        | Pytest, Postman, Swagger UI                    |
| (Optional) Front-End Dashboard | React + Tailwind + Next.js                     |

THE PYTHON VERSION HAS TO BE 3.11.9

pyenv install 3.11.9
pyenv global 3.11.9

python --version

output: Python 3.11.9