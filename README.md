# 📝 설문조사 API 프로젝트

> **Flask를 기반으로 한 설문조사 API 개발 프로젝트입니다.**  
사용자가 설문조사에 이미지와 질문을 추가하고, 답변 데이터를 수집·통계 분석하며, 이를 시각적으로 표현할 수 있는 기능을 제공합니다. 최종적으로 AWS EC2를 활용하여 배포까지 완료하는 것을 목표로 합니다.

---

## 📖 프로젝트 개요

이 프로젝트의 주요 목표는 다음과 같습니다:
 - **CRUD 기능 제공:** 이미지와 질문의 생성, 수정, 삭제 지원
 - **데이터 분석 및 시각화:** 설문조사 결과를 통계로 분석 후 그래프로 표현
 - **AWS 배포:** EC2를 활용한 배포
 - **유저 친화적 API 제공:** 직관적인 인터페이스와 유용한 문서 제공

---

## 🐤 데모
> 아래는 애플리케이션 실행 화면 예시입니다.  



https://github.com/user-attachments/assets/d8506c51-fba6-4e8b-9759-fa21a4ebc5c4



---

## 💻 시작하기

### 1️⃣ 설치

```bash
# 저장소 클론
git clone https://github.com/hak2881/flask_miniproject1.git
cd flask_miniproject1

# Python 설치 (3.6 이상 권장)
# 필수 패키지 설치
pip install -r requirements.txt

### 2️⃣ 실행, 종료

```bash
# 애플리케이션 실행
bash launch.py
# 애플리케이션 종료
bash terminate.py
```
---

## 🔧 기술 스택

- **백엔드:** Flask, Python
- **프론트엔드:** HTML, JavaScript
- **데이터베이스:** MySQL
- **배포:** AWS EC2
- **시각화:** Matplotlib, Plotly

---

## 📂 프로젝트 구조

```plaintext
flask_miniproject/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── answer.py
│   │   ├── choices.py
│   │   ├── images.py
│   │   ├── questions.py
│   │   ├── stats_routes.py
│   │   └── users_routes.py
│   ├── __init__.py
│   └── modely.py
├── migrations/
└── scripts/
    ├── .gitignore
    ├── config.py
    ├── form.conf
    ├── gunicorn.log
    ├── launch.sh
    ├── requirements.txt
    ├── run.py
    ├── terminate.sh
    └── wsgi.py
```
---

## ⚒ 개발 과정

1. **데이터베이스 연결:**  
   MySQL과 Flask SQLAlchemy를 활용하여 데이터 모델을 설계하고 데이터 관리를 구현했습니다.

2. **Blueprint 설계:**  
   모듈별로 API 엔드포인트를 분리하여 확장성과 유지보수성을 높였습니다.  
   주요 Blueprint는 다음과 같습니다:
   - `questions.py`: 질문 관련 CRUD 처리
   - `users.py` : 유저 관련 CRUD 처리
   - `answers.py`: 답변 처리 및 저장
   - `stats_routes.py`: 통계 및 데이터 시각화


3. **에러 처리:**  
   사용자 경험을 고려하여 안정적인 에러 핸들링을 구현했습니다.  
   예를 들어, 잘못된 요청 시 HTTP 상태 코드를 반환하고 상세한 오류 메시지를 제공합니다.

4. **시각화 기능 추가:**  
   설문조사 데이터를 수집한 후 통계적으로 분석하고, 그래프나 차트 형태로 시각화하여 사용자가 데이터를 쉽게 이해할 수 있도록 구성했습니다.

---

## 👨‍💻 역할 및 기여

### **개발 팀**
| 이름          | 역할                                | 주요 기여                          |
|---------------|-------------------------------------|------------------------------------|
| **김병학**    | 팀장 / API 설계                    | Flask Blueprint 활용 API 개발      |
| **이성범**    | 데이터베이스 설계 및 연결           | MySQL 데이터 모델 설계 및 관리      |
| **이영우**    | 제작           | ppt 제작 및 발표            |

---

---

## 📊 Use Case Diagram

### Use Case Diagram이란?

> **Use Case Diagram**은 시스템과 사용자의 상호작용을 명세한 다이어그램으로, 사용자의 관점에서 시스템의 `서비스`, `기능`, `외부와의 관계`에 대하여 다이어그램으로 표현한 것을 의미합니다.

---

### 구성 요소

#### **1️⃣ System**
- 외부에서 Actor가 보는 프로그램과 그 내부의 동작을 영역으로 구분 지어 표현합니다.  

---

#### **2️⃣ Actor**
- 시스템을 사용하는 사용자나, 시스템과 상호작용하는 또 다른 시스템을 의미합니다.  

---

#### **3️⃣ Usecase**
- 사용자 입장에서 바라본 시스템의 기능을 표현합니다.  

---

#### **4️⃣ Relation**
- Actor와 Usecase, Usecase들 사이의 관계를 표현합니다.  

---

---

### 🔗 참고 자료
- [깃허브 프로젝트 생성 가이드](https://www.notion.so/16ccaf5650aa81f69398ca6e366165de?pvs=21)
- [Git Flow 전략](https://www.notion.so/Git-Flow-16ccaf5650aa810b8b8bed6ab4977e76?pvs=21)

---

### 🚀 배포 준비
1. AWS EC2 인스턴스 생성
2. Gunicorn 및 Nginx 구성
3. 배포 후 API 안정성 테스트

---

문의 및 추가 정보: [프로젝트 저장소 링크](https://github.com/hak2881/flask_miniproject1)


