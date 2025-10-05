# Assignment #06

<aside>

- #4.5 For Loops
- #4.6 URL Formatting
- #4.7 Requests
- #4.8 Status Codes
- #4.9 Recap
</aside>

---

## #4.5 For Loops

### **for-in 문**

- 시퀀스(tuple, list, string 등)의 각 요소를 순회하며 반복 작업을 수행하는 제어문

```python
# tuple이나 list 생성 시 변수명은 복수형 사용
websites = (
    "google.com",
    "airbnb.com",
    "amazon.com",
    "netflix.com"
)

# for loop: websites의 각 요소를 website 변수에 할당하며 반복
for website in websites:
    print(website)
```

> **출력:**
> 
> 
> ```python
> google.com
> airbnb.com
> amazon.com
> netflix.com
> ```
> 

---

## #4.6 URL Formatting

**문자열 메서드**:

- **if not**: 조건이 False일 때 실행 (`not`은 불린값을 반대로 뒤집음)
- `startswith(prefix)`: 문자열이 특정 접두사로 시작하는지 확인 (반환값: True/False)
- **f-string**: `f"문자열 {변수}"` 형태로 문자열 안에 변수를 삽입하는 포맷팅 방법

```python
websites = (
    "google.com",
    "https://airbnb.com",
    "https://amazon.com",
    "netflix.com"
)

# URL Formatting
for website in websites:
    # startswith()로 "https://" 유무 확인
    if not website.startswith("https://"):
        website = f"https://{website}"  # f-string으로 문자열 조합
    print(website)
```

> **출력:**
> 
> 
> ```python
> https://google.com
> https://airbnb.com
> https://amazon.com
> https://netflix.com
> ```
> 

---

## #4.7 Requests

### PyPI와 외부 패키지

**Python Standard Library**: Python 설치 시 기본 제공되는 내장 모듈 (import만으로 사용 가능)

- 예: `os`, `sys`, `json`, `datetime` 등

**PyPI (Python Package Index)**: 외부 개발자가 만든 서드파티 패키지 저장소

- 사이트: https://pypi.org/
- 별도 설치 필요: `pip install` 명령어 사용

### requests 모듈

**HTTP 통신**: 클라이언트(브라우저)와 서버 간 데이터를 주고받는 프로토콜

- **requests**: HTTP 요청을 간편하게 보낼 수 있는 라이브러리
- 사이트: https://pypi.org/project/requests/
- 용도: 웹 스크래핑, REST API 호출, 웹 페이지 다운로드 등

**설치 방법:**

```powershell
python -m pip install requests
```

### VSCode 모듈 설치 오류 해결

**문제**: `ModuleNotFoundError: No module named 'requests'`

**원인**: VSCode가 사용 중인 Python 인터프리터와 pip로 설치한 위치가 다를 때 발생

**해결방법**:

1. **Python 인터프리터 확인**
    - `Ctrl + Shift + P` → `Python: Select Interpreter` 선택
    - 올바른 Python 버전 선택
2. **Python/pip 버전 확인**

```powershell
python --version
pip --version
```

1. **올바른 방법으로 모듈 설치**

```bash
python -m pip install requests
```

- `python -m pip`: 현재 Python 인터프리터에 연결된 pip 사용
1. **VSCode 재시작**

---

## #4.8 Status Codes

**HTTP 상태 코드**: 서버가 클라이언트 요청에 대한 처리 결과를 알려주는 3자리 숫자

- 상태 코드 문서: https://developer.mozilla.org/ko/docs/Web/HTTP/Status

```python
from requests import get

websites = (
    "google.com",
    "https://airbnb.com",
    "https://naver.com",
    "netflix.com"
)

results = {}  # 빈 딕셔너리 생성

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"

    # get(): HTTP GET 요청을 보내고 Response 객체 반환
    response = get(website)

    # Response 객체의 status_code 속성으로 상태 코드 확인
    if response.status_code == 200:
        results[website] = "OK"  # 딕셔너리에 결과 저장
    else:
        results[website] = "FAILED"

    print(website, response)
    print(website, response.status_code)

print(results)
```

> **출력:**
> 
> 
> ```python
> https://google.com <Response [200]>
> https://google.com 200
> https://airbnb.com <Response [200]>
> https://airbnb.com 200
> https://naver.com <Response [200]>
> https://naver.com 200
> https://netflix.com <Response [200]>
> https://netflix.com 200
> {'https://google.com': 'OK', 'https://airbnb.com': 'OK', 'https://naver.com': 'OK', 'https://netflix.com': 'OK'}
> ```
> 

### HTTP 상태 코드 분류

- **1xx (Informational)**: 요청 수신, 처리 진행 중
- **2xx (Success)**: 요청 성공 (200: OK)
- **3xx (Redirection)**: 추가 조치 필요 (301: 영구 이동, 302: 임시 이동)
- **4xx (Client Error)**: 클라이언트 오류 (400: 잘못된 요청, 404: 찾을 수 없음)
- **5xx (Server Error)**: 서버 오류 (500: 내부 서버 오류, 503: 서비스 불가)

---

## #4.9 Recap

**응답 코드 테스트 사이트**: https://httpbin.org/status/`응답번호`

```python
from requests import get

websites = (
    "google.com",
    "netflix.com",
    "https://httpbin.org/status/101",
    "https://httpbin.org/status/304",
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/501"
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)

    status = response.status_code

    # 조건문 순서: 큰 숫자 → 작은 숫자
    if status >= 500:  # 500~599
        results[website] = "5xx Server Error"
    elif status >= 400:  # 400~499
        results[website] = "4xx Client Error"
    elif status >= 300:  # 300~399
        results[website] = "3xx Redirection"
    elif status >= 200:  # 200~299
        results[website] = "2xx OK"
    elif status >= 100:  # 100~199
        results[website] = "1xx Informational"
    else:
        results[website] = "Unknown Status"

print(results)

```

> **출력:**
> 
> 
> ```python
> {
>     'https://google.com': '2xx OK',
>     'https://netflix.com': '2xx OK',
>     'https://httpbin.org/status/101': '1xx Informational',
>     'https://httpbin.org/status/304': '3xx Redirection',
>     'https://httpbin.org/status/404': '4xx Client Error',
>     'https://httpbin.org/status/501': '5xx Server Error'
> }
> ```
>