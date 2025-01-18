# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Animal:
    def eat(self):
        print('The animal started eating.')
        return self

    def digest(self):
        print('The animal started digesting')
        return self


animal_obj = Animal()
animal_obj.eat().digest()           # animal_obj.eat() after execution returned self == animal_obj
#                                     then the expression became animal_obj.digest()

# Another way of writing animal_obj.eat().digest()
animal_obj.eat()\
    .digest()

