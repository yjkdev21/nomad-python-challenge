# Assignment #05

<aside>

- #4.0 Methods
- 자료 구조 (Data Structure)
- #4.1 Lists
- #4.2 Tuples
- #4.3 Dicts
- 추가: Sets
</aside>

---

## #4.0 Methods

### 함수와 메소드

**함수 (Function)**

- 단독 함수
- 독립적으로 사용
- `함수이름()` 형태
- 예: `print()`, `len()`, `type()`

```python
print("안녕")
len("hello")
```

**메소드 (Method)**

- 데이터(객체)와 결합된 함수
- 객체에 붙어서 사용
- `객체.메소드이름()` 형태
- 예: `.upper()`, `.lower()`, `.replace()`

```python
name = "python"
name.upper()  # "PYTHON"
name.lower()  # "python"
```

💡 **팁**: 파이썬 공식 문서(https://docs.python.org/3/)에서 내장 타입별 메소드 목록 확인 가능

**예시**

```python
name = "hello"
print(name.upper())  # HELLO
# name.upper() → 메소드 (문자열 객체의 메소드)
# print() → 함수 (내장 함수)
```

---

## 자료 구조 (Data Structure)

파이썬의 주요 자료구조:

- `list` **리스트** - 순서O, 변경O
- `tuple` **튜플** - 순서O, 변경X
- `dict` **딕셔너리** - Key-Value 쌍, 변경O
- `set` **세트** - 순서X, 중복X, 변경O

---

## #4.1 Lists

**리스트 (List)**

- 대괄호 `[]`로 생성
- 순서가 있는 데이터 집합
- 생성, 수정, 삭제 가능 (가변, mutable)
- 중복 허용

```python
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

```

---

## #4.2 Tuples

**튜플 (Tuple)**

- 소괄호 `()`로 생성
- 순서가 있는 데이터 집합
- **불변(immutable)** - 생성 후 수정, 삭제 불가능
- 읽기 전용 데이터에 사용

```python
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

# ❌ 불가능한 작업들
# days[0] = "Sunday"  # TypeError 발생
# days.append("Thursday")  # AttributeError

```

**튜플을 사용하는 이유**

- 데이터를 보호하고 싶을 때 (실수로 수정 방지)
- 리스트보다 메모리 효율적
- 딕셔너리의 키로 사용 가능

---

## #4.3 Dicts

**딕셔너리 (Dictionary)**

- 중괄호 `{}`로 생성
- Key(키)와 Value(값)의 쌍으로 구성
- 순서 유지 (Python 3.7+)
- Key는 불변 타입만 가능 (문자열, 숫자, 튜플)
- 수정, 생성, 삭제 가능

```python
player = {
    'name': 'Alice',
    'age': 30,
    'alive': True,
    'skills': ['Python', 'Machine Learning', 'Web Development']
}

# 값 접근 (대괄호)
player['name']          # "Alice"
player['skills'][0]     # "Python"
# player['height']      # ❌ KeyError 발생 (키가 없으면 에러)

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

```

---

## 추가: Sets

**세트 (Set)**

- 중괄호 `{}`로 생성 (딕셔너리와 구분: 키 없음)
- 순서 없음
- **중복 불가능** (자동으로 중복 제거)
- 수정 가능

```python
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

```

---

## 자료구조 비교표

| 자료구조 | 순서 | 중복 | 변경 | 표기 | 인덱싱 |
| --- | --- | --- | --- | --- | --- |
| **List** | O | O | O | [] | O |
| **Tuple** | O | O | X | () | O |
| **Dict** | O | Key 중복 X | O | {} | Key 로 |
| **Set** | X | X | O | {} | X |

---

<aside>

### 언제 어떤 자료구조를 사용할까?

1. **List (리스트)** 
    - 순서가 중요할 때
    - 값을 자주 추가/삭제할 때
    - 중복을 허용해야 할 때
    - 예: 할 일 목록, 점수 리스트, 로그 기록
2. **Tuple (튜플)** 
    - 데이터를 보호하고 싶을 때
    - 값이 변하지 않아야 할 때
    - 딕셔너리의 키로 사용할 때
    - 예: 좌표, 날짜, 설정값
3. **Dict (딕셔너리)** 
    - 키-값 쌍으로 데이터를 저장할 때
    - 빠른 검색이 필요할 때
    - 구조화된 데이터를 다룰 때
    - 예: 사용자 정보, 설정, JSON 데이터
4. **Set (세트)** 
    - 중복을 제거하고 싶을 때
    - 집합 연산이 필요할 때
    - 멤버십 테스트가 많을 때
    - 예: 고유 아이템, 태그, 방문 기록
</aside>