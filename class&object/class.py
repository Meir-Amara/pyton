class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.age}'

    def __add__(self,other):
        return "vvvvvv"


meir = Person("meir", 22)
x = meir+6
print(x)


