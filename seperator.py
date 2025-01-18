def separation(expression):
    num = []
    operator = []
    temp = 0
    for i in range(len(expression)):
        char = expression[i]
        if char.isdigit():
            temp = temp * 10 + int(char)
        elif char == ' ':
            continue
        else:
            num.append(temp)
            temp = 0
            operator.append(expression[i])
    num.append(temp)
    return num, operator
