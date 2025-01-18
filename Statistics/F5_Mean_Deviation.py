from F2_Mean import mean
from F3_Median import median
from F4_Mode import mode


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
    m = mode(x, f, gap)
    x_minus_m = [abs(i - m) for i in x]
    fi_x_minus_m = [f[i] * x_minus_m[i] for i in range(len(f))]
    return (sum(fi_x_minus_m)) / (sum(f)), x_minus_m, fi_x_minus_m
