class Dog:

    type = "pet"

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def bark(self):
        print(self.name + " is barking")

    
class Labradog(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.__owner = "Goerge"

    def __repr__(self):
        return "Labradog object, name = {name}, age = {age}".format(name = self.name, age = self.age)

    def bark(self):
        super().bark()
        print(self.name + " is a Labradog")

    def changeOwner(self, newOwner):
        self.__owner = newOwner

    def printOwner(self):
        print("Labradog owner is {}".format(self.__owner))

class Bulldog(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)


    def bark(self):
         super().bark()
         print(self.name + " is a Bulldog")


def makeDogBark(dog):
    dog.bark()

doge = Dog("Doge", 15)
doge.bark()
print("Class Dog type = " + Dog.type)
# 2 ways
print("Class Dog type = " + doge.__class__.type)

labradog = Labradog("Rex", 8)
labradog.bark()
print(labradog.__class__.type)

labradog.printOwner()
labradog.changeOwner("Lewis")
labradog.printOwner()
labradog.__owner = "Max" # Doesn't work, __owner is private
labradog.printOwner()

bulldog = Bulldog("Vex", 6)
makeDogBark(labradog)
makeDogBark(bulldog)

print(labradog)

doge2 = Dog("Doge2", 30)
del doge2.age
print(doge.age)

doge.type = "animal"

print(Dog.type)
print(doge.type)
print(doge2.type)
