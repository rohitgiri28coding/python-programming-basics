numbers = [2, 15, 8, 7]
maximum = numbers[0]
for i in numbers:
    if maximum < i:
        maximum = i
print(maximum)
