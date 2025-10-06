# Assignment #07

# ========================================
# 5.1 Why We Need OOP
# ========================================

# 1. 캡슐화 (Encapsulation)
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
# print(account.__balance)  # 에러: 직접 접근 불가


# 2. 추상화 (Abstraction)
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


# 3. 다형성 (Polymorphism)
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


# ========================================
# 5.2 Classes
# ========================================

# Class: 설계도 또는 틀
# 특정 데이터(속성)와 그 데이터를 처리하는 함수(메서드)들을 묶어놓은 것
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


# Method: 클래스 내부에 정의된 함수
# 첫 번째 매개변수는 항상 self (자기 자신을 참조)
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):  # self는 필수!
        return f"안녕하세요, {self.name}입니다."

person = Person("홍길동")
print(person.greet())  # 안녕하세요, 홍길동입니다.


# ========================================
# 5.3 Methods
# ========================================

# __init__: 객체 생성 시 가장 먼저 자동으로 실행되는 메서드 (생성자)
class Puppy:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{name}이(가) 생성되었습니다!")

puppy = Puppy("바둑이", 3)  # 바둑이이(가) 생성되었습니다!


# __str__: print() 또는 str() 함수 사용 시 자동으로 호출되는 메서드
class Puppy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"강아지 {self.name}, {self.age}살"

puppy = Puppy("바둑이", 3)
print(puppy)  # 강아지 바둑이, 3살


# __repr__: 개발자를 위한 객체 표현
class Puppy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy(name='{self.name}', age={self.age})"

puppy = Puppy("바둑이", 3)
print(repr(puppy))  # Puppy(name='바둑이', age=3)


# __len__: len() 함수 사용 가능하게 함
class Classroom:
    def __init__(self, students):
        self.students = students

    def __len__(self):
        return len(self.students)

classroom = Classroom(["학생1", "학생2", "학생3"])
print(len(classroom))  # 3


# 인스턴스: 클래스를 통해 만들어진 실제 객체
# 하나의 클래스로 여러 개의 서로 다른 인스턴스 생성 가능
puppy1 = Puppy("바둑이", 3)  # 인스턴스 1
puppy2 = Puppy("초코", 1)    # 인스턴스 2
puppy3 = Puppy("뽀삐", 5)    # 인스턴스 3


# ========================================
# 5.4 Inheritance
# ========================================

# 상속: 부모 클래스의 속성과 메서드를 자식 클래스가 물려받는 것
# 코드 재사용성을 높이는 핵심 기능

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


# 메서드 오버라이딩 (Method Overriding)
# 자식 클래스에서 부모 클래스의 메서드를 재정의
class Dog:
    def speak(self):
        return "멍멍!"

class Puppy(Dog):
    def speak(self):  # 메서드 오버라이딩
        return "왈왈! (작은 소리)"

puppy = Puppy()
print(puppy.speak())  # 왈왈! (작은 소리)


# ========================================
# 5.5 Inheritance part Two | super()
# ========================================

# super(): 자식 클래스에서 부모 클래스의 메서드와 속성에 접근할 때 사용
# 부모 클래스를 참조하는 임시 객체를 반환

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


# super() 없이 사용한 경우 vs super() 사용
# super() 없이 (비추천)
class Puppy_Without_Super(Dog):
    def __init__(self, name, breed, age):
        Dog.__init__(self, name, breed)  # 부모 클래스 이름 직접 명시
        self.age = age

# super() 사용 (추천)
class Puppy_With_Super(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)  # 더 간결하고 유연함
        self.age = age