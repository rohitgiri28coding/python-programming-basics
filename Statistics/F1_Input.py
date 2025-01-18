def input_fi():
    global n
    n = int(input('Enter the total number of observations: '))
    if input('If the frequency is entirely 1, input 1; otherwise, type any other character: ') == '1':
        f = [1 for _ in range(n)]
    else:
        f = [int(input(f'Enter frequency for {i+1}th observation: ')) for i in range(n)]
    return f


def input_xi():
    gap = 0
    if input('If the data is given in Class interval input 1; otherwise, type any other character: ') == '1':
        start_value = int(input('enter start value: '))
        gap = float(input('Enter gap (upper limit - lower limit): '))
        x = [(start_value * 2 + gap)/2]
        for i in range(1, n):
            x.append((x[i-1] + gap))
    else:
        x = [int(input(f'Enter x for {i+1}th observation: ')) for i in range(n)]
    return x, gap
