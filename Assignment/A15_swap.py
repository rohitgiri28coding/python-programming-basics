num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
print('Before swap x = ', num1, 'y = ', num2)
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print('After swap x = ', num1, 'y = ', num2)

# M2
num1, num2 = int(input('Enter a number: ')), int(input('Enter another number: '))
print('Before swap x = ', num1, 'y = ', num2)
num1, num2 = num2, num1
print('After swap x = ', num1, 'y = ', num2)
