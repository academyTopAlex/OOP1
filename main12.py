from abc import ABC
import time
from typing import List


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


# for oneClass in [Vehicle, LandVehicle, TrackedVehicle]:
#     for twoClass in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(isinstance(oneClass(), twoClass))
#     print("-" * 50)

class SampleClass:
    def __init__(self, val):
        self.val = val


# ob1 = SampleClass(0)
# ob2 = SampleClass(2)
# ob3 = ob1
# ob3.val += 1
# print(ob1 is ob2)
# print(ob2 is ob3)
# print(ob3 is ob1)
# print(ob1.val, ob2.val, ob3.val)
# class Class1:
#     def __str__(self):
#         return "1"
#
#
# class Class2(Class1):
#     def __str__(self):
#         return "2"
#
#
# class Class3(Class2):
#     pass
#
#
# x = Class3()
# print(x)

class Human:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.age = age

    def __str__(self):
        return f"{self.__name} {self.age}"

    def add_age(self):
        self.age += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, v):
        if self.check_name(v):
            self.__name = v
        else:
            raise Exception("!!!")

    def check_name(self, v):
        pass


# h = Human("1", 78)
# h.name = "jhfj"
# h.age = ""
# h.add_age()


class BuilderABC(ABC):
    def build(self):
        print("построил")


class Builder(Human, BuilderABC):
    def __init__(self, name: str, age: int, x):
        super().__init__(name, age)
        self.__x = x


class Sailor(Human):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def run(self):
        print("пошел")


class Pilot(Human):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def fly(self):
        print("полетел")


# builder = Builder("builder", 20)
# sailor = Sailor("Sailor", 25)
# pilot = Pilot("Pilot", 30)
#
# lst: List[BuilderABC] = [builder]
#
# for human in lst:
#     print(human.build())


class Left:
    var = "L"
    varLeft = "LL"

    def fun(self):
        return "Left"


class Right:
    var = "R"
    varRight = "RR"

    def fun(self):
        return "Right"


class Sub(Right, Left):
    pass


#
# obj = Sub()
# print(obj.var, obj.varLeft, obj.varRight, obj.fun())

def printExcTree(thisclass, nest=0):
    if nest > 1:
        print(" |" * (nest - 1), end="")
    if nest > 0:
        print(" +---", end="")
    print(thisclass.__name__)
    for subclass in thisclass.__subclasses__():
        printExcTree(subclass, nest + 1)


# printExcTree(BaseException)


# class Passport:
#     def __init__(self, number, date):
#         self.__number = number
#         self.__date = date
#
#
# passport = Passport()
# passport.number = 5454
# passport.date = "12.12.2023"
#
# print(passport.data, passport.number)
# print(passport)

class Controller(ABC):
    def changedirection(self, left, on):
        pass


class Controller1(Controller):
    def changedirection(self, left, on):
        print("tracks: ", left, on)


class Controller2(Controller):
    def changedirection(self, left, on):
        print("wheels: ", left, on)


class Car:
    x = 0

    def __init__(self, controller: Controller, type: str):
        self.controller = controller
        self.type = type

    def turn(self, left):
        self.controller.changedirection(left, True)
        time.sleep(0.25)
        self.controller.changedirection(left, False)


# car1 = Car|ue)


# class Worcer:
#     pass
#
# class WorcerLib:
#     pass
#
# class Controler:
#     pass

# class Test:
#     x = None
#
#     def __init__(self, n):
#         self.num = n
#
#     @staticmethod
#     # def create_obg():
#     #     if Test.x is None:
#

# print(t1.x, t2.x, t3.x)
# print(t1.num, t2.num, t3.num)
# Test.x = 1
# t3.num = 9899
# print(t1.x, t2.x, t3.x)
# print(t1.num, t2.num, t3.num)
#


class MyMath:
    count = 0

    @staticmethod
    def pl1(x, y, h):
        MyMath.count += 1
        return 0.5 * h

    @staticmethod
    def pl2(x, y, h):
        MyMath.count += 1
        return 0.5 * h

    @staticmethod
    def pl3(x, y, h):
        MyMath.count += 1
        return 0.5 * h


MyMath.pl1(1, 1, 5)
MyMath.pl1(1, 1, 5)
MyMath.pl1(1, 1, 5)
MyMath.pl1(1, 1, 5)
MyMath.pl1(1, 1, 5)
print(MyMath.count)
