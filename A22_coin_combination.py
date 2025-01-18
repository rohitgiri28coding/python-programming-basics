def possible_combinations(n):
    x = True
    possible_cases = 2 ** n
    combinations = ['H' if i < possible_cases // 2 else 'T' for i in range(0, possible_cases)]
    for i in range(2, n + 1):
        for j in range(possible_cases):
            x = not x if j % (possible_cases // (2 ** i)) == 0 else x
            combinations[j] = combinations[j] + ('T' if x else 'H')
    return combinations


# def combo(n):
#     possible_cases = 2 ** n
#     combination = [''.join(['H' if j & (1 << (n - k - 1)) else 'T' for k in range(n)]) for j in range(possible_cases)]
#     return combination


num = int(input('enter number of coins to be flipped: '))

combination = possible_combinations(num)
# print(combo(num))
for k in combination:
    print(k)
