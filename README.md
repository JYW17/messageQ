# 🐇 RabbitMQ IoT Messaging System

이 프로젝트는 **RabbitMQ**를 활용하여 **Producer-Consumer 메시지 통신 시스템**을 구축한 예제입니다.  
**IoT 환경**에서 장치 간 비동기 메시지 송수신을 구현했습니다.

## 📦 **구성**
- **Producer**: 메시지를 RabbitMQ 큐에 보냅니다.
- **Consumer**: 메시지를 RabbitMQ 큐에서 수신하고 처리합니다.
- **RabbitMQ**: 메시지 큐 서버 (Docker로 실행)

---

## 🛠️ **설치 및 실행 방법**
### 📋 **1. 필수 요구사항**
- **운영체제**: Ubuntu 20.04 / Linux / Windows (WSL2)  
- **필수 소프트웨어**: 
  - Docker 
  - Python 3.x  
  - pip (파이썬 패키지 관리자)  

---

### 🔥 **2. 설치 절차**
#### 1️⃣ **Docker 설치**
```bash
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
