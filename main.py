class Animal:
    def __init__(self, name, age, owner, docter) -> None:
        self.__name = name
        self.__age = age
        self.__owner = owner
        self.__docter = docter

    def __str__(self) -> str:
        return f"Я {self.__name} мне {self.__age} лет"

    def talk(self):
        pass

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

class Cat(Animal):
    def __init__(self, name: str, age: int, owner, docter, may: str):
        super().__init__(name, age, owner, docter)
        self.may = may

    def talk(self):
        print("мяу")

class Dog(Animal):
    def __init__(self, name: str, age: int, owner, docter, gaf: str):
        super().__init__(name, age, owner, docter)
        self.gaf = gaf

    def talk(self):
        print("гав")

cat1 = Cat("Васька", 5, "", "", "may")
dog1 = Dog("Васька", 5, "", "", "may")
cat1.talk()
dog1.talk()
# print(cat1.age)
# print(cat1.name)
# cat1._age = 1000
# print(cat1)
# cat2 = Cat("Барсик", 2)
# print(cat2)
# print(cat2.age)
# print(cat2.name)

# cat1.may(3)

# print(type(cat1))

