# Automated CI/CD Pipeline for Containerized Application Deployment

## 📌 Overview

This project demonstrates an end-to-end **DevOps CI/CD workflow** for automatically testing, containerizing, deploying, and monitoring a Python web application.

The pipeline integrates **GitHub, Jenkins, Docker, Kubernetes, Prometheus, and Grafana** to automate application delivery and provide monitoring visibility.

---

## 🏗️ Architecture

```text
                  Developer
                      │
                      ▼
                 ┌─────────┐
                 │ GitHub  │
                 └────┬────┘
                      │
                      ▼
                 ┌─────────┐
                 │ Jenkins │
                 └────┬────┘
                      │
             ┌────────┼─────────┐
             ▼        ▼         ▼
          Checkout  Testing   Build
             │        │         │
             └────────┼─────────┘
                      ▼
                 ┌─────────┐
                 │ Docker  │
                 └────┬────┘
                      │
                      ▼
                ┌───────────┐
                │ Kubernetes│
                └─────┬─────┘
                      │
              ┌───────┴────────┐
              ▼                ▼
         Application       Monitoring
                              │
                       ┌──────┴──────┐
                       ▼             ▼
                  Prometheus      Grafana
```

---

## 🚀 Features

* Automated CI/CD pipeline
* GitHub source control
* Jenkins pipeline automation
* Automated unit testing
* Docker containerization
* Kubernetes deployment
* Kubernetes health checks
* Readiness and liveness probes
* Prometheus metrics
* Grafana monitoring configuration
* Docker Compose development environment
* Linux shell automation
* Environment-based configuration

---

## 🛠️ Technologies

| Technology | Purpose                 |
| ---------- | ----------------------- |
| Python     | Application development |
| Flask      | Web application         |
| Git/GitHub | Source control          |
| Jenkins    | CI/CD automation        |
| Docker     | Containerization        |
| Kubernetes | Container orchestration |
| Prometheus | Metrics monitoring      |
| Grafana    | Visualization           |
| Pytest     | Automated testing       |
| Linux/Bash | Automation              |

---

## 📂 Project Structure

```text
devops-cicd-pipeline/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── docker/
│   └── Dockerfile
│
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── servicemonitor.yaml
│   └── kustomization.yaml
│
├── monitoring/
│   ├── prometheus/
│   │   └── prometheus.yml
│   └── grafana/
│       ├── datasource.yaml
│       └── dashboard-provider.yaml
│
├── scripts/
│   ├── build.sh
│   └── test.sh
│
├── tests/
│   └── test_app.py
│
├── Jenkinsfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

---

## ⚙️ Requirements

Install:

* Python 3.10+
* Git
* Docker
* Jenkins
* Kubernetes
* kubectl

For local Kubernetes testing, you can use:

* Minikube
* Kind
* Docker Desktop Kubernetes

---

## ▶️ Run the Application Locally

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r app/requirements.txt
```

Start the application:

```bash
python app/app.py
```

The application runs on:

```text
http://localhost:5000
```

---

## 🧪 Run Tests

```bash
pytest -q
```

The test suite validates:

* Application endpoint
* Health endpoint
* Readiness endpoint
* Prometheus metrics endpoint

---

## 🐳 Docker

Build the image:

```bash
docker build -f docker/Dockerfile -t devops-demo:1.0 .
```

Run the container:

```bash
docker run -p 5000:5000 devops-demo:1.0
```

Open:

```text
http://localhost:5000
```

---

## 🐳 Docker Compose

Start the complete local environment:

```bash
docker compose up --build
```

Services:

```text
Application → http://localhost:5000

Prometheus  → http://localhost:9090

Grafana     → http://localhost:3000
```

Default development Grafana credentials:

```text
Username: admin
Password: admin
```

These credentials should be changed before any non-local deployment.

---

## ☸️ Kubernetes Deployment

Apply the Kubernetes configuration:

```bash
kubectl apply -k k8s/
```

Check the pods:

```bash
kubectl get pods -n devops-demo
```

Check the service:

```bash
kubectl get services -n devops-demo
```

Check application logs:

```bash
kubectl logs -n devops-demo deployment/devops-demo
```

Access the application locally:

```bash
kubectl port-forward -n devops-demo service/devops-demo 8080:80
```

Then open:

```text
http://localhost:8080
```

---

## 🔄 Jenkins CI/CD Pipeline

The `Jenkinsfile` automates the following process:

```text
GitHub Push
     ↓
Checkout
     ↓
Install Dependencies
     ↓
Run Unit Tests
     ↓
Build Docker Image
     ↓
Deploy to Kubernetes
     ↓
Verify Deployment
```

The Kubernetes deployment stage can be enabled using:

```text
DEPLOY_TO_K8S=true
```

---

## 📊 Monitoring

The application exposes Prometheus metrics through:

```text
/metrics
```

Example metrics include:

```text
http_requests_total
http_request_latency_seconds
```

Prometheus collects these metrics and Grafana can visualize them.

This allows monitoring of:

* Request volume
* Application latency
* Application availability
* Service health

---

## 🔐 DevOps Security Practices

For production environments, the following improvements are recommended:

* Store credentials in Jenkins Credentials Manager
* Use Kubernetes Secrets
* Never commit passwords or API keys
* Use private container registries
* Scan Docker images for vulnerabilities
* Use TLS
* Implement Kubernetes RBAC
* Add network policies
* Run containers as non-root users
* Pin production dependencies

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* CI/CD
* Git/GitHub
* Jenkins
* Docker
* Kubernetes
* Prometheus
* Grafana
* Linux
* Bash scripting
* Automated testing
* Containerization
* Infrastructure automation
* Application monitoring

---

## 👨‍💻 Author

**GOGU Sai Varshith**

Computer Science and Engineering
KL University

---

## 📜 License

MIT License
