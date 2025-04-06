MediaAMP-Project/
├── flask_app/
│   ├── app.py
│   ├── wsgi.py
│   ├── hit_compute.sh
│   ├── compute.log
│   ├── flask_app.service
│   └── requirements.txt
├── jenkins/
│   ├── Jenkinsfile
│   └── setup_notes.md
├── prometheus/
│   ├── prometheus.yml
│   └── flask_metrics_exporter.md
├── screenshots/
├── README.md
└── .gitignore


# 🚀 MediaAMP-Project

An end-to-end DevOps simulation project using **Proxmox**, **Flask**, **CI/CD with Jenkins**, **Monitoring with Prometheus**, and **Automation via Crontab**.

---

## 1️⃣ Proxmox Setup

Provisioned:
- ✅ 1 VM with Ubuntu 22.04
- ✅ 1 LXC Container (Alpine Linux)
- Networking: Static IPs using virtual bridge (vmbr0)

📸 Screenshot:  
![Screenshot from 2025-04-05 01-15-49](https://github.com/user-attachments/assets/5cd91ba8-ec61-4508-9a20-813e333df3aa)
![Screenshot from 2025-04-05 01-22-35](https://github.com/user-attachments/assets/b7585e5b-ddd0-445c-a38f-4b6a07580bde)
![Screenshot from 2025-04-05 02-03-22](https://github.com/user-attachments/assets/0d04b7b5-e7d4-4de9-b250-0b9115e07ee6)
![Screenshot from 2025-04-05 02-21-07](https://github.com/user-attachments/assets/735bd4cc-7b30-4c0c-8a30-d0dd4bd60df3)
![Screenshot from 2025-04-05 02-35-53](https://github.com/user-attachments/assets/36555434-6332-4084-b6a0-b28fd45616be)
![Screenshot from 2025-04-05 02-44-02](https://github.com/user-attachments/assets/60b79e8b-5f64-48e3-8b47-9e181b1a6107)





---

## 2️⃣ Networking Setup

- Static IP for VM: `192.168.122.7`
- Enabled ping between VM ↔ LXC
- Internet outbound working

📸 Screenshot:
![Screenshot from 2025-04-05 02-50-36](https://github.com/user-attachments/assets/31abe126-8da5-4f1e-b640-6a1540ef33e6)


---

## 3️⃣ Flask Application

Flask app routes:
- `/` → returns `"Hello World from Harsh Khandelwal!"`
- `/compute` → computes `Fibonacci(30): 832040`

Deployed with:
- ✅ Gunicorn
- ✅ Nginx reverse proxy
- ✅ SystemD service

📁 File: `flask_app/app.py`  
📁 SystemD Service: `flask_app/flask_app.service`

📸 Screenshot:  
![Screenshot from 2025-04-05 13-32-45](https://github.com/user-attachments/assets/fc9412aa-4e79-44d3-9be1-87afe6eac2d4)
![Screenshot from 2025-04-05 13-32-55](https://github.com/user-attachments/assets/9f814372-ad18-4357-9b07-800d83d5233a)
![Screenshot from 2025-04-05 13-53-34](https://github.com/user-attachments/assets/4d975a2a-a285-4ff0-b461-8dc86f17ab13)


---

## 4️⃣ Automation with Crontab

- Script `hit_compute.sh` hits the `/compute` endpoint every minute.
- Output logged in `compute.log`.

📁 File: `flask_app/hit_compute.sh`

📸 Screenshot:  
![Screenshot from 2025-04-04 19-25-54](https://github.com/user-attachments/assets/1fad0585-f15e-4bd2-984e-af66c5f53429)

---

## 5️⃣ CI/CD with Jenkins

Pipeline Features:
- ✅ Clones GitHub repo
- ✅ Sets up virtual environment
- ✅ Restarts Flask SystemD service
- ✅ Test hits `/` endpoint using `curl`

📁 Jenkinsfile in `jenkins/`

📸 Screenshot:  
![Screenshot from 2025-04-07 00-22-11](https://github.com/user-attachments/assets/835da80d-8874-480a-9512-a6ecdda5f210)
![Screenshot from 2025-04-04 19-22-35](https://github.com/user-attachments/assets/6dc3ab97-21cb-40ce-9151-a8e2a6e37b8f)
![Screenshot from 2025-04-04 19-22-46](https://github.com/user-attachments/assets/65818581-30a8-4eef-a5b1-ac4cdfae1514)
![Screenshot from 2025-04-07 00-29-47](https://github.com/user-attachments/assets/2519f098-6458-4fa5-b0c2-bda7e70f3c06)



---

## 6️⃣ Monitoring with Prometheus

- **Node Exporter** for CPU/RAM metrics
- **prometheus_flask_exporter** for app metrics

📁 Prometheus config in `prometheus/`

📸 Screenshot:  
![Prometheus Monitoring](./screenshots/prometheus-monitoring.png)

---

## 📦 Tech Stack

- 🐧 Proxmox VE
- 🐍 Flask
- 🕸️ Nginx + Gunicorn
- 🔁 SystemD
- 🧪 Jenkins CI
- 📈 Prometheus & Exporters
- 🔁 Crontab


---

## 👨‍💻 Author

**Harsh [@Harsh7-code](https://github.com/Harsh7-code)**  
Project done as part of real-world simulation using Proxmox infra.

---
