# lambda function = function written in 1 line using lambda keyword
#                   accepts any no of arg, but only has one expression
#                   useful when needed for a short period of time, throw-away

#  fn_name = lambda arg: operation

mul = lambda x, y: x * y
print(mul(5, 2))
full_name = lambda first, last: first + " " + last
print(full_name('Rohit', 'Giri'))
age_check = lambda age: True if age >= 18 else False
print(age_check(int(input('What is your age: '))))
