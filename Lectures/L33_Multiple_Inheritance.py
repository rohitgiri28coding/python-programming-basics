class Prey:
    def running_away(self, animal):
        print("The "+animal+" is running away")


class Predator:
    def eating_flesh(self, name):
        print("The "+name+" is eating flesh")


class Rabbit(Prey):
    pass


class Fish(Prey, Predator):
    def running_away(self, animal):  # Overriding
        print('The fish is swimming away')


class Hawk(Predator):
    pass


fish_obj = Fish()
fish_obj.running_away('fish')
fish_obj.eating_flesh('fish')

