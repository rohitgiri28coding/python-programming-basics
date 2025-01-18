# Lines which may produce error is written in try block and to handle it we write except block
# Exception are the events occurred during the execution that interrupts the normal flow of program

try:
    age = int(input("Enter your age: "))
    income = 1000
    print(income/age)
except ValueError:
    print('Invalid age')
except ZeroDivisionError:
    print('Age cannot be zero')


try:
    print(1000/int(input('Enter a num to divide 1000: ')))
except Exception:
    print('Wrong input')
finally:
    print('Thank You!')
