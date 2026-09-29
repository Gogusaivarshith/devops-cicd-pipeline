# Automated CI/CD Pipeline for Containerized Application

A portfolio-ready DevOps project demonstrating an end-to-end CI/CD workflow using **GitHub, Jenkins, Docker, Kubernetes, Prometheus, Grafana, Python, and Linux**.

## Architecture

```text
                 ┌──────────────┐
                 │    GitHub     │
                 └──────┬───────┘
                        │ webhook / checkout
                        ▼
                 ┌──────────────┐
                 │    Jenkins    │
                 │ CI/CD Pipeline│
                 └──────┬───────┘
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
       Run Unit Tests        Build Docker Image
                                   │
                                   ▼
                           Deploy to Kubernetes
                                   │
                     ┌─────────────┴─────────────┐
                     ▼                           ▼
              Application                  Monitoring
                     │                    Prometheus
                     │                         │
                     └─────────────────────────┤
                                               ▼
                                            Grafana
```

## What the project demonstrates

- Git-based source control
- Automated CI/CD with Jenkins
- Automated unit testing
- Docker image creation
- Kubernetes Deployment and Service
- Kubernetes health/readiness probes
- Prometheus application metrics
- Grafana dashboard provisioning
- Linux/shell automation
- Configuration through environment variables
- Reproducible local development

## Technology Stack

| Technology | Purpose |
|---|---|
| Python + Flask | Demo application |
| pytest | Automated tests |
| Git/GitHub | Source control |
| Jenkins | CI/CD automation |
| Docker | Containerization |
| Kubernetes | Container orchestration |
| Prometheus | Metrics collection |
| Grafana | Monitoring/dashboarding |
| Linux + Bash | Automation |

## Project Structure

```text
devops-cicd-pipeline/
├── app/
│   ├── app.py
│   └── requirements.txt
├── tests/
│   └── test_app.py
├── docker/
│   └── Dockerfile
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── servicemonitor.yaml
│   └── kustomization.yaml
├── monitoring/
│   ├── prometheus/
│   │   └── prometheus.yml
│   └── grafana/
│       ├── datasource.yaml
│       └── dashboard-provider.yaml
├── scripts/
│   ├── test.sh
│   └── build.sh
├── Jenkinsfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

## Application

The Flask service exposes:

- `GET /` — application information
- `GET /health` — liveness/health endpoint
- `GET /ready` — readiness endpoint
- `GET /metrics` — Prometheus metrics

## Run Locally

### Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
python app/app.py
```

Open:

```text
http://localhost:5000
```

### Run tests

```bash
pip install pytest
pytest -q
```

### Docker

```bash
docker build -f docker/Dockerfile -t devops-demo:1.0 .
docker run -p 5000:5000 devops-demo:1.0
```

### Docker Compose

```bash
docker compose up --build
```

Application:

```text
http://localhost:5000
```

Prometheus:

```text
http://localhost:9090
```

Grafana:

```text
http://localhost:3000
```

The local Grafana configuration uses the default development credentials:

```text
username: admin
password: admin
```

Change these credentials for any non-local deployment.

## Kubernetes

This repository uses Kubernetes manifests that can be tested with Minikube, Kind, Docker Desktop Kubernetes, or a suitable cluster.

Create the namespace and deploy:

```bash
kubectl apply -k k8s/
```

Check resources:

```bash
kubectl get pods -n devops-demo
kubectl get services -n devops-demo
```

Check application logs:

```bash
kubectl logs -n devops-demo deployment/devops-demo
```

Port-forward locally:

```bash
kubectl port-forward -n devops-demo service/devops-demo 8080:80
```

Then open:

```text
http://localhost:8080
```

## Jenkins Pipeline

The `Jenkinsfile` implements:

1. Checkout
2. Install dependencies
3. Unit tests
4. Docker image build
5. Kubernetes deployment

Set these Jenkins environment variables/credentials according to your environment:

```text
DOCKER_IMAGE
KUBE_CONTEXT
```

For a real registry deployment, authenticate Jenkins with your container registry and replace the placeholder image configuration.

## CI/CD Flow

```text
git push
   ↓
Jenkins webhook
   ↓
Checkout
   ↓
Install dependencies
   ↓
pytest
   ↓
Docker build
   ↓
Push image to registry
   ↓
kubectl apply
   ↓
Kubernetes rolling deployment
   ↓
Health/readiness verification
```

## Monitoring

Prometheus scrapes the application's `/metrics` endpoint.

Useful metrics include:

```text
http_requests_total
http_request_latency_seconds
```

Grafana can then visualize request traffic and application health.

## Security Notes

This repository is designed as a learning/portfolio project. For production use:

- Use a private image registry and credentials store.
- Never commit passwords, API keys, or cloud credentials.
- Use Kubernetes Secrets for sensitive values.
- Pin dependency versions.
- Use non-root containers where practical.
- Add image vulnerability scanning.
- Add RBAC and network policies.
- Use TLS for external traffic.
- Protect Jenkins and Grafana with strong authentication.

## Resume Description

**Automated CI/CD Pipeline for Containerized Application Deployment** — Built an end-to-end DevOps pipeline using **Jenkins, Docker, Kubernetes, GitHub, Prometheus, and Grafana**. Automated testing, Docker image builds, and Kubernetes deployments through CI/CD, implemented health/readiness probes and application metrics, and configured monitoring dashboards for application and infrastructure visibility.

## GitHub

```bash
git init
git add .
git commit -m "Initial commit: DevOps CI/CD pipeline"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/devops-cicd-pipeline.git
git push -u origin main
```
