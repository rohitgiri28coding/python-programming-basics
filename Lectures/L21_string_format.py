first_name = "Rohit"
last_name = "Giri"
full_name = f"{first_name} {last_name} is a coder."  # Formatted string
print(full_name)

full_name = 'Name of coder is {} {}'.format(first_name, last_name)
print(full_name)
full_name = 'last name = {1}, first name = {0}'.format(first_name, last_name)  # Positional argument
print(full_name)

print('The {animal} is drinking {item}'.format(item='milk', animal='cow'))  # keyword argument

print('Hi, my name is {}.'.format(first_name))          # Normal formatting
print('Hi, my name is {:10}.'.format(first_name))       # Extra padding (room) for the formatted string
print('Hi, my name is {:<10}.'.format(first_name))      # Extra padding + left (default) alignment of formatted txt
print('Hi, my name is {:>10}.'.format(first_name))      # Extra padding + right alignment of formatted txt
print('Hi, my name is {:^10}.'.format(first_name))      # Extra padding + center alignment of formatted txt


num = 1000
pi = 3.142857

print('The number pi is {:.2f}'.format(pi))     # shows the decimal value up to two digits, else gets truncated
print('The number is {:,}'.format(num))         # adds a comma after every thousand
print('The number is {:b}'.format(num))         # shows no in binary
print('The number is {:o}'.format(num))         # shows no in octal
print('The number is {:x}'.format(num))         # shows no in hexadecimal (lower case)
print('The number is {:X}'.format(num))         # shows no in hexadecimal (upper case)
print('The number is {:e}'.format(num))         # shows no in scientific form (lower case)
print('The number is {:E}'.format(num))         # shows no in scientific form (upper case)
