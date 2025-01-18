def mode(f, x, gap=0):
    if all(i == 1 for i in f):
        count = [x.count(i) for i in x]
        return x[count.index(max(count))]
    else:
        index = f.index(max(f))
        fm = f[index]
        fm_minus_1 = f[index-1]
        fm_plus_1 = f[index+1]
        lm = (x[index] * 2 - gap)/2
        return lm + gap * (fm - fm_minus_1)/(fm * 2 - fm_minus_1 - fm_plus_1)
