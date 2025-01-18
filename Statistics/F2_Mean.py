import math


def mean(f, x):
    summation_fi = sum(f)
    fi_xi = [f[i] * x[i] for i in range(len(f))]
    summation_fi_xi = sum(fi_xi)
    return summation_fi_xi/summation_fi, fi_xi


def geometric_mean(x, f):
    logx = [math.log10(i) for i in x]
    fi_logx = [f[i] * logx[i] for i in range(len(f))]
    summation_fi_logx = sum(fi_logx)
    summation_fi = sum(f)
    return 10 ** (summation_fi_logx / summation_fi), fi_logx


def harmonic_mean(f, x):
    summation_fi = sum(f)
    fi_by_xi = [f[i] / x[i] for i in range(len(f))]
    summation_fi_by_xi = sum(fi_by_xi)
    return summation_fi/summation_fi_by_xi, fi_by_xi
