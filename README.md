# 🍔 DoorDash Delivery Fee Service API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This is a containerized microservice built with **FastAPI** that simulates DoorDash's delivery fee and delivery time estimation engine. It is backed by a fully automated **CI/CD Pipeline** built on **GitHub Actions**.

---

## 🗺️ Table of Contents
- [🚀 Quick Start (Local Run)](#-quick-start-local-run)
- [🔌 API Endpoints Reference](#-api-endpoints-reference)
- [🧪 Local Testing & Verification](#-local-testing--verification)
- [📦 GitHub Actions (CI/CD Pipeline)](#-github-actions-cicd-pipeline)
- [🛠️ Troubleshooting & Common Errors](#%EF%B8%8F-troubleshooting--common-errors)

---

## 🚀 Quick Start (Local Run)

Follow these commands to build and run the service locally using Docker.

### 1. Build the Docker Image
```bash
docker build -t doordash .
```

### 2. Run the Container
Choose **one** of the following options depending on your port availability:

* **Option A: Standard Port (`8080`)** (If port 8080 is free)
  ```bash
  docker run -d -p 8080:8080 --name doordash-api doordash
  ```

* **Option B: Custom Port (`8090`)** (Recommended if port 8080 is used by Apache Airflow, Tomcat, etc.)
  ```bash
  docker run -d -p 8090:8080 --name doordash-api doordash
  ```

### 3. Check App Status
Open your browser and navigate to:
* **Interactive Docs (Swagger UI):** `http://localhost:8080/docs` (or `http://localhost:8090/docs`)
* **Welcome Message:** `http://localhost:8080/` (or `http://localhost:8090/`)
* **Health Check:** `http://localhost:8080/status/` (or `http://localhost:8090/status/`)

---

## 🔌 API Endpoints Reference

### 1. Welcome Message
* **Endpoint:** `GET /`
* **Response Example:**
  ```json
  { "message": "Welcome to the DoorDash Delivery Fee Service API" }
  ```

### 2. Service Status (Health Check)
* **Endpoint:** `GET /status/`
* **Response Example:**
  ```json
  { "status": "Service is up and running" }
  ```

### 3. Estimate Delivery Time
* **Endpoint:** `GET /estimate-time/{distance_km}`
* **Response Example (`GET /estimate-time/12.3`):**
  ```json
  { "estimated_delivery_time_minutes": 71.5 }
  ```

### 4. Calculate Delivery Fee
* **Endpoint:** `POST /calculate-fee/`
* **Payload Format:**
  ```json
  {
    "distance_km": 10.5,
    "weight_kg": 2.0
  }
  ```
* **Response Example:**
  ```json
  { "delivery_fee": 21.75 }
  ```

---

## 🧪 Local Testing & Verification

You can run automated Pytest integration tests directly against your running Docker container.

### Step 1: Install Test Dependencies
```bash
pip install -r requirements-tests.txt
```

### Step 2: Set Port and Run Pytest
Choose the command set matching your terminal environment:

#### 💻 Option A: Anaconda Prompt / CMD (Windows)
```cmd
:: 1. Navigate to the project folder
cd C:\Users\Admin\Desktop\JEDHA\MLOPS\exo_CICD\doordash-copycat

:: 2. Set the port (use 8080 or 8090 depending on how you ran the container)
set API_PORT=8090

:: 3. Run pytest
pytest
```

#### 🛡️ Option B: PowerShell
```powershell
# 1. Set the port
$env:API_PORT="8090"

# 2. Run pytest
pytest
```

#### 🐧 Option C: Linux / macOS Bash
```bash
API_PORT=8090 pytest
```

---

## 📦 GitHub Actions (CI/CD Pipeline)

A robust continuous integration workflow is configured in `.github/workflows/ci.yaml`. At every `push` or `pull_request` on the `main` branch, GitHub Actions will:
1. Spin up a clean **Ubuntu** virtual environment.
2. Clone the repository.
3. **Build the Docker Image** to ensure no compilation/package errors.
4. **Run the API Container** in background mode.
5. Wait for the API to respond successfully (robust retry loop with `curl`).
6. Setup Python 3.10 and **run the entire Pytest suite** against the live Docker container.

---

## 🛠️ Troubleshooting & Common Errors

### 1. Docker Port Collision Error
> `Bind for 0.0.0.0:8080 failed: port is already allocated`
* **Cause:** Port 8080 is used by Airflow, Jenkins, or another local app.
* **Fix:** Run the container on a custom port like `8090` (see [Quick Start Option B](#-quick-start-local-run)) and configure tests with `API_PORT=8090`.

### 2. Docker Container Name Conflict
> `Conflict. The container name "/doordash-api" is already in use`
* **Cause:** An old container named `doordash-api` exists on your system.
* **Fix:** Stop and force-delete the old container:
  ```bash
  docker rm -f doordash-api
  ```

### 3. Git Email Privacy Push Rejection
> `push declined due to email privacy restrictions`
* **Cause:** Your GitHub account has e-mail privacy active, but your local Git is using your real e-mail.
* **Fix:** Configure your local Git to use your GitHub anonymous no-reply address:
  ```bash
  # 1. Set the private e-mail for this repo
  git config user.email "ID+username@users.noreply.github.com"

  # 2. Re-sign the last commit with the new e-mail
  git commit --amend --reset-author --no-edit

  # 3. Push again
  git push origin main
  ```

---

## 🧼 Cleanup Local Containers
Once you are done working or testing, run this command to stop and remove your container to free up memory and ports:
```bash
docker rm -f doordash-api
```
