# DevOpsLab: On-Prem DevOps Project

A complete end-to-end **DevOps simulation project for on-prem environments**, including manual deployment, Dockerization, CI/CD with Jenkins, Kubernetes deployment using Minikube, and more.

---

## 📦 Project Overview

A lightweight internal Issue Tracker API built using:

- **Backend**: FastAPI (Python)
- **DevOps Tools**: Docker, Jenkins, Kubernetes (Minikube), Git
- **Environment**: Ubuntu VM (Oracle VirtualBox)
- **Deployment Target**: On-prem simulation (local Linux VMs)

---

## 🧱 Phase 1: Manual FastAPI Deployment on Ubuntu VM

- Installed Python, FastAPI, and Uvicorn on Ubuntu
- Created a `main.py` FastAPI app with simple routes
- Exposed app on port 8000 and tested manually with `curl` and browser
- Configured `ufw` firewall to allow access
- Practiced Linux commands: `systemctl`, `top`, `ps`, `curl`, `journalctl`

---

## 🐳 Phase 2: Dockerize FastAPI App

- Created `Dockerfile` to containerize FastAPI app
- Built Docker image locally: `docker build -t fastapi-devopslab .`
- Ran container: `docker run -d -p 8000:8000 fastapi-devopslab`
- Added `.dockerignore` and `requirements.txt`
- Verified app was accessible via container

---

## ⚙️ Phase 3: CI/CD with Jenkins (On-Prem)

- Installed Jenkins on the Ubuntu VM
- Configured Jenkins to run Docker builds
- Added a `Jenkinsfile` to the repo with the following stages:
  - Clone repository from GitHub
  - Build Docker image
  - Remove old container (if running)
  - Run new container
- Created a **Pipeline Job** in Jenkins to automate the full process

---

## ☸️ Phase 4: Kubernetes Deployment (Minikube)

- Installed Minikube and `kubectl` on Ubuntu
- Created `deployment.yaml` to define app deployment
- Created `service.yaml` to expose app via NodePort (30080)
- Built Docker image inside Minikube environment
- Applied manifests using `kubectl apply -f`
- Accessed app via: `http://<minikube-ip>:30080/`

---

## 🔧 Tools & Technologies Used

| Category     | Tools                        |
|--------------|------------------------------|
| Language     | Python 3.10, FastAPI          |
| Deployment   | Uvicorn, Docker, Kubernetes   |
| CI/CD        | Jenkins, GitHub, Git          |
| Environment  | Ubuntu 20.04 (Oracle VM)      |
| K8s Type     | Minikube (local Kubernetes)   |
| Access Tools | curl, ufw, journalctl, top    |

---

## 📁 Folder Structure (Simplified)
```bash
devopslab/
├── main.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── .dockerignore
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
└── README.md
```

---

## 🔜 Next Phases (Planned)

- Phase 5: Monitoring & Logging (logrotate, health check, `top`, etc.)
- Phase 6: Bash scripting (automated backup, cron jobs, alerts)
- Phase 7: Security Hardening (UFW, SSH, secrets, RBAC)
- Phase 8: Ansible & Terraform (Infrastructure as Code - optional)

---

## 🧠 Author

**Sai Praneeth Gurrapu**  
Contact: gurrapu.saipraneeth98@gmail.com  
LinkedIn: [https://www.linkedin.com/in/saipraneethgurrapu](https://www.linkedin.com/in/saipraneethgurrapu)  
GitHub: [https://github.com/SaiPraneeth2509](https://github.com/SaiPraneeth2509)

---

> This project is built as part of my hands-on DevOps learning journey, simulating real-world on-prem deployment scenarios using open-source tools.
