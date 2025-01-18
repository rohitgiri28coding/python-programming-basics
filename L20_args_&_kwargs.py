# *args = parameter that will pack all argument into a tuple
#         useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


add(1, 2, 3, 4, 5, 6)


def multiply(*mul):
    prod = 1
    for i in mul:
        prod *= i
    print(prod)


multiply(1, 2, 3, 4, 5, 6)

# **kwargs = parameter that will pack all the arguments into a dictionary
#          useful so that  a function can accept a varying amount of keyword argument


def hello(**name):
    print('Hello '+name['first_name']+" "+name['last_name'])
    print("Good Morning",end=' ')
    for key,value in name.items():
        print(value, end=' ')


hello(title='Mr.', first_name='Rohit', last_name='Giri')
