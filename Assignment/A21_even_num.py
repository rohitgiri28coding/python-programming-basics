size = int(input('enter no of elements: '))
data = [input('enter a num: ') for _ in range(size)]
even_num = []
odd_num = []
for i in data:
    if i.isdigit():
        if int(i) % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)
    else:
        pass
print(even_num)
print(odd_num)
