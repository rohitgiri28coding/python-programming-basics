# Prevents user from creating an object of the class
# + compels (forces to do sth) a user to override its abstract method in its child class

# abstract class  = class which contain one or more abstract classes
# abstract method = a method that has a declaration but does not have  an implementation

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod             # if this is not used method will not be considered abstract
    def start(self):
        pass

    def stop(self):
        pass


class Motorbike(Vehicle):
    def start(self):
        pass                        # This will do nothing


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print('Car stopped')


m_obj = Motorbike()
m_obj.start()

c_obj = Car()
c_obj.start()
c_obj.stop()