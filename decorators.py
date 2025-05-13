# a simple decorator
def decorator(func):

    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    
    return wrapper

def method_decorator(func):

    def wrapper(self, *args, **kwargs):
        print("Before calling the function")
        func(self)
        print("After calling the function")

    return wrapper

def class_decorator(cls):

    cls.class_name = cls.__name__

    return cls

# simple class with decorator

@class_decorator

class Person: 

    def __init__(self, **args):
        self._name = args.get("name")
        self._born_year = args.get("born_year")

    @staticmethod
    def say_hello():
        print("Hello")

    @property
    def born_year(self):
        return self._born_year

    @born_year.setter
    def born_year(self, value):
        if value > 0:
            self._born_year = value
        else:
            raise ValueError("Born year must be grater than zero")

    @property
    def age(self):
        return 2025 - self._born_year

# instance new persons
mina = Person(name = "Mina Fitria", born_year = 2001)

# say hello
Person.say_hello()

# Born year and ages
print(mina.age)
print(mina.born_year)
mina.born_year = 2002
print(mina.age)