# Warning; the code actually changes the original list
num = [10, 8, 7, 6, 6, 6, 11, 9, 10, 8]
for i in num:
    if num.count(i) > 1:
        num.remove(i)
print(num)


#       OR


num = [11, 11, 11, 18, 161, 15, 15, 17]
uniques = []
for i in num:
    if i not in uniques:
        uniques.append(i)
print(uniques)
