def median(f, x, gap=0):
    if all(i == 1 for i in f):
        x.sort()
        if len(f) % 2 == 0:
            return [(x[len(f) // 2 - 1] + x[len(f) // 2]) / 2]
        else:
            return [x[(len(f)+1)//2-1]]
    else:
        cf = [sum([f[i] for i in range(j + 1)]) for j in range(len(f))]
        n_by_2 = cf[len(cf)-1] / 2
        index = 0
        for i in range(len(cf)):
            if cf[i] > n_by_2:
                index = i
                break
        return (x[index] * 2 - gap) / 2 + gap * (n_by_2 - cf[index - 1]) / f[index], cf


def quartiles(f, x, gap=0):
    if all(i == 1 for i in f):
        x.sort()
        return x[(len(x) + 1) / 4], x[(len(x) + 1) / 2], x[(len(x) + 1) * 0.75]
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
