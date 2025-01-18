def frequency(op, symbol):
    return op.count(symbol)


def delete_elements(index, number, operator, res):
    number.pop(index)
    number.pop(index)
    number.insert(index, res)
    operator.pop(index)
    return number, operator


def calculate(number, operator, symbol, freq):
    for _ in range(freq):
        index = operator.index(symbol)
        if symbol == '/':
            res = number[index] / number[(index + 1)]
            number, operator = delete_elements(index, number, operator, res)
        elif symbol == '*':
            res = number[index] * number[(index + 1)]
            number, operator = delete_elements(index, number, operator, res)
        elif symbol == '+':
            res = number[index] + number[(index + 1)]
            number, operator = delete_elements(index, number, operator, res)
        elif symbol == '-':
            res = number[index] - number[(index + 1)]
            number, operator = delete_elements(index, number, operator, res)
    return number, operator


def call(num, op):
    num, op = calculate(num, op, '/', frequency(op, '/'))
    num, op = calculate(num, op, '*', frequency(op, '*'))
    num, op = calculate(num, op, '-', frequency(op, '-'))
    num, op = calculate(num, op, '+', frequency(op, '+'))
    return num[0]
