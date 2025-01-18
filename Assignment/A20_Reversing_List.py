size = int(input('Enter size for list: '))
word = []
for _ in range(size):
    word.append(input('Enter a string: '))
reversed_list = word[::-1]
print(f'List = {word}\nReversed List = {reversed_list}')
