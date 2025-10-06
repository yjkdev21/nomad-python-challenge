# Assignment #07

<aside>

- #5.0 OOP
- #5.1 Why We Need OOP
- #5.2 Classes
- #5.3 Methods
- #5.4 Inheritance
- #5.5 Inheritance part Two | super()
</aside>

---

## #5.0 OOP

**객체 지향 프로그래밍 (Object Oriented Programming)**

- OOP는 파이썬뿐만 아니라 Java, C++, C#, JavaScript, TypeScript, Dart 등 다양한 언어에서 사용됨
- 프로그래밍 **패러다임**(paradigm) 중 하나 (단순한 "규칙"보다는 설계 철학에 가까움)
- 실세계의 개념을 객체로 모델링하여 직관적이고, 데이터와 동작(메서드)을 하나로 묶어 관리
- **재사용성**이 높고, **유지보수**가 편리함
- 새로운 기능 추가 시 기존 코드 변경을 최소화할 수 있어 **확장성**이 우수함

---

## #5.1 Why We Need OOP

**OOP의 주요 특징과 장점**

### **1. 캡슐화 (Encapsulation)**

- 데이터(속성)와 그 데이터를 처리하는 함수(메서드)를 하나의 객체로 묶음
- 외부로부터 데이터를 보호하고 접근 제어 가능 (private, public 등)
- 불필요한 세부 구현을 숨기고 필요한 인터페이스만 노출
- 결과: 코드 중복 감소, 데이터 일관성 유지

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private 속성 (__)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)  # 에러 직접 접근 불가

```

### **2. 추상화 (Abstraction)**

- 복잡한 세부 구현을 숨기고 필요한 기능만 외부에 제공
- 사용자는 "어떻게"보다 "무엇을"에 집중할 수 있음
- 예: 자동차 운전 시 엔진 내부 작동 원리를 몰라도 됨

```python
class Car:
    def start(self):
        self.__check_fuel()
        self.__start_engine()
        print("차량 시동 완료")

    def __check_fuel(self):  # 내부 구현 (사용자는 몰라도 됨)
        print("연료 확인 중...")

    def __start_engine(self):
        print("엔진 시동 중...")

my_car = Car()
my_car.start()  # 간단하게 시동만 걸면 됨

```

### **3. 상속 (Inheritance)**

- 기존 클래스의 속성과 메서드를 새로운 클래스가 물려받음
- 코드 재사용성 극대화
- 계층 구조로 관계를 명확히 표현 가능

### **4. 다형성 (Polymorphism)**

- 같은 인터페이스나 메서드가 다른 방식으로 동작 가능
- 메서드 오버라이딩(overriding), 오버로딩(overloading)
- 유연한 코드 작성 가능

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹~"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # 각각 다른 소리 출력

```

### **추가 장점**

- **이해 용이성**: 실세계 개념을 코드로 직관적으로 표현
- **구조적 구성**: 기능별로 객체를 나눠 체계적 관리
- **확장성**: 새 기능 추가 시 기존 코드 수정 최소화
- **협업 효율**: 모듈화된 구조로 팀 작업에 유리
- **유지보수성**: 버그 수정 및 기능 변경이 용이

---

## #5.2 Classes

**Class와 Method**

### **Class (클래스)**

- 특정 데이터(속성)와 그 데이터를 처리하는 함수(메서드)들을 묶어놓은 **설계도** 또는 **틀**
- 구체적인 데이터 값은 달라도 같은 구조와 행동을 하는 객체들을 생성하는 도구
- 예: `Puppy` 클래스를 만들면, 이를 통해 여러 개의 강아지 객체(인스턴스) 생성 가능

```python
class Puppy:
    # 클래스 속성 (모든 인스턴스가 공유)
    species = "강아지"

    def __init__(self, name, age):
        # 인스턴스 속성 (각 객체마다 다름)
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name}: 멍멍!"

# 인스턴스 생성
puppy1 = Puppy("바둑이", 3)
puppy2 = Puppy("초코", 1)

print(puppy1.bark())  # 바둑이: 멍멍!
print(puppy2.bark())  # 초코: 멍멍!

```

### **Method (메서드)**

- 클래스 내부에 정의된 함수
- 클래스의 데이터(속성)에 쉽게 접근하고 조작할 수 있음

### **Python 클래스 메서드 규칙**

1. 클래스 내부에서 정의되어야 함
2. 첫 번째 매개변수는 **항상 `self`**
    - `self`는 자기 자신(객체 인스턴스)을 참조함
    - 관례적 명명이지만 필수적으로 사용됨
    - 이를 통해 메서드 내에서 해당 객체의 속성에 접근 가능

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):  # self는 필수!
        return f"안녕하세요, {self.name}입니다."

person = Person("홍길동")
print(person.greet())  # 안녕하세요, 홍길동입니다.

```

---

## #5.3 Methods

**클래스 내장 메서드 (Special Methods / Magic Methods)**

### **`__init__` (Initialize - 초기화)**

- 객체 생성 시 **가장 먼저 자동으로 실행**되는 메서드
- 생성자(constructor)라고도 불림
- 인자를 전달하면 해당 값으로 객체의 초기 속성을 설정함

```python
class Puppy:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{name}이(가) 생성되었습니다!")

puppy = Puppy("바둑이", 3)  # 바둑이이(가) 생성되었습니다!

```

### **`__str__` (String - 문자열)**

- 객체를 `print()` 함수로 출력하거나 `str()` 함수로 변환할 때 **자동으로 호출**되는 메서드
- `__str__`의 반환값(문자열)이 출력됨
- 정의하지 않으면 기본값(메모리 주소)이 출력됨

```python
class Puppy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"강아지 {self.name}, {self.age}살"

puppy = Puppy("바둑이", 3)
print(puppy)  # 강아지 바둑이, 3살

```

### **기타 유용한 내장 메서드**

**`__repr__`**: 개발자를 위한 객체 표현

```python
class Puppy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy(name='{self.name}', age={self.age})"

puppy = Puppy("바둑이", 3)
print(repr(puppy))  # Puppy(name='바둑이', age=3)

```

**`__len__`**: len() 함수 사용 가능

```python
class Classroom:
    def __init__(self, students):
        self.students = students

    def __len__(self):
        return len(self.students)

classroom = Classroom(["학생1", "학생2", "학생3"])
print(len(classroom))  # 3

```

### **인스턴스 (Instance)**

- 클래스를 통해 만들어진 **실제 객체**
- 클래스는 설계도(청사진), 인스턴스는 그 설계도로 만든 **실체**
- 하나의 클래스로 여러 개의 서로 다른 인스턴스 생성 가능

```python
# Puppy 클래스(설계도)로 여러 인스턴스 생성
puppy1 = Puppy("바둑이", 3)  # 인스턴스 1
puppy2 = Puppy("초코", 1)    # 인스턴스 2
puppy3 = Puppy("뽀삐", 5)    # 인스턴스 3

```

---

## #5.4 Inheritance

**상속 (Inheritance)**

### **상속이란?**

- 부모 클래스(기본 클래스, Base Class)의 속성과 메서드를 자식 클래스(파생 클래스, Derived Class)가 물려받는 것
- OOP의 핵심 개념 중 하나로, **코드 재사용성**을 높이는 핵심 기능

### **상속의 장점**

- 중복 코드 작성을 최소화
- 코드 재사용성 향상
- 유연성과 확장성 증가
- 계층 구조를 통한 체계적인 코드 구조화

### **상속 문법**

```python
# 부모 클래스
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name}: 멍멍!"

# 자식 클래스 (Dog 클래스를 상속받음)
class Puppy(Dog):
    pass

# 사용
puppy = Puppy("바둑이")
print(puppy.bark())  # 바둑이: 멍멍! (부모의 메서드 사용)

```

### **메서드 오버라이딩 (Method Overriding)**

자식 클래스에서 부모 클래스의 메서드를 재정의

```python
class Dog:
    def speak(self):
        return "멍멍!"

class Puppy(Dog):
    def speak(self):  # 메서드 오버라이딩
        return "왈왈! (작은 소리)"

puppy = Puppy()
print(puppy.speak())  # 왈왈! (작은 소리)

```

### **용어 정리**

- **부모 클래스** = 기본 클래스 (Base Class) = 슈퍼 클래스 (Super Class)
- **자식 클래스** = 파생 클래스 (Derived Class) = 서브 클래스 (Sub Class)

---

## #5.5 **Inheritance part Two |** super()

### **super()란?**

- 자식 클래스에서 부모 클래스의 메서드와 속성에 접근할 때 사용하는 내장 함수
- 부모 클래스를 참조하는 임시 객체를 반환함

### **주요 사용 목적**

- 부모 클래스의 `__init__` 메서드 호출 (초기화 상속)
- 메서드 오버라이딩(재정의) 시 부모 클래스의 원본 메서드 호출
- 부모 클래스의 기능을 유지하면서 확장 가능

### **사용 예시**

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def info(self):
        return f"{self.name}는 {self.breed}입니다."

class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)  # 부모의 __init__ 호출
        self.age = age  # 자식 클래스만의 속성 추가

    def info(self):
        parent_info = super().info()  # 부모의 메서드 호출
        return f"{parent_info} 나이는 {self.age}살입니다."

puppy = Puppy("바둑이", "진돗개", 3)
print(puppy.info())
# 바둑이는 진돗개입니다. 나이는 3살입니다.

```

### **super() 없이 사용한 경우 vs super() 사용**

```python
# super() 없이 (비추천)
class Puppy(Dog):
    def __init__(self, name, breed, age):
        Dog.__init__(self, name, breed)  # 부모 클래스 이름 직접 명시
        self.age = age

# super() 사용 (추천)
class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)  # 더 간결하고 유연함
        self.age = age

```

### **장점**

- 부모 클래스 이름을 직접 명시하지 않아도 됨 (코드 유지보수 용이)
- 다중 상속 시 올바른 메서드 호출 순서(MRO, Method Resolution Order) 보장
- 코드 유지보수성 향상 (부모 클래스 이름 변경 시에도 수정 불필요)