# functions = a block of code which is executed only when it is called
# Functions should be defined before calling and if it's called before defining it, it will give an error
# For eg: is fn is defn in  line 5 and is called in line 2 it will give error
# Functions can be parameterized. def fn_name(variable_name)
# Arguments passed during function call can be positional or keyword arguments
def say_hello():
    print('Hello')


say_hello()


def greet(name, num):
    print(('Hi, Good Morning ' + name + "\n") * num)


greet(input("Enter your name: "), 3)  # Positional argument: if the position of name and num is changed it matters
greet(num=2, name='Rohit')  # In Keyword arguments position does not matter.
#                           # It enhances readability of code
#                           # If we want to use both arguments,
#                            we should use positional argument before the keyword argument
greet('Rohit', num=1)  # Error: fn(5, name='Rohit')   Or  fn(name='Rohit',5)


def sq(num):
    return num * num


print(sq(int(input('Enter a number: '))))

print(say_hello())  # It will print None at the end as the say_hello() fn doesn't have a return type



