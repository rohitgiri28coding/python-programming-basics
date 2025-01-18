import math


def input_fi():
    global n
    n = int(input('Enter the total number of observations: '))
    if input('If the frequency is entirely 1, input 1; otherwise, type any other character: ') == '1':
        f = [1 for _ in range(n)]
    else:
        f = [int(input(f'Enter frequency for {i + 1}th observation: ')) for i in range(n)]
    return f


def input_xi():
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


def mean(f, x):
    summation_fi = sum(f)
    fi_xi = [f[i] * x[i] for i in range(len(f))]
    summation_fi_xi = sum(fi_xi)
    return summation_fi_xi / summation_fi, fi_xi


def geometric_mean(f, x):
    logx = [math.log10(i) for i in x]
    fi_logx = [f[i] * logx[i] for i in range(len(f))]
    summation_fi_logx = sum(fi_logx)
    summation_fi = sum(f)
    return 10 ** (summation_fi_logx / summation_fi), fi_logx


def harmonic_mean(f, x):
    summation_fi = sum(f)
    fi_by_xi = [f[i] / x[i] for i in range(len(f))]
    summation_fi_by_xi = sum(fi_by_xi)
    return summation_fi / summation_fi_by_xi, fi_by_xi


def median(f, x, gap=0):
    if all(i == 1 for i in f):
        x.sort()
        if len(f) % 2 == 0:
            return (x[len(f) // 2 - 1] + x[len(f) // 2]) / 2, x
        else:
            return x[(len(f) + 1) // 2 - 1], x
    else:
        cf = [sum([f[i] for i in range(j + 1)]) for j in range(len(f))]
        n_by_2 = cf[len(cf) - 1] / 2
        index = 0
        for i in range(len(cf)):
            if cf[i] > n_by_2:
                index = i
                break
        return (x[index] * 2 - gap) / 2 + gap * (n_by_2 - cf[index - 1]) / f[index], cf


def quartiles(f, x, gap=0):
    if all(i == 1 for i in f):
        x.sort()
        return x[math.floor(len(x) / 4 + 0.9)], x[math.floor(len(x) / 2 + 0.9)], x[math.floor(len(x) * 0.75 + 0.9)]
    else:
        cf = [sum([f[i] for i in range(j + 1)]) for j in range(len(f))]
        n_by_4 = sum(f) / 4
        index = []
        for i in range(len(cf)):
            if cf[i] > n_by_4:
                index.append(i)
            elif cf[i] > (n_by_4 * 2):
                index.append(i)
            elif cf[i] > (n_by_4 * 3):
                index.append(i)
        return (x[index[0]] * 2 - gap) / 2 + gap * (n_by_4 - cf[index[0] - 1]) / f[index[0]], (
                x[index[1]] * 2 - gap) / 2 + gap * (n_by_4 * 2 - cf[index[1] - 1]) / f[index[1]], (
                       x[index[2]] * 2 - gap) / 2 + gap * (n_by_4 * 3 - cf[index[2] - 1]) / f[index[2]], cf


def mode(f, x, gap=0):
    if all(i == 1 for i in f):
        count = [x.count(i) for i in x]
        if all(i == 1 for i in f):
            return 'No Mode'
        return x[count.index(max(count))]
    else:
        if len(set(f)) == 1:
            return 'No Mode'
        index = f.index(max(f))
        fm = f[index]
        fm_minus_1 = f[index - 1]
        fm_plus_1 = f[index + 1]
        lm = (x[index] * 2 - gap) / 2
        return lm + gap * (fm - fm_minus_1) / (fm * 2 - fm_minus_1 - fm_plus_1)


def mean_deviation_about_mean(f, x):
    m = mean(f, x)[0]
    mean_deviation = [abs(i - m) for i in x]
    fi_mean_deviation = [f[i] * mean_deviation[i] for i in range(len(f))]
    return (sum(fi_mean_deviation)) / (sum(f)), mean_deviation, fi_mean_deviation


def mean_deviation_about_median(f, x, gap=0):
    m = median(f, x, gap)[0]
    x_minus_m = [abs(i - m) for i in x]
    fi_x_minus_m = [f[i] * x_minus_m[i] for i in range(len(f))]
    return (sum(fi_x_minus_m)) / (sum(f)), x_minus_m, fi_x_minus_m


def mean_deviation_about_mode(f, x, gap=0):
    m = mode(f, x, gap)
    x_minus_m = [abs(i - m) for i in x]
    fi_x_minus_m = [f[i] * x_minus_m[i] for i in range(len(f))]
    return (sum(fi_x_minus_m)) / (sum(f)), x_minus_m, fi_x_minus_m


def standard_deviation(f, x):
    m = mean(f, x)[0]
    x_minus_mean = [(i - m) ** 2 for i in x]
    f_x_minus_mean = [f[i] * x_minus_mean[i] for i in range(len(f))]
    return (sum(f_x_minus_mean) / (sum(f) - 1)) ** 0.5, f_x_minus_mean, x_minus_mean


f = input_fi()
l = input_xi()
x = l[0]
gap = l[1]
print(mean(f, x))
# print(harmonic_mean(f, x))
# print(geometric_mean(f, x))
# print(median(f, x, gap))
# print(quartiles(f, x, gap))
# print(mode(f, x, gap))
print(mean_deviation_about_mean(f, x))
print(mean_deviation_about_median(f, x, gap))
print(mean_deviation_about_mode(f, x, gap))
print(standard_deviation(f, x))
