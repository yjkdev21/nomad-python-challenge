# nomad-python-challenge

> 노마드코더 파이썬 챌린지 - 2주 완성 프로젝트

## 챌린지 소개

노마드코더의 파이썬 챌린지를 통해 2주 안에 파이썬 기초를 학습하는 프로젝트입니다. 강의를 수강하고 퀴즈와 과제를 완료하면서 웹 스크래퍼 제작을 목표로 합니다.

### 강의 정보

- 강의명: **Python으로 웹 스크래퍼 만들기 (Python for Beginners)**
- 총 강의수: **68개** (약 8시간)
- 난이도: **입문/기초**
- 챌린지 기간: **2주**
- 강의 링크: [Python for Beginners](https://nomadcoders.co/python-for-beginners)

---

## 학습 목표

- 파이썬의 기초 문법과 객체 지향 프로그래밍 학습
- 웹 스크래퍼 제작 및 데이터 수집 기술 습득
- Flask를 활용한 웹 서버 구축 경험

---

## 기술 스택

### 사용 기술 및 패키지

```
Language & Framework
- Python 3
- Flask
- HTML

Libraries
- requests
- BeautifulSoup4

Tools
- Repl.it
```

### 학습 주제

- Variables (변수)
- Functions (함수)
- Data Types (자료형)
- Arguments (인자)
- Keyword Arguments (키워드 인자)
- for loops (반복문)
- if/elif/else (조건문)
- Object Oriented Programming (객체 지향 프로그래밍)
- Web Scraping (웹 스크래핑)
- Flask Web Framework

### 수행 과제

- 국가 리스트와 통화 코드 스크래핑
- 알바 정보 스크래핑 (Stack Overflow Jobs, Indeed Jobs)
- 해커뉴스 API와 Flask 활용
- Web Server 구축
- Search Feature 구현
- CSV 파일 내보내기
- 채용 공고 웹 스크래퍼 제작
- 그 외 다수

---

## 학습 진도표 (2주 과정)

> 최종 업데이트: 2025.10.13

### 1주차

| 요일 | 과제 | 학습 범위 | 과제 유형 |
|------|------|-----------|--------|
| 월 | Assignment #01 | #1.2 - #2.3 | 퀴즈 |
| 화 | Assignment #02 | #2.4 - #2.8 | 퀴즈 |
| 수 | Assignment #03 | #2.9 - #3.2 | 코드 챌린지 |
| 목 | Assignment #04 | #3.3 - #3.7 | 코드 챌린지 |
| 금 | Assignment #05 | #4.0 - #4.4 | 퀴즈 |
| 토~일 | Assignment #06 | #4.5 - #4.9 | 코드 챌린지 (2일) |

### 2주차

| 요일 | 과제 | 학습 범위 | 과제 유형 |
|------|------|-----------|--------|
| 월 | Assignment #07 | #5.0 - #5.6 | 퀴즈 |
| 화~수 | Assignment #08 | #6.0 - #6.6 | 코드 챌린지 (2일) |
| 목~일 | Assignment #09 | #7.0 - #7.8 | 졸업작품 (4일) |

---

## 프로젝트 구조

```
nomad-python-challenge/
│
├── week1/                      # 1주차 학습
│   ├── assignment01/
│   │   ├── main.py            # Python 실습 코드
│   │   └── notes.md           # 학습 내용 정리
│   ├── assignment02/
│   │   ├── main.py
│   │   └── notes.md
│   ├── assignment03/
│   │   ├── main.py
│   │   └── notes.md
│   ├── assignment04/
│   │   ├── main.py
│   │   └── notes.md
│   ├── assignment05/
│   │   ├── main.py
│   │   └── notes.md
│   └── assignment06/
│       ├── main.py
│       └── notes.md
│
├── week2/                      # 2주차 학습
│   ├── assignment07/
│   │   ├── main.py
│   │   └── notes.md
│   ├── assignment08/
│   │   ├── main.py
│   │   └── notes.md
│   ├── assignment09/
│   │   ├── main.py
│   │   └── notes.md
│   └── final-project/          # 최종 수료 프로젝트 (Flask Web App)
│       ├── app.py              # Flask 웹 서버
│       ├── extractors/
│       │   └── wanted.py       # 채용 공고 스크래퍼
│       └── templates/
│           ├── index.html      # 메인 페이지
│           └── search.html     # 검색 결과 페이지
│
├── search/                     # 정적 검색 결과 페이지 (GitHub Pages용)
│   ├── search-java.html
│   ├── search-js.html
│   └── search-python.html
│
├── index.html                  # 프로젝트 메인 페이지 (수료 증명용)
└── README.md                   # 프로젝트 전체 설명
```

---

## 최종 프로젝트

### 채용 공고 웹 스크래퍼

Flask를 활용한 실시간 채용 공고 검색 웹 애플리케이션

**주요 기능**
- 채용 공고 실시간 스크래핑
- 키워드 기반 검색 기능
- 검색 결과 캐싱으로 성능 최적화
- 반응형 웹 디자인 (Pico CSS)
- CSV 파일 내보내기

**사용 기술**
- **Backend**: Flask (Python Web Framework)
- **Scraping**: Playwright, BeautifulSoup4
- **Frontend**: HTML, Pico CSS
- **Data**: Python Dictionary (In-memory Cache)

---

## 저작권 안내

> **중요**: 노마드코더 정책에 따라, 퀴즈 및 코드 챌린지의 구체적인 내용과 정답은 공개하지 않습니다.
> 
> 본 저장소에는 강의 내용을 바탕으로 한 **개인 학습 노트**와 **개념 정리**만 포함됩니다.

### 포함 내용
- 강의에서 배운 개념 정리
- 학습하면서 이해한 내용 요약
- 개인적으로 작성한 연습 코드
- 에러 해결 과정 및 학습 회고

### 미포함 내용
- 퀴즈 문제 및 정답
- 코드 챌린지 문제 및 해답
- 강의 자료의 직접적인 복사

---

## 학습 진행 상황

- [x] 1주차 완료
- [x] 2주차 완료
- [x] 졸업작품 완성

---

## 학습 기록

**시작일**: 2025.09.29  
**완료일**: 2025.10.13  
**학습 기간**: 2주 (14일)

---

## License

본 저장소는 개인 학습 목적으로 생성되었습니다.

---

**Nomad Coders - Python for Beginners**
