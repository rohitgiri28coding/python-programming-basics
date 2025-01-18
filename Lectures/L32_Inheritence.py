#               Animal
#                 ^
#                 |
#                 |
#                 |
#                 |
#                Cow
#                 ^
#                 |
#                 |
#                 |
#                 |
#                Cow
# Multi level Inheritance
class Animal:                       # Animal class is subclassed by cow class

    def walk(self, name):
        print('The '+name+' is walking.')

    def eat(self, name):
        print('The '+name+' is eating.')

    def sleep(self, name):
        print('The '+name+' is sleeping')


class Cow(Animal):                  # cow class is the child class of animal class
    pass


cow_obj = Cow()
cow_obj.eat('cow')
cow_obj.sleep('cow')
cow_obj.walk('cow')


class Calf(Cow):
    pass


calf_obj = Calf()
calf_obj.walk('calf')
