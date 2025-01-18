from F2_Mean import mean


def standard_deviation(f, x):
    m = mean(f, x)[0]
    x_minus_mean = [(i - m) ** 2 for i in x]
    f_x_minus_mean = [f[i]*x_minus_mean[i] for i in range(len(f))]
    return (sum(f_x_minus_mean) / (sum(f))) ** 0.5, f_x_minus_mean, x_minus_mean
