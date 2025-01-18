# Duck typing = concept where the class of an obj is less imp than the methods/attributes
#               class type is not checked if min methods/attributes are present
#               'if it walks like a duck, quack like a duck, then it must be a duck.'

class Duck:
    def walk(self):
        print('Duck is walking...')

    def talk(self):
        print('duck is quacking')


class Chicken:
    def walk(self):
        print('chicken is walking...')

    def talk(self):
        print('chicken is clucking')


class Person:
    def catch(self, duck_obj):
        duck_obj.talk()
        duck_obj.walk()
        print('You caught it.....')


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)           # if the chicken doesn't contain talk and walk which are used in person
#                                 then we can't use chicken obj
