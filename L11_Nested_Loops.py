# the inner loop will complete all it's iterations before the completion of one iteration of outer loop

num = [5, 2, 5, 2, 2]
for i in num:
    print('x' * i)

#        OR

for i in num:
    output = ''
    for j in range(i):
        output += 'x'
    print(output)
