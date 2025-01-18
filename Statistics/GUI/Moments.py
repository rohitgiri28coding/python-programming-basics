def moments(f, x, gap, n):
    nby2 = len(x) // 2-1
    A = x[nby2]
    d = [(x[i] - A) / gap for i in range(len(x))]  # only applicable when ci is given
    moment = []
    d_set = []
    f_d_set = []
    for i in range(1, n+1):
        newd = [j**i for j in d]
        f_newd = [f[j]*newd[j] for j in range(len(f))]
        moment.append(round(sum(f_newd)/sum(f), 2))
        d_set.append(newd)
        f_d_set.append(f_newd)
    return moment, d_set, f_d_set


def input_xi():
    n = int(input('enter no of observations: '))
    gap = 0
    if input('If the data is given in Class interval input 1; otherwise, type any other character: ') == '1':
        start_value = int(input('enter start value: '))
        gap = float(input('Enter gap (upper limit - lower limit): '))
        x = [(start_value * 2 + gap) / 2]
        for i in range(1, n):
            x.append((x[i - 1] + gap))
    else:
        x = [int(input(f'Enter x for {i + 1}th observation: ')) for i in range(n)]
    return x, gap


x, gap = input_xi()
moments(1, x, gap)
