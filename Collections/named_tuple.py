from collections import namedtuple

Point = namedtuple("Point", "x y z")
p1 = Point(1, 2, 3)
print(p1)

Student = namedtuple("Student", ["name", "age"])
s1 = Student("Peter", 21)
print(s1)
print("Name of student is: {name}".format(name = s1.name))
print(s1._fields)
s2 = s1._replace(name = "Tom")
print(s2.name)

Car = namedtuple("Car", "brand age color topSpeed")
c1 = ["BMW", 10, "White", 270.5]
bmw = Car._make(c1)
print(bmw.topSpeed)