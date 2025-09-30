# Assignment #02

## 2.4 Functions 함수

### 파이썬 함수 규칙

- 파이썬에서는 `def` 키워드를 사용하여 함수를 정의
- 함수명 뒤에는 콜론`:` 작성
- 숫자로 시작 / 공백 불가
- 함수를 호출하려면 함수 이름 뒤에 괄호를 사용

```python
# 함수 정의
def say_hello():
    print("hello how r u?")

# 함수 호출
say_hello()
```

> **출력:** `hello how r u?`
> 

## 2.5 Indentation 들여쓰기

- 파이썬 문법은 중괄호 대신 **들여쓰기**로 **영역(scope)**을 지정
- 들여쓰기는 일관성만 유지하면 됨 (보통 스페이스 4칸 권장)
- if, for, class, def 등에서 사용

```python
# 에러 예시
# def say_hello():
# print("hello how r u?")

# def say_bye():
# print("Good Bye!")
```

```python
# 정상 예시
def say_hello():
    print("hello how r u?")

def say_bye():
    print("Good Bye!")
```

## 2.6 Parameters 매개변수와 인수

### 매개변수 (Parameter)

- 함수를 **정의**할 때 받을 데이터를 나타내는 변수

### 인수 (Argument)

- 함수를 **호출**할 때 실제로 전달하는 데이터(값)

```python
# parameter = user_name
def say_hi(user_name):
    print("Hi", user_name, "!")

# argument = "Jack", "Tom"
say_hi("Jack")
say_hi("Tom")
```

> **출력:**
> 
> 
> ```
> Hi Jack !
> Hi Tom !
> ```
> 

## 2.7 Multiple Parameters 다중 매개변수

- 함수에 필요한 매개변수의 개수와 인수의 개수는 동일해야 함
- 2개 이상의 인수가 필요한 경우 순서에 유의

```python
def say_hello2(user_name, user_age):
    print("Hi My name is", user_name)
    print("I'm", user_age)

say_hello2("Jack", 36)
```

> **출력:**
> 
> 
> ```
> Hi My name is Jack
> I'm 36
> ```
> 

