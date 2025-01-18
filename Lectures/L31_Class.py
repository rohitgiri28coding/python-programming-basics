# Name of class should follow CamelCase
# self is equivalent to this
# __init__ is the constructor for the class

class Car:
    wheels = 4                                                  # class variable

    def __init__(self, model, color):                           # constructor
        self.model = model
        self.color = color

    def start(self):
        print('car started....dhrung dhrung')

    def stop(self):
        print('car has been stopped')


car1 = Car('Nano', 'Black')
print(car1.color)
print(car1.model)
car1.wheels = 2
print(car1.wheels)
car1.start()
car1.stop()

car2 = Car('kivi', 'blue')
print(car2.color)
print(car2.model)
print(car2.wheels)
car2.start()
car2.stop()

# The _init() method is a special method in Python classes, and it serves as the constructor for the class.
# It is automatically called when an object of the class is created.
# The purpose of the __init_() method is to initialize the attributes (or properties) of the object.
# The method is defined with the name _init_ and takes at least one parameter,
# conventionally named self, which refers to the instance of the class being created.
# It is used to initialize the state of the object by assigning initial values to its attributes.
# You can define the _init_() method to accept additional parameters besides self,
# allowing you to pass values during object creation and use them to set specific attributes.
# The _init() method is optional in a class. If it is not defined,
# the class still inherits the __init_() method from its parent class (if any).
# You can overload the _init_() method by defining multiple versions with different parameter signatures,
# allowing for different ways to initialize the object.
