# 📝 설문조사 Api 제작



---



## 📖 프로젝트 설명  

이 프로젝트는 Flask을 기반으로 한 **설문 조사 Api 제작**입니다.  

사용자는 새로운 이미지,질문을 추가, 삭제하며 작업을 완료 처리하거나 삭제할 수 있습니다.  

AWS EC2를 사용하여 배포단계 까지 하는것이 최종 목표입니다.

마지막으로 질문에 대한 답들을 통계내어 그래프로 시각적으로 볼 수 있게 구성하였습니다.



---



## 🐤 데모  



아래는 애플리케이션 실행 화면 예시입니다:  


https://github.com/user-attachments/assets/35348d4d-aea6-44bd-aedf-bb71df3a607c


---



---



## 💻 시작하기  



### 설치  

1. 이 저장소를 클론합니다:  

   ```bash

   git clone https://github.com/hak2881/flask_miniproject1.git

   cd task-manager

   ```



2. Python을 설치합니다(버전 3.6 이상 권장).



### 애플리케이션 실행  

Python으로 스크립트를 실행합니다:  

```bash

bash launch.py

```

---



## 🔧 기술 스택  

- **언어**: Python, Html, JavaScript  



---



## 📂 프로젝트 구조  



```plaintext

flask_miniproject/

├── app 
    ├── routes
         ├── __init__.py
         ├── answer.py
         ├── choices.py
         ├── images.py
         ├── questions.py
         ├── stats_routes.py
         └── users_routes.py
   ├── __init__.py
   └── modely.py
├── migrations  
└── scripts        
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



1. **데이터 저장 mysql 연결**

2. **Blueprint를 활용한 Api 생성**

3. **에러 처리**



---



## 👨‍💻 역할 및 기여  



- **개발자**: [Kim Byung Hak], [Lee Seong Bum], [Lee Young Woo]  

    - Flask Blueprint를 활용한 Api 개발.  

    - AWS EC2를 활용해 배포  

    - 직관적인 메뉴 옵션 및 사용자 인터페이스 구성.  



---



