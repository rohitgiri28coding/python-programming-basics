# multiplying 2 list with each other's corresponding elements and if there is no corresponding element mul 1
size1 = int(input('enter size for list1: '))
num1 = [int(input('Enter a number: ')) for _ in range(size1)]
size2 = int(input('enter size for list2: '))
num2 = [int(input('Enter a number: ')) for _ in range(size2)]
l3 = []
for i in range(max(size1, size2)):
    if size2 == size1:
        l3.append(num1[i]*num2[i])
    elif i >= max(size1, size2) - 1 and max(size1, size2) == size1:
        l3.append(num1[i])
    elif i >= max(size1, size2) - 1 and max(size1, size2) == size2:
        l3.append(num2[i])
    else:
        l3.append(num1[i]*num2[i])
print(f'{num1} * {num2} = {l3}')

# using list comprehension and zip function
size1 = int(input('Enter size for list1: '))
num1 = [int(input('Enter a number: ')) for _ in range(size1)]

size2 = int(input('Enter size for list2: '))
num2 = [int(input('Enter a number: ')) for _ in range(size2)]

# Ensure both lists have the same length by appending 1 to the shorter list
num1 += [1] * (size2 - size1) if size1 < size2 else []
num2 += [1] * (size1 - size2) if size2 < size1 else []

l3 = [a * b for a, b in zip(num1, num2)]

print(f'{num1} * {num2} = {l3}')
