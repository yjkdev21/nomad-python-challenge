# Assignment #04

<aside>

- #3.3 And & Or
- #3.4 Python Standard Library
- #3.5 - #3.6 While
</aside>

---

## #3.3 And & Or

### 논리 연산자

- `and` : 둘 다 True 면 **True**
- `or` : 둘 중 하나만 True 여도 **True**

### 조건문 예제

```python
age = int(input("How old are you? "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 35:
    print("You are a young adult.")
elif age == 50 or age == 40:
    print("You are in your prime years.")
else:
    print("You are an adult.")

```

**출력 예시:**

```
How old are you? 30
You are a young adult.
```

```
How old are you? 40
You are in your prime years.
```

---

## 주요 함수들

### input() 함수

- 사용자로부터 입력을 받는 함수
- 반환값은 항상 **문자열(str)** 타입

```python
age = input("How old are you? ")
print("You are " + age + " years old.")
```

> **출력:**
> 
> 
> ```
> How old are you? 33
> You are 33 years old.
> ```
> 

### type() 함수

- 값의 타입을 확인할 수 있는 함수
- `<class 'type'>` 형태로 확인 가능

```python
age = input("How old are you? ")
print(type(age))
```

> **출력:**
> 
> 
> ```
> How old are you? 14
> <class 'str'>
> ```
> 

### int() 함수

- **형변환 함수** (타입 변환 함수)
- 문자열이나 실수를 정수(int)로 변환

```python
age = int(input("How old are you? "))
print(type(age))
```

> **출력:**
> 
> 
> ```
> How old are you? 42
> <class 'int'>
> ```
> 

---

## #3.4 Python Standard Library

### 파이썬 표준 라이브러리

공식 문서: https://docs.python.org/ko/3.13/library/index.html

### 라이브러리 사용법

```python
# 방법 1: 모듈 전체 불러오기
import 모듈

# 방법 2: 특정 함수만 불러오기
from 모듈 import 함수
```

### 실습 예제 - 숫자 맞추기 게임

```python
# random 라이브러리의 randint 함수 import
from random import randint

user_choice = int(input("Choose number: "))
pc_choice = randint(0, 50)

print(f"PC choice: {pc_choice}")

if user_choice == pc_choice:
    print("Draw")
elif user_choice > pc_choice:
    print("You win")
else:
    print("You lose")
```

> **출력 예시:**
> 
> 
> ```
> Choose number: 40
> PC choice: 30
> You win
> ```
> 

---

## #3.5 - #3.6 While

### while 반복문

- 조건이 **True**일 때만 반복 실행되는 반복문
- 조건이 **False**가 되면 반복 종료

### 실습 예제 - 숫자 맞추기 게임2

```python
from random import randint

print("Welcome to the game!")
pc_choice = randint(1, 100)

playing = True

while playing:
    user_choice = int(input("Choose number(1~100): "))

    if user_choice == pc_choice:
        print("You won!")
        playing = False
    elif user_choice < pc_choice:
        print("Higher")  # 더 높은 수를 선택하세요
    elif user_choice > pc_choice:
        print("Lower")   # 더 낮은 수를 선택하세요

print(f"PC choice: {pc_choice}")
```

> **출력 예시:**
> 
> 
> ```
> Welcome to the game!
> Choose number(1~100): 80
> Lower
> Choose number(1~100): 60
> Higher
> Choose number(1~100): 70
> Higher
> Choose number(1~100): 75
> Lower
> Choose number(1~100): 73
> You won!
> PC choice: 73
> ```
> 

## 추가: 주석(Comments)

### 주석 작성법

- **한 줄 주석**: `#`
- **여러 줄 주석**: `'''` 또는 `"""`

```python
# 이것은 한 줄 주석입니다

'''
이것은
여러 줄
주석입니다
'''

"""
이것도
여러 줄
주석입니다
"""
```
