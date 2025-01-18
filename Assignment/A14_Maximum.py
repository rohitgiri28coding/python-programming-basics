def find_max(numbers):
    numbers.sort(reverse=True)
    return numbers[0]


num = [10, 5, 8, 9, 45, 75, 100]
print(max(num))
print(find_max(num))
