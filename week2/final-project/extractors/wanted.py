from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup


class WantedJobScrapper:
    def __init__(self):
        """스크래퍼 초기화 - 브라우저 실행"""
        # Playwright 시작
        self.p = sync_playwright().start()
        # 크로미움 브라우저 실행 
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
                    f"https://www.wanted.co.kr/search?query={keyword}&tab=position"
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
                        link = f"https://www.wanted.co.kr{job.find('a')['href']}"
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
