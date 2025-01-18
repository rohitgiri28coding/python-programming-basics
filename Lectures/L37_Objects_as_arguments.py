class Car:
    color = None


class Bike:
    color = None


def change_color(vehicle_obj, color):
    vehicle_obj.color = color


car_1 = Car()
bike_1 = Bike()

change_color(car_1, 'Black')
change_color(bike_1, 'Blue')

print(bike_1.color)
print(car_1.color)
