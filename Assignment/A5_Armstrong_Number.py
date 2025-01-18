num1 = num = int(input('Enter a Number: '))
length = len(str(num))
temp = 0
if num1 > 0:
    for i in range(length):
        temp += (num1 % 10) ** length
        num1 = num1 // 10
if temp == num:
    print(f'{num} is an Armstrong number.')
else:
    print(f'{num} is not an Armstrong number.')
