# super() = Fn used to give access to the methods of a parent class
#           Returns a temporary obj of the parent class when used

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class Cube(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        self.height = length

    def volume(self):
        return super().area()*self.height


cube = Cube(5)
print(cube.volume())

sq_obj = Square(5)
print(sq_obj.area())

rect_obj = Rectangle(5, 2)
print(rect_obj.area())
