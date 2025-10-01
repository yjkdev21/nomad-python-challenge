# Assignment #03

# ========================================
# 2.9 Default Parameters
# ========================================

def say_hello_user(user_name="Guest"):
    print("hello, " + user_name)

say_hello_user()
say_hello_user("Alice")

# 실습: 사칙연산 및 제곱 함수
# ==============================

# 더하기
def plus(a=1, b=1):
    print(a + b)

# 빼기
def minus(a=1, b=1):
    print(a - b)

# 곱하기
def multiply(a=1, b=1):
    print(a * b)

# 나누기
def divide(a=1, b=1):
    print(a / b)

# 제곱
def power(a=1, b=1):
    print(a ** b)

# 함수 호출
plus(2, 3)
minus(5, 3)
multiply(3, 4)
divide(10, 2)
power(2, 3)

# 기본값 사용
plus()
minus()
multiply()
divide()
power()

# ========================================
# 2.10 - 2.11 Return Values
# ========================================

# 반환
def tax_calc(money):
    return money * 0.35
    # 아래 문장은 실행 안됨
    print("Your money")

def pay_tax(tax):
    print("Thank you for paying", tax)

# 반환값을 다른 함수에 전달
pay_tax(tax_calc(100000))

# 문자열 포맷팅 
# ==============================

# 포맷된 문자열을 반환
def coffee(coffee_type):
    return f"Enjoy your {coffee_type} coffee!"

print(coffee("espresso"))

# print 실행 결과를 반환 (None)
def tea(tea_type):
    return print(f"Enjoy your {tea_type} tea!")

tea("green")

# ========================================
# 3.0 - 3.2 If & Else & Elif
# ========================================


# if 문
# ==============================
if 10 < 4:
    print("10 < 4 Correct")

if 10 > 4:
    print("10 > 4 Correct")

if 10 == 10:
    print("10 == 10 Correct")

a = "hello"

if a == "hello":
    print("a is hello")


# Else & Elif
# ==============================

winner = 200

if winner > 50:
    print("You win!") # 출력
elif winner > 100:
    print("You top score!")
elif winner < 50:
    print("You lose!")
else:
    print("It's a tie!")
