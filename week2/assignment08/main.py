# Assignment #08

# ========================================
# 6.1 필수 라이브러리 설치
# ========================================

# BeautifulSoup4: HTML/XML에서 데이터 추출
# pip install beautifulsoup4

# Requests: HTTP 요청을 보내고 웹 페이지 콘텐츠 가져오기
# pip install requests

# 설치 확인
import requests
from bs4 import BeautifulSoup

print(requests.__version__)
# print(BeautifulSoup.__version__)


# ========================================
# 6.2 - 6.4 BeautifulSoup 기본 사용법
# ========================================

# 슬라이싱 (Slicing) - 리스트/문자열의 일부 추출
my_list = [0, 1, 2, 3, 4, 5]
print(my_list[1:-1])  # [1, 2, 3, 4] - 첫/마지막 제외
print(my_list[::2])   # [0, 2, 4] - 2칸씩 건너뛰기
print(my_list[::-1])  # [5, 4, 3, 2, 1, 0] - 역순


# 언패킹 (Unpacking) - 시퀀스 요소를 여러 변수에 한 번에 할당
a, b = [1, 2]  # a=1, b=2
categories = ["Python", "Backend"]
first, second = categories[:2]
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2, 3, 4]


# .get() 메서드 - 안전하게 값 가져오기 (KeyError 방지)
test_dict = {"name": "test"}
print(test_dict.get("class", []))  # class 없으면 빈 리스트 반환


# 기본 스크래핑 예제
import requests
from bs4 import BeautifulSoup

# 1. 웹페이지 요청
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
response = requests.get(url)

# 2. HTML 파싱
soup = BeautifulSoup(
    response.content,  # HTML 원본 데이터
    "html.parser",     # 파서 종류
)

# 3. 데이터 추출
# 첫 번째/마지막 li 태그는 광고/메타 정보 → 제외
jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

all_jobs = []

for job in jobs:
    # 광고 게시물 건너뛰기
    if "meta-ad" in job.get("class", []):
        continue

    # 카테고리 2개 미만이면 건너뛰기
    categories = job.find_all("p", class_="new-listing__categories__category", limit=2)
    if len(categories) < 2:
        continue

    # 언패킹
    first, second = categories

    # 텍스트 추출
    title = job.find("h3", class_="new-listing__header__title").text
    company = job.find("p", class_="new-listing__company-name").text
    first = first.text
    second = second.text

    # URL 추출
    url_tag = job.find('div', class_='tooltip--flag-logo').next_sibling
    job_url = url_tag['href']

    # 딕셔너리로 구조화
    job_data = {
        "title": title,
        "company": company,
        "first": first,
        "second": second,
        "url": f"https://weworkremotely.com{job_url}"
    }
    all_jobs.append(job_data)

print(f"총 {len(all_jobs)}개 수집 완료")
print(all_jobs)


# ========================================
# 6.5 Pagination (페이지네이션)
# ========================================

# 여러 페이지의 데이터를 자동으로 수집
import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
    """특정 페이지의 채용 공고 스크래핑"""
    print(f"Scraping URL: {url}")

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

    for job in jobs:
        if "meta-ad" in job.get("class", []):
            continue

        categories = job.find_all(
            "p",
            class_="new-listing__categories__category",
            limit=2
        )
        if len(categories) < 2:
            continue

        first, second = categories

        title = job.find("h3", class_="new-listing__header__title").text
        company = job.find("p", class_="new-listing__company-name").text
        first = first.text
        second = second.text

        url_tag = job.find('div', class_='tooltip--flag-logo').next_sibling
        job_url = url_tag['href']

        job_data = {
            "title": title,
            "company": company,
            "category1": first,
            "category2": second,
            "url": f"https://weworkremotely.com{job_url}"
        }
        all_jobs.append(job_data)

def get_pages(url):
    """전체 페이지 수 확인"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    pages = soup.find("span", class_="pages-container").find_all("span", class_="page")
    return pages

# 실행
base_url = "https://weworkremotely.com/remote-full-time-jobs"
total_pages = get_pages(f"{base_url}?page=1")

# 모든 페이지 순회
for x in range(len(total_pages)):
    page_url = f"{base_url}?page={x+1}"
    scrape_page(page_url)

print(f"\n총 {len(all_jobs)}개 수집 완료")


# ========================================
# 코드 개선 - 에러 처리
# ========================================

def scrape_page_with_error_handling(url):
    """에러 처리가 추가된 스크래핑 함수"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 4xx, 5xx 에러 발생
    except requests.RequestException as e:
        print(f"Error: {url} - {e}")
        return
    
    soup = BeautifulSoup(response.content, "html.parser")
    # ... 나머지 코드


# ========================================
# 코드 개선 - 텍스트 정리
# ========================================

# .strip(): 앞뒤 공백/줄바꿈 제거
title = job.find("h3", class_="new-listing__header__title").text.strip()
company = job.find("p", class_="new-listing__company-name").text.strip()


# ========================================
# 코드 개선 - CSV 저장
# ========================================

import csv

# all_jobs 리스트를 CSV 파일로 저장
with open('jobs.csv', 'w', newline='', encoding='utf-8') as f:
    if all_jobs:
        writer = csv.DictWriter(f, fieldnames=all_jobs[0].keys())
        writer.writeheader()
        writer.writerows(all_jobs)
        print("jobs.csv 저장 완료!")


# ========================================
# 추가 팁 - User-Agent 설정
# ========================================

# 봇 접근 차단 우회
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers)


# ========================================
# 추가 팁 - 요청 간 시간 지연
# ========================================

import time

# 서버 부담 방지
for x in range(len(total_pages)):
    page_url = f"{base_url}?page={x+1}"
    scrape_page(page_url)
    time.sleep(1)  # 1초 대기

