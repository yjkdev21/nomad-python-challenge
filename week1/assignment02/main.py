# Assignment #02

# ========================================
# 2.4 Functions 함수
# ========================================

# 함수 정의
def say_hello():
    print("hello how r u?")

# 함수 호출
say_hello()

# ========================================
# 2.5 Indentation
# ========================================

# 에러 예시
# def say_hello():
# print("hello how r u?")

# def say_bye():
# print("Good Bye!")


# 정상 예시
def say_hello():
    print("hello how r u?")

def say_bye():
    print("Good Bye!")

# ========================================
# 2.6 Parameters
# ========================================

# parameter = user_name
def say_hi(user_name):
    print("Hi", user_name, "!")

# argument = "Jack", "Tom"
say_hi("Jack")
say_hi("Tom")

# ========================================
# 2.7 Multiple Parameters
# ========================================

def say_hello2(user_name, user_age):
    print("Hi My name is", user_name)
    print("I'm", user_age)

say_hello2("Mary", 36)

# ========================================
# 2.8 Recap
# ========================================

def tax_calculator(money):
    print(money * 0.35)

tax_calculator(12500)
