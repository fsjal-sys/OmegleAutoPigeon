class Person:
    #initial features
    def __init__(self, age, weight, height, name):
        self.age = age
        self.weight = weight
        self.height = height
        self.name = name

    def walk(self):
        print(self.name+" is walking")

user = Person(25, 80, 180, "Jon Truman")

print(user.age)
user.walk()
