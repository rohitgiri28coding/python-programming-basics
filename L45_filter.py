# filter() = creates a collection of elements from an iterable for which a fn returns true
# filter(fn, iterable)

candidates = [('Rohit', 24),
              ('Shikha', 28),
              ('Roshni', 24),
              ('Mohit', 14),
              ('Abhi', 17)]
adult_candidates = list(filter(lambda age: age[1] >= 18, candidates))
for i in adult_candidates:
    print(i)
