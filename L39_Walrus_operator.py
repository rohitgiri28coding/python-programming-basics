# walrus operator :=
# assigns value to variables as part of large exp
# also known as assignment expression

food = list()

while item := input('What item do you like to eat: ').lower() != 'stop':
    food.append(item)
