def save_to_file(file_name, jobs):
    # CSV 파일 생성 (키워드 이름으로 파일명 설정, 예: python.csv)
    file = open(f"{file_name}.csv", "w", encoding="utf-8")

    # CSV 파일 첫 줄에 헤더(컬럼명) 작성
    file.write("Title,Company,Location,Reward,Link\n")

    # 각 채용공고 정보를 CSV 파일에 한 줄씩 작성
    for job in jobs:
        # 딕셔너리에서 값 꺼내서 쉼표로 구분해서 저장
        file.write(
            f"{job['title']},{job['company_name']}, {job['location']}, {job['reward']}, {job['link']}\n"
        )

    # 파일 닫기 (저장 완료)
    file.close()
