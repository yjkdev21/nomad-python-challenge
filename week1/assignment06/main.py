# Assignment #06

# ========================================
# 4.5 For Loops
# ========================================

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


# ========================================
# 4.6 URL Formatting
# ========================================

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


# ========================================
# 4.8 Status Codes
# ========================================

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


# ========================================
# 4.9 Recap
# ========================================

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