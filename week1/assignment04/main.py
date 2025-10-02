# Assignment #03

# ========================================
# 3.3 And & Or
# ========================================

age = int(input("How old are you? "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 35:
    print("You are a young adult.")
elif age == 50 or age == 40:
    print("You are in your prime years.")
else:
    print("You are an adult.")

# 주요 함수들
# ==============================

# input() 함수
age = input("How old are you? ")
print("You are " + age + " years old.")

# type() 함수
age = input("How old are you? ")
print(type(age))

# int() 함수
age = int(input("How old are you? "))
print(type(age))

# ========================================
# 3.4 Python Standard Library
# ========================================

# 방법 1: 모듈 전체 불러오기
# import 모듈

# 방법 2: 특정 함수만 불러오기
# from 모듈 import 함수

# 실습 예제 - 숫자 맞추기 게임
# ==============================

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

# ========================================
# 3.5 - #3.6 While
# ========================================

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



# 추가: 주석(Comments)
# ==============================

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
