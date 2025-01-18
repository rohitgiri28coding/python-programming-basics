# continuous indented statement after keywords like if, elif, else are considered inside it
# if 'if statement' is true elif statement or else statement will not execute

x = -10
if x >= 1:
    print('Number greater than 1')
    print('or equal to 1')
elif x == 0:
    print('Number equal to 0')
else:
    print('Number less than 0')
print('hi')
