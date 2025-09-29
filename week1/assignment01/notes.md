# Assignment #01

## #2.0 Hello World

```python
# Hello World program in Python
print("Hello World!")
```

## #2.1 Variables

### 파이썬 변수 규칙

- 이름에 공백 허용 X
- snake_case(스네이크 표기법) 사용 - 단어 사이 언더바
- 변수명 시작은 항상 문자로 시작 (숫자 불가능)

```python
a = 2
b = 3
c = a + b
a = 1
b = 10
print(c)
```

> **출력**: `5`
> 

**설명**: `c`는 처음 계산된 값(5)을 저장하므로, 이후 `a`와 `b`를 변경해도 `c`는 변하지 않음

## #2.2 Strings and Booleans

### String (문자열)

- 작은 따옴표(')나 큰 따옴표(")를 사용

```python
my_name = "yjkdev"
print(my_name)
```

### Boolean (참/거짓)

- 정확히 `True`, `False`로 작성 (첫 글자 대문자)

```python
is_active = True
print(is_active)
```

## #2.3 Recap

### print에서 변수와 문자열 혼용

```python
my_age = 20
print("hello I'm", my_age, "years old")
```

> **출력**: `hello I'm 20 years old`