# Assignment #05

# ========================================
# 4.0 Methods
# ========================================

# 함수 (Function) - 독립적으로 사용
print("안녕")
len("hello")

# 메소드 (Method) - 객체에 붙어서 사용
name = "python"
name.upper()  # "PYTHON"
name.lower()  # "python"

# 함수와 메소드 함께 사용 예시
name = "hello"
print(name.upper())  # HELLO
# name.upper() → 메소드 (문자열 객체의 메소드)
# print() → 함수 (내장 함수)


# ========================================
# 4.1 Lists
# ========================================

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# 인덱싱 (접근)
days_of_week[0]      # "Monday" (첫 번째 요소)
days_of_week[-1]     # "Friday" (마지막 요소)

# 슬라이싱
days_of_week[1:3]    # ["Tuesday", "Wednesday"]

# 주요 메소드
days_of_week.count("Monday")    # 특정 요소 개수 세기
days_of_week.append("Saturday") # 끝에 요소 추가
days_of_week.insert(0, "Sunday") # 특정 위치에 삽입
days_of_week.remove("Wednesday") # 특정 요소 삭제
days_of_week.pop()              # 마지막 요소 제거하고 반환
days_of_week.reverse()          # 리스트 순서 뒤집기
days_of_week.sort()             # 리스트 정렬
days_of_week.clear()            # 리스트 비우기

# 길이 확인
len(days_of_week)

# 리스트 연결
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2  # [1, 2, 3, 4]


# ========================================
# 4.2 Tuples
# ========================================

days = ("Monday", "Tuesday", "Wednesday")

# 인덱싱 (접근만 가능)
days[0]     # "Monday"
days[-2]    # "Tuesday" (뒤에서 두 번째)

# 슬라이싱
days[0:2]   # ("Monday", "Tuesday")

# 튜플 메소드 (제한적)
days.count("Monday")  # 특정 요소 개수
days.index("Tuesday") # 특정 요소의 인덱스

# 길이 확인
len(days)

# !! 불가능한 작업
# days[0] = "Sunday"  # TypeError 발생
# days.append("Thursday")  # AttributeError


# ========================================
# 4.3 Dicts
# ========================================

player = {
    'name': 'Alice',
    'age': 30,
    'alive': True,
    'skills': ['Python', 'Machine Learning', 'Web Development']
}

# 값 접근 (대괄호)
player['name']          # "Alice"
player['skills'][0]     # "Python"

# 값 접근 (get 메소드) - 권장
player.get('name')      # "Alice"
player.get('height')    # None (키가 없어도 에러 안남)
player.get('height', 0) # 0 (기본값 지정 가능)

# 값 수정
player['name'] = 'Dave'
player['age'] = 31

# 값 추가
player['height'] = 180
player['skills'].append('Django')

# 값 삭제
del player['age']           # 특정 키 삭제
player.pop('alive')         # 키 삭제하고 값 반환
player.clear()              # 전체 삭제

# 주요 메소드
player.keys()               # 모든 키 반환
player.values()             # 모든 값 반환
player.items()              # (키, 값) 튜플 반환

# 키 존재 확인
'name' in player            # True
'height' in player          # False

# 딕셔너리 병합 (Python 3.9+)
extra_info = {'team': 'A', 'score': 100}
player = player | extra_info


# ========================================
# 추가: Sets
# ========================================

# 세트 생성
numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4} - 중복 자동 제거
empty_set = set()          # 빈 세트 ({}는 빈 딕셔너리!)

# 요소 추가/삭제
numbers.add(5)
numbers.remove(2)     # 없으면 에러
numbers.discard(10)   # 없어도 에러 안남

# 집합 연산
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1 | set2  # 합집합 {1, 2, 3, 4, 5}
set1 & set2  # 교집합 {3}
set1 - set2  # 차집합 {1, 2}
set1 ^ set2  # 대칭차집합 {1, 2, 4, 5}

# 활용: 리스트 중복 제거
my_list = [1, 2, 2, 3, 3, 3]
unique = list(set(my_list))  # [1, 2, 3]
