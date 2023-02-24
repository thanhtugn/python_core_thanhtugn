#1. Create a new class with some attributes and methods.
import datetime
class Vehicle:
    def __init__(self, name, max_speed=100, color='red', year=2020):
        self.name = name
        self._max_speed = max_speed
        self.__color = color
        self.__year = year

    def get_name(self):
        return self.name
    
    def get_max_speed(self):
        return self._max_speed
    
    def get_color(self):
        return self.__color
    
    def get_year(self):
        return self.__year
    
    def __call_yearold(self):
        year_old = datetime.datetime.now().year - self.__year
        return year_old
        
    def get_yearold(self):
        return self.__call_yearold()

    def set_color(self, color):
        self.__color = color

    def set_max_speed(self, max_speed):
        self._max_speed = max_speed

#2. Create child class
class Motor(Vehicle):
    def __init__(self, engine, name, max_speed=100, color='red',years=2020):
        self.__engine = engine
        super().__init__(name, max_speed, color, years)

    def get_engine(self):
        return self.__engine
        
    def get_max_speed(self):
        return super().get_max_speed() + 50






#Define a new object of child class 
# motor = Motor(110, 'Vision', 200, 'blue', 2022)
# print('__Motor Information__')
# print(f'name: {motor.get_name()}')
# print(f'max speed: {motor.get_max_speed()}')
# print(f'color: {motor.get_color()}')
# print(f'year: {motor.get_yearold()}')
# print(f'engine: {motor.get_engine()}')

#Define class Car which inherits from Vehicle 
class Car(Vehicle):
    def __init__(self, name, branch , engine,  max_speed=100, color='red', year=2020):
        self.__branch = branch
        self.__engine = engine
        super().__init__(name, max_speed, color, year)

    def get_branch(self):
        return self.__branch
    
    def get_yearold(self):
        return super().get_yearold() + 10
    
    def get_engine(self):
        return self.__engine

# car = Car('BMW I8', 'BMW','B38', 400, 'blue', 2022)
# print('__Car Information__')
# print(f'name: {car.get_name()}')
# print(f'branch: {car.get_branch()}')
# print(f'engine: {car.get_engine()}')
# print(f'max speed: {car.get_max_speed()}')
# print(f'color: {car.get_color()}')
# print(f'year: {car.get_yearold()}')

#4. Polymorphism

class Bird:
    def __init__(self):
        pass
    def intro(self):
        print('There are many types of birds here')

    def flight(self):
        print('Most of the birds can fly, some other can not')

class Eagle(Bird):
    def __init__(self):
        super().__init__()
        
    def flight(self):
        print('Eagle can fly')

class Ostrich(Bird):
    def __init__(self):
        super().__init__()

    def flight(self):
        print('Ostrich can not fly')

# bird = Bird()
# eagle = Eagle()
# ostrich = Ostrich()

# bird.intro()
# bird.flight()

# eagle.intro()
# eagle.flight()

# ostrich.intro()
# ostrich.flight()

#####################
# Polymorphism
class England:
    def capital(self):
        print('London is capital of England')

    def language(self):
        print('English is the language of England')

    def type_country(self):
        print('England is developed country')

class Vietnam:
    def capital(self):
        print('Hanoi is capital of Vietnam')

    def language(self):
        print('Vietnamese is the language of Vietnam')

    def type_country(self):
        print('Vietnam is developing country')

def func(obj):
    obj.capital()
    obj.language()
    obj.type_country()

# england = England()
# vn = Vietnam()
# for ct in [england, vn]:
#     func(ct)




# def add (a,b, c=10):
#     return a+b+c

# add(2,3,4)
# add(2,3)

#5. Abstraction
from abc import ABC, abstractmethod
class Polygon():
    @abstractmethod
    def no_of_sides(self):
        pass

class Triangle(Polygon):
    def no_of_sides(self):
        print('The triangle has 3 sides')

class Hexagon(Polygon):
    def no_of_sides(self):
        print('The hexagon has 6 sides')

trg = Triangle()
trg.no_of_sides()

hxg = Hexagon()
hxg.no_of_sides()



