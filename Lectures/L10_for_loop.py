# for loop = a statement that will execute its block of code only for a limited no of times
# for loop = limited iteration
# while loop = can be iterated unlimited times


for first_name in 'Rohit':
    print(first_name)
for last_name in ['G', 'i', 'r', 'i']:
    print(last_name)
for num in range(0, 20, 2):
    print(num)

# break, continue, pass

# break = terminates the loop entirely
# continue = skips to the next iteration
# pass = does nothing, acts as a placeholder

# Using break keyword
while True:
    name = input('Enter your name: ')
    if name != '':
        break
print('Hi '+name)

# Using continue keyword
for num in range(0, 11):
    if num == 5:
        continue
    print(num)

# Using pass keyword
for num in range(0, 10):
    if num == 4:
        pass
    else:
        print(num)

