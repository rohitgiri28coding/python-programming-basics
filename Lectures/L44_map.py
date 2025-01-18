# map() = applies a function to each item in an iterable(list, tuple, etc.)

# map(fn, iterable)

store = [('Shirt', 1000),
         ('Trouser', 2000),
         ('Pants', 3000),
         ('Tie', 500)]
to_usd = lambda data: (data[0], '{:.2f}'.format((data[1]/82)))
to_inr = lambda data: (data[0], data[1]*82)

store_dollars = list(map(to_usd, store))
store_inr = list(map(to_inr, store))
for i in store_dollars:
    print(i)
for i in store_inr:
    print(i)
