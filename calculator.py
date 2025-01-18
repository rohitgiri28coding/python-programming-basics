from seperator import separation
from calculation import *

exp = input('Enter expression: ')
number, operator = separation(exp)
print(number)
print(operator)
answer = call(number, operator)
print(answer)
