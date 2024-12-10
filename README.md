# RabbitMQ IoT Messaging System

이 프로젝트는 **RabbitMQ**를 사용하여 **Producer-Consumer 메시지 통신 시스템**을 구축한 예제입니다.  
Producer는 메시지를 전송하고, Consumer는 메시지를 수신하여 처리합니다.

## 실행 방법

### 1. 필수 요구사항
- **운영체제**: Ubuntu 20.04 / Linux / Windows (WSL2)
- **필수 소프트웨어**: 
  - Docker
  - Python 3.x
  - pip (Python 패키지 관리자)

---

### 2. 설치 절차

1. **Docker 및 python3, pip 설치**
```
# Docker 설치
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker

# Python3 및 pip 설치
sudo apt-get install -y python3 python3-pip
```

2. **필수 라이브러리 설치**
```
pip3 install pika
```
만약 error: externally-managed-environment 오류 시 아래 실행
```
sudo apt install python3-pika
```

3. **GitHub 저장소 클론**
```
git clone https://github.com/JYW17/messageQ.git
cd messageQ
```

---

### 3. 실행 방법

1. **RabbitMQ 컨테이너 실행**
```
sudo docker run -d --name rabbitmq-server -p 5672:5672 -p 15672:15672 rabbitmq:management
```
- **RabbitMQ 웹 인터페이스**: http://localhost:15672  
- **ID / PW**: `guest / guest`

2. **Consumer / Producer 실행**
- **Consumer 실행**: 
  ```
  python3 consumer.py
  ```
- **Producer 실행**: 다른 터미널 창들로 실행
  ```
  #n에는 0-99 숫자를 입력하여 각 producer마다 개인 번호 부여
  python3 producer.py n
  ```

---

### 4. 파일 설명
- **consumer.py**: RabbitMQ로부터 메시지를 수신하고 출력하는 코드
- **producer.py**: RabbitMQ로 메시지를 전송하는 코드, 

---

### 5. 주의사항
1. **RabbitMQ 포트 충돌**:  
- 다른 서비스가 5672 포트를 사용 중이면 포트를 변경해야 합니다.  
- RabbitMQ 컨테이너가 실행 중인지 확인하려면 `docker ps` 명령어를 사용합니다.  

2. **RabbitMQ 웹 대시보드**:  
- 웹 브라우저에서 [http://localhost:15672](http://localhost:15672)로 접속하여 대시보드에 접근할 수 있습니다.  
- 기본 로그인 정보:  
  - **ID**: guest  
  - **PW**: guest  
