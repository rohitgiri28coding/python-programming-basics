def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)


try:
    number = int(input('Enter a number: '))
    if number < 0:
        raise ValueError()
    print(fact(number))
except ValueError:
    print('Enter a whole number, to calculate factorial.')
