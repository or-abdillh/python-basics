class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

mina = Person("Mina", 25)
mina.greet()

aulia = Person("Aulia", 30)
aulia.greet()