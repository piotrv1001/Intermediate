class Person:

    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    @classmethod
    def howManyPeople(cls):
        return cls.counter

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print("Name = {name}, age = {age}".format(name = self.name, age = self.age))


print(Person.isAdult(21))
li = [Person("Name", 20) for _ in range(10)]
print(Person.howManyPeople())

peter = Person("Peter", 21)
peter.display()

print(Person.mro()) # Method Resolution Order