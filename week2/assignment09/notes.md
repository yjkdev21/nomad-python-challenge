# Assignment #09

## 시작 전 파일 준비

### Playwright 설치

**Playwright란?**

- 웹 브라우저를 자동으로 제어할 수 있게 해주는 Python/JavaScript 라이브러리
- Selenium보다 빠르고 현대적인 웹 자동화 도구

**주요 용도**

1. **웹 크롤링/스크래핑**
    - 동적 웹사이트(JavaScript로 로딩되는 사이트) 데이터 수집
    - 로그인이 필요한 사이트 접근
2. **웹 자동화**
    - 반복적인 웹 작업 자동화 (폼 작성, 클릭 등)
    - 웹사이트 테스트 자동화
3. **스크린샷/PDF 생성**
    - 웹페이지 캡처 및 PDF 변환

**비슷한 도구들과 비교**

- **Selenium**: 오래된 웹 자동화 도구 (Playwright가 더 빠르고 현대적)
- **BeautifulSoup**: 정적 HTML 파싱만 가능 (JavaScript 실행 안됨)
- **requests**: 단순 HTTP 요청만 가능

**설치 방법**

```bash
# 1. Python 패키지 설치
pip install playwright

# 2. 실제 브라우저(Chrome, Firefox 등) 다운로드
playwright install

# 3. BeautifulSoup 설치 (HTML 파싱용)
pip install beautifulsoup4

```

---

### 파일 준비

[**main.py**](http://main.py/)

```python
# wanted.py에서 스크래핑 함수 가져오기
from extractors.wanted import extract_wanted_jobs

# 사용자에게 검색 키워드 입력받기
keyword = input("What do you want to search for? ")

# 원티드에서 채용공고 스크래핑 (리스트로 반환됨)
jobs = extract_wanted_jobs(keyword)

# CSV 파일 생성 (키워드 이름으로 파일명 설정, 예: python.csv)
file = open(f"{keyword}.csv", "w", encoding="utf-8")

# CSV 파일 첫 줄에 헤더(컬럼명) 작성
file.write("Title,Company,Location,Reward,Link\\n")

# 각 채용공고 정보를 CSV 파일에 한 줄씩 작성
for job in jobs:
    # 딕셔너리에서 값 꺼내서 쉼표로 구분해서 저장
    file.write(f"{job['title']},{job['company_name']},{job['location']},{job['reward']},{job['link']}\\n")

# 파일 닫기 (저장 완료)
file.close()

```

**extractors/wanted.py**

```python
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

class WantedJobScrapper:
    def __init__(self):
        """스크래퍼 초기화 - 브라우저 실행"""
        # Playwright 시작
        self.p = sync_playwright().start()
        # 크로미움 브라우저 실행 (headless=False: 브라우저 창 보이기)
        self.browser = self.p.chromium.launch(headless=False)
        # 검색할 키워드 리스트
        self.keywords = []
        # 스크래핑 결과 저장할 리스트
        self.result = []

    def add_keyword(self, keyword):
        """검색 키워드 추가"""
        # 리스트로 받으면 그대로 저장
        if isinstance(keyword, list):
            self.keywords = keyword
        # 문자열로 받으면 리스트에 추가
        elif isinstance(keyword, str):
            self.keywords.append(keyword)
        print(f"Keywords : {self.keywords}")

    def cleanup(self):
        """브라우저와 playwright 종료 - 메모리 정리"""
        if self.browser:
            self.browser.close()  # 브라우저 닫기
        if self.p:
            self.p.stop()  # Playwright 종료

    def start(self):
        """실제 스크래핑 시작"""
        try:
            # 키워드마다 반복
            for keyword in self.keywords:
                print(f"Scrapping {keyword}...")

                # 새 탭(페이지) 열기
                page = self.browser.new_page()
                # 원티드 검색 페이지로 이동
                page.goto(
                    f"<https://www.wanted.co.kr/search?query={keyword}&tab=position>"
                )

                # 페이지 스크롤해서 모든 채용공고 로드
                for x in range(5):
                    # 자바스크립트로 페이지 맨 아래로 스크롤
                    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    time.sleep(2)  # 2초 대기 (데이터 로딩 기다림)

                # 페이지의 HTML 가져오기
                content = page.content()
                page.close()  # 페이지 닫기 (메모리 절약)

                # BeautifulSoup으로 HTML 파싱
                soup = BeautifulSoup(content, "html.parser")
                # 모든 채용공고 카드 찾기
                jobs = soup.find_all("div", class_="JobCard_container__zQcZs")
                jobs_db = []  # 이번 키워드의 채용공고 저장

                # 각 채용공고마다 정보 추출
                for job in jobs:
                    try:
                        # 링크 추출
                        link = f"<https://www.wanted.co.kr>{job.find('a')['href']}"
                        # 제목 추출
                        title = job.find("strong", class_="JobCard_title___kfvj").text
                        # 회사명 추출
                        company_name = job.find(
                            "span",
                            class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu wds-nkj4w6",
                        ).text
                        # 보상금 추출
                        reward = job.find("span", class_="JobCard_reward__oCSIQ").text
                        # 위치 추출
                        location = job.find(
                            "span",
                            class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__location__4_w0l wds-nkj4w6",
                        ).text

                        # 딕셔너리로 정보 저장
                        job_data = {
                            "title": title,
                            "company_name": company_name,
                            "location": location,
                            "reward": reward,
                            "link": link,
                        }
                        jobs_db.append(job_data)  # 리스트에 추가

                    except Exception as e:
                        # 에러 발생해도 계속 진행
                        print(f"Error parsing job: {e}")
                        continue

                # 결과 저장
                self.result = jobs_db
            print(f"Scrapping Done!")
            # 스크래핑 결과 반환
            return self.result

        finally:
            # 에러가 나든 안나든 무조건 브라우저 정리
            self.cleanup()

def extract_wanted_jobs(keyword):
    """원티드 채용공고 추출 함수 (외부에서 호출용)"""
    # 스크래퍼 객체 생성
    scrapper = WantedJobScrapper()
    # 키워드 추가
    scrapper.add_keyword(keyword)
    # 스크래핑 시작하고 결과 반환
    return scrapper.start()

```

---

## #7.0 - #7.1 Hello Flask

### Flask란?

**Flask**

- Python으로 작성된 마이크로 웹 프레임워크
- 가볍고 간단하며 확장 가능한 구조
- 공식 문서: https://flask.palletsprojects.com/ko/stable/

**설치 방법**

```bash
pip install flask

```

**기본 사용법**

```python
# Flask 라이브러리에서 Flask 클래스 가져오기
from flask import Flask

# Flask 애플리케이션 생성
# __name__ 사용 권장 (현재 모듈 이름 자동 인식)
app = Flask(__name__)

# 루트 경로(/) 설정 - 데코레이터로 URL과 함수 연결
@app.route("/")
def home():
    # 브라우저에 "hello!" 메시지 반환
    return 'hello!'

# 웹 서버 실행
# 0.0.0.0 = 모든 IP에서 접속 허용, 기본 포트 5000
# debug=True: 코드 변경 시 자동 재시작, 에러 상세 표시
app.run("0.0.0.0", debug=True)

```

**개발 vs 배포 환경**

- **개발**: `debug=True` - 코드 수정 시 서버 자동 재시작, 에러 상세 표시
- **배포**: `debug=False` (기본값) - 보안을 위해 에러 메시지 숨김

---

## #7.2 Render Template

### HTML 반환하기

**문자열로 HTML 반환**

- Flask는 `return`한 문자열을 **HTML로 해석**
- HTML 태그를 직접 문자열로 작성 가능

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>Hello!</h1>'

app.run("0.0.0.0", debug=True)

```

출력: 브라우저에 `<h1>` 스타일이 적용된 "Hello!" 표시

---

### 라우트 추가와 링크 연결

**여러 페이지 만들기**

- `@app.route()` 데코레이터로 URL 경로와 함수를 연결
- HTML `<a>` 태그로 페이지 간 이동 가능

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>Hello!</h1> <a href="/hi">go to hi</a>'

@app.route("/hi")
def hello():
    return 'hi'

app.run("0.0.0.0", debug=True)

```

결과: 링크 클릭 시 `/hi` 페이지로 이동

---

### 템플릿 파일로 HTML 렌더링

**render_template() 함수**

- HTML 파일을 분리하여 관리 가능
- `templates/` 폴더에 HTML 파일 저장 필수
- Flask가 자동으로 `templates/` 폴더에서 파일 검색

**프로젝트 구조**

```
project/
├── app.py
└── templates/
    └── home.html

```

[**app.py**](http://app.py/)

```python
# Flask와 템플릿 렌더링 기능 가져오기
from flask import Flask, render_template

# Flask 앱 생성 (__name__으로 현재 파일 위치 인식)
app = Flask(__name__)

@app.route("/")
def home():
    # templates/home.html 파일 렌더링
    return render_template("home.html")

@app.route("/hi")
def hello():
    return 'hi'

# 서버 실행
app.run("0.0.0.0", debug=True)

```

---

### 템플릿에 변수 전달하기

**Jinja2 템플릿 엔진**

- Flask는 Jinja2 템플릿 엔진 사용
- Python 변수를 HTML로 전달 가능
- HTML에서 `{{ 변수명 }}` 형태로 출력

**동작 과정**

1. 브라우저 → Flask: HTTP Request 발생
2. Flask → 브라우저: 데이터를 HTML에 삽입하여 Response 전송

[**app.py**](http://app.py/)

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # name 변수를 템플릿으로 전달
    return render_template("home.html", name="Jack")

@app.route("/hi")
def hello():
    return 'hi'

app.run("0.0.0.0", debug=True)

```

**templates/home.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
    <!-- {{ name }} 위치에 "Jack"이 삽입됨 -->
    <h1>Welcome to the Home Page, {{name}}!</h1>
</body>
</html>

```

출력: "Welcome to the Home Page, Jack!"

---

### HTML 파일 인식 문제 해결

**문제 상황**

- VSCode에서 `templates/` 폴더의 HTML 파일이 Django 템플릿으로 인식됨
- HTML 문법 하이라이팅이 제대로 작동하지 않음

**해결 방법**

1. VSCode 좌측 하단 **[톱니바퀴 버튼]** → **[Settings]** 클릭
2. 검색창에 `file associations` 입력
3. *[File: Associations]**에서 **[Add Item]** 클릭
4. **Item**: `.html`, **Value**: `html` 입력 후 **[OK]** 클릭

**결과**: `.html` 확장자 파일이 모두 HTML로 인식됨

---

## #7.3 Form

**Form 태그와 Query String**

- HTML `<form>` 태그로 사용자 입력 받기
- `action` 속성: 데이터를 전송할 URL 지정
- `name` 속성: 입력값의 키(key) 역할
- Flask에서 `request.args.get()` 으로 쿼리 파라미터 접근

[**app.py**](http://app.py/)

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    # URL의 ?keyword=값 에서 keyword 추출
    keyword = request.args.get("keyword")
    return render_template("search.html", keyword=keyword)

app.run("0.0.0.0")

```

**templates/home.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Scrapper</title>
</head>
<body>
    <h1>Job Scrapper</h1>
    <h4>What job do you want to search for?</h4>
    <!-- form 제출 시 /search?keyword=입력값 형태로 이동 -->
    <form action="/search">
        <input type="text" name="keyword" placeholder="키워드를 입력하세요"/>
        <button>Search</button>
    </form>
</body>
</html>

```

**templates/search.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Scrapper</title>
</head>
<body>
    <h1>Search Results: "{{keyword}}"</h1>
</body>
</html>

```

결과: Search 버튼 클릭 시 `/search?keyword=입력값` 형태의 URL로 이동하고, 입력한 키워드가 페이지에 표시됨

---

## #7.5 Arguments

**스크래핑 결과를 웹에 표시하기**

- `extract_wanted_jobs()` 함수로 채용 공고 수집
- 수집한 데이터를 템플릿으로 전달

```python
from flask import Flask, render_template, request
from extractors.wanted import extract_wanted_jobs

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    # 키워드로 채용공고 스크래핑
    jobs = extract_wanted_jobs(keyword)
    print(jobs)  # 콘솔에 출력
    # 검색어와 결과를 템플릿으로 전달
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("0.0.0.0")

```

---

## #7.6 For Loops

**Jinja2 템플릿에서 반복문 사용하기**

- `{% for item in items %}` ~ `{% endfor %}` 구문 사용
- Python의 for 문과 유사하게 동작
- 리스트, 튜플 등 iterable 객체 순회 가능

**templates/search.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Scrapper</title>
</head>
<body>
    <h1>Search Results: "{{keyword}}"</h1>

    <!-- jobs 리스트의 각 항목을 반복 -->
    {% for job in jobs %}
    <div>
        {{job}}  <!-- 전체 딕셔너리 출력 -->
        {{job.link}}  <!-- 특정 키의 값만 출력 -->
    </div>
    {% endfor %}
</body>
</html>

```

결과: 각 채용 공고의 정보가 반복되어 화면에 표시됨

---

## #7.7 Pico CSS

**Pico CSS란?**

- 최소한의 CSS 클래스로 깔끔한 디자인을 제공하는 경량 CSS 프레임워크
- CDN으로 간단하게 적용 가능
- 공식 문서: https://picocss.com/docs

**CDN 링크 추가**

```html
<link rel="stylesheet" href="<https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css>">

```

**templates/home.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Scrapper</title>
    <link rel="stylesheet" href="<https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css>">
</head>
<body>
    <!-- container 클래스로 중앙 정렬 및 여백 자동 적용 -->
    <main class="container">
        <h1>Job Scrapper</h1>
        <h4>What job do you want to search for?</h4>
        <form action="/search">
            <input type="text" name="keyword" placeholder="키워드를 입력하세요"/>
            <button>Search</button>
        </form>
    </main>
</body>
</html>

```

**templates/search.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Scrapper</title>
    <link rel="stylesheet" href="<https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css>">
</head>
<body>
    <main class="container">
        <h1>Search Results: "{{keyword}}"</h1>

        <figure>
            <!-- role="grid"로 반응형 테이블 생성 -->
            <table role="grid">
                <thead>
                    <tr>
                        <th>Position</th>
                        <th>Company</th>
                        <th>Location</th>
                        <th>Link</th>
                    </tr>
                </thead>
                <tbody>
                    {% for job in jobs %}
                    <tr>
                        <td>{{job.title}}</td>
                        <td>{{job.company_name}}</td>
                        <td>{{job.location}}</td>
                        <td><a href="{{job.link}}" target="_blank">지원하기 →</a></td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </figure>
    </main>
</body>
</html>

```

결과: 깔끔하고 보기 좋은 테이블 형태로 채용 공고 표시

---

## #7.8 Cache

**캐싱(Caching)이란?**

- 한 번 조회한 데이터를 메모리에 저장하여 재사용
- 같은 검색어로 다시 검색 시 스크래핑 없이 저장된 결과 반환
- 속도 향상 및 서버 부하 감소

**캐시 구현하기**

- 딕셔너리 `db`에 `{키워드: 결과}` 형태로 저장
- 검색 전에 `db`에 키워드가 있는지 확인
- 있으면 저장된 데이터 사용, 없으면 새로 스크래핑

```python
from flask import Flask, render_template, request
from extractors.wanted import extract_wanted_jobs

app = Flask(__name__)

# 캐시 저장용 딕셔너리
db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    # 캐시 확인
    if keyword in db:
        # 캐시에 있으면 저장된 데이터 사용
        jobs = db[keyword]
    else:
        # 캐시에 없으면 새로 스크래핑
        jobs = extract_wanted_jobs(keyword)
        # 결과를 캐시에 저장
        db[keyword] = jobs

    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("0.0.0.0")

```

**동작 과정**

1. 첫 번째 검색: `python` 검색 → 스크래핑 실행 → `db`에 저장
2. 두 번째 검색: `python` 재검색 → `db`에서 바로 가져옴 (빠름)
3. 다른 검색어: `javascript` 검색 → 스크래핑 실행 → `db`에 추가 저장

**장점**

- 중복 스크래핑 방지
- 응답 속도 대폭 향상
- 서버 리소스 절약

**주의사항**

- 서버 재시작 시 캐시 초기화됨
- 실제 서비스에서는 Redis, Memcached 등 별도 캐시 시스템 사용 권장