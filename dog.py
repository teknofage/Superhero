class Dog:
    # Required properties are defined inside the __init__ constructor 
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    # Methods are defined as their own named functions inside the class
    def bark(self):
        print ("Woof!")

my_dog = Dog("Rex", "SuperDog")
my_dog.bark()
print(my_dog)
print(my_dog.name)
