size = int(input('Enter size for list: '))
num = []
for _ in range(0, size):
    num.append(int(input('Enter a number: ')))
print(f'List = {num}\nMaximum number in the list = {max(num)}\nMinimum number in the list = {min(num)}')

#  using list comprehension
size = int(input('Enter size for list: '))
num = [int(input('Enter a number: ')) for _ in range(size)]
print(f'List = {num}\nMaximum number in the list = {max(num)}\nMinimum number in the list = {min(num)}')
