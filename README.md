# 🚀 FastAPI Monitoring Microservice – M.Tech DevOps for Cloud Assignment

This is a lightweight FastAPI-based microservice developed as part of an M.Tech assignment for the subject *DevOps for Cloud*. It demonstrates containerized deployment, configuration management, networking, and monitoring using Kubernetes, Docker, and Prometheus – fully compatible with Apple Silicon (MacBook Pro 2022).

---

## 📌 Application Description

This microservice provides two endpoints:

- `GET /get_info`: Returns metadata such as app version, title, environment, and pod hostname.
- `GET /metrics`: Exposes Prometheus-compatible metrics for request tracking and monitoring.

Environment variables are injected via Kubernetes ConfigMap to follow 12-factor app principles.

---

## 🧱 Tech Stack

| Layer             | Technology                         |
|------------------|-------------------------------------|
| Backend Framework| FastAPI                             |
| Server           | Uvicorn                             |
| Metrics Exporter | prometheus_fastapi_instrumentator   |
| Containerization | Docker                              |
| Orchestration    | Kubernetes (Minikube)               |
| Monitoring       | Prometheus                          |
| Config Management| Kubernetes ConfigMap                |
| Platform         | macOS (Apple Silicon)               |

---

## 📁 Project Structure

```

app-2023mt03575/
├── main.py
├── Dockerfile
├── .env
├── .dockerignore
├── k8s/
│   ├── config-2023mt03575.yaml
│   ├── deployment-2023mt03575.yaml
│   ├── service-2023mt03575.yaml
│   └── metrics-service.yaml

````

---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites

- Docker Desktop
- Minikube (with Docker driver)
- kubectl
- Helm (for Prometheus)

### 2️⃣ Start Minikube

```bash
minikube start --driver=docker
````

### 3️⃣ Build Docker Image *inside* Minikube

```bash
eval $(minikube docker-env)
docker build -t img-2023mt03575 .
```

### 4️⃣ Apply Kubernetes Configs

```bash
kubectl apply -f k8s/config-2023mt03575.yaml
kubectl apply -f k8s/deployment-2023mt03575.yaml
kubectl apply -f k8s/service-2023mt03575.yaml
```

### 5️⃣ Access the App

```bash
minikube service service-2023mt03575
```

> Navigate to `/get_info` to verify app is running.

---

## 📊 Prometheus Monitoring Setup

### 🔧 Install Prometheus via Helm

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/prometheus --namespace monitoring --create-namespace --set server.service.type=NodePort
```

### 🔍 View Prometheus UI

```bash
minikube service prometheus-server -n monitoring
```

> Use the UI to search metrics like:
>
> * `http_requests_total`
> * `container_cpu_usage_seconds_total`
> * `container_memory_usage_bytes`

---

## 📈 Metrics Captured

* Request count to `/get_info`
* CPU and memory usage per replica
* Auto-generated latency/histogram metrics via `prometheus_fastapi_instrumentator`

---

## 📌 Observed Load Balancing

* Service of type `NodePort` routes traffic to 2 pod replicas.
* Repeated `/get_info` requests return different `HOSTNAME` values.
* Logs and Prometheus confirm round-robin distribution.

---

## 🛠️ Troubleshooting

| Issue                     | Fix                                                          |
| ------------------------- | ------------------------------------------------------------ |
| `ImagePullBackOff`        | Use `imagePullPolicy: Never` and build image inside Minikube |
| Cannot access `/get_info` | Ensure correct port mapping and FastAPI is running           |
| Prometheus not scraping   | Restart Prometheus or ensure scrape target matches service   |

---

## 🧠 Author & Metadata

* **Name**: Syed Mustafa Haider
* **BITS ID**: 2023MT03575
* **Assignment**: M.Tech – DevOps for Cloud
* **Date**: May 2025

---
