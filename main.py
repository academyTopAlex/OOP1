from typing import List

class Person:
    pass

class Owner:
    def __init__(self, phone):
        self.phone = phone


class Docter:
    pass


class Animal:
    def __init__(self, name, age, owner: Owner, docter: Docter) -> None:
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

    def get_owner(self):
        return self.__owner

class Cat(Animal):
    count = 0

    def __init__(self, name: str, age: int, owner, docter, may: str):
        super().__init__(name, age, owner, docter)
        self.may = may
        Cat.count += 1

    def talk(self):
        print("мяу")


class Dog(Animal):
    def __init__(self, name: str, age: int, owner, docter, gaf: str):
        super().__init__(name, age, owner, docter)
        self.gaf = gaf

    def talk(self):
        print("гав")


cat1 = Cat("Васька", 5, Owner("55"), Docter(), "may")
cat2 = Cat("СерЛанцелап", 5, Owner("5454"), Docter(), "may")
dog1 = Dog("ВаськаПес", 5, Owner("5484848"), Docter(), "may")

# cat1.talk()
# dog1.talk()

lst: List[Animal] = []
lst.append(dog1)
lst.append(cat2)
lst.append(cat1)

for animal in lst:
    print(animal.get_owner().phone)


# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, var):
#         self.__stack_list.append(var)
#
#     def pop(self):
#         if len(self.__stack_list) != 0:
#             var = self.__stack_list[-1]
#             del self.__stack_list[-1]
#             return var
#
#     def __str__(self):
#         return str(self.__stack_list)
#
# stack1 = Stack()
#
#
# stack1.push(9)
# stack1.push(8)
# stack1.push(7)
# stack1.push(6)
# stack1.push(5)
#
# stack1.pop()
# stack1.pop()
# stack1.pop()
# stack1.pop()
# stack1.pop()
# stack1.pop()
#
# print(stack1)
