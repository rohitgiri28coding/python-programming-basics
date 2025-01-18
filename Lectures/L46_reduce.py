# reduce() = apply a fn to an iterable and reduce it to a single cumulative value
#            performs fn on first two elements and repeats its process until only 1 value remains


import functools
letters = ['h', 'e', 'l', 'l', 'o']
word = functools.reduce(lambda x, y: x+y, letters)
print(word)

num = [6, 5, 4, 3, 2, 1]
fact = functools.reduce(lambda x, y: x * y, num)
print(fact)

