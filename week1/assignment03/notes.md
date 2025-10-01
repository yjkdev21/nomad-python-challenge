# Assignment #03

## #2.9 Default Parameters

- 매개변수에 기본값을 설정하면 인수 없이도 함수 호출 가능

```python
def say_hello_user(user_name="Guest"):
    print("hello, " + user_name)

say_hello_user()
say_hello_user("Alice")
```

> **출력:**
> 
> 
> `hello, Guest`
> 
> `hello, Alice`
> 

### 실습: 사칙연산 및 제곱 함수

```python
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
```

> **출력:**
> 
> 
> ```
> 5
> 2
> 12
> 5.0
> 8
> 2
> 0
> 1
> 1.0
> 1
> ```
> 

## #2.10 - #2.11 Return Values

- 함수가 결과값을 반환할 때 사용
- return을 만나면 함수가 종료됨

```python
# 반환
def tax_calc(money):
    return money * 0.35
    # 아래 문장은 실행 안됨
    print("Your money")

def pay_tax(tax):
    print("Thank you for paying", tax)

# 반환값을 다른 함수에 전달
pay_tax(tax_calc(100000))
```

> **출력:** `Thank you for paying 35000.0`
> 

### 문자열 포맷팅

- 문자열 앞에 `f`를 붙여서 사용
- 변수를 중괄호 `{}`로 표현

```python
# 포맷된 문자열을 반환
def coffee(coffee_type):
    return f"Enjoy your {coffee_type} coffee!"

print(coffee("espresso"))

# print 실행 결과를 반환 (None)
def tea(tea_type):
    return print(f"Enjoy your {tea_type} tea!")

tea("green")
```

> **출력:**
> 
> 
> `Enjoy your espresso coffee!`
> 
> `Enjoy your green tea!`
> 

## #3.0 - #3.2 If & Else & Elif

### if 문

- 조건이 참일 때 코드 실행

```python
if 10 < 4:
    print("10 < 4 Correct")

if 10 > 4:
    print("10 > 4 Correct")

if 10 == 10:
    print("10 == 10 Correct")

a = "hello"

if a == "hello":
    print("a is hello")
```

> **출력:**
> 
> 
> ```
> 10 > 4 Correct
> 10 == 10 Correct
> a is hello
> ```
> 

### Else & Elif

- elif: 이전 조건이 거짓일 때 다음 조건 확인
- else: 모든 조건이 거짓일 때 실행
- 조건 중 하나가 참이 되면 해당 코드만 실행하고 나머지는 확인하지 않음

```python
winner = 200

if winner > 50:
    print("You win!") # 출력
elif winner > 100:
    print("You top score!")
elif winner < 50:
    print("You lose!")
else:
    print("It's a tie!")
```

> **출력:** `You win!`
>