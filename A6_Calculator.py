from array import *
entered_str = input('CALCULATOR\nEnter the expression: ')
entered_str = entered_str.replace(' ', '')
k = res = 0
for i in range(len(entered_str)):
    num = array('l')
    op = array('u')
    for j in range(len(entered_str)-1):
        if not (entered_str[k:(j + 1)]).isnumeric():
            op[i] = entered_str[j:j + 1]
            num[i] = int(entered_str[k:j])
            i += 1
            k = j
            break
        j += 1

