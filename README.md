# AI-Powered Cloud Reliability & Auto-Healing Platform

## Overview

The AI-Powered Cloud Reliability & Auto-Healing Platform is a cloud-native DevOps project designed to demonstrate modern application deployment, monitoring, and automated incident response. It integrates industry-standard tools to build a reliable, observable, and scalable application while showcasing DevOps best practices, containerization, orchestration, CI/CD, Infrastructure as Code (IaC), and AI-assisted operations.

## Current Features

- ✅ Flask REST API
- ✅ Health Check Endpoint (`/health`)
- ✅ Error Simulation Endpoint (`/simulate-error`)
- ✅ Prometheus Metrics Endpoint (`/metrics`)
- ✅ Unit Testing with Pytest
- ✅ Git & GitHub Version Control

## Tech Stack

- Python
- Flask
- Pytest
- Prometheus Client
- Git
- GitHub

## Project Structure

```text
ai-cloud-reliability-platform/
│
├── application/
│   ├── app.py
│   ├── requirements.txt
│   └── tests/
├── docs/
├── Dockerfile
├── README.md
├── LICENSE
└── .gitignore
```

## Run Locally
```bash
pip install -r application/requirements.txt
python application/app.py
```
Run tests:

```bash
pytest application/tests -v
```
### Without Docker

```bash
pip install -r application/requirements.txt
python application/app.py
```
### With Docker

```bash
docker build -t ai-cloud-reliability-app .
docker run -p 5000:5000 ai-cloud-reliability-app
```

## Roadmap

- ✅ Flask Application
- ✅ Docker Containerization
- ⏳ Kubernetes
- ⏳ Prometheus & Grafana
- ⏳ Loki Logging
- ⏳ AI Incident Analyzer
- ⏳ Jenkins CI/CD
- ⏳ Terraform
- ⏳ AWS Deployment

## License

MIT License

