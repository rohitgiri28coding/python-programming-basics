# index operator [] = give access to a sequence's element (str, list, tuples)

name = "rohit giri"
if name[0].islower():
    name = name.capitalize()
print(name)

first_name = name[:5].upper()
# second_name = name[6:].lower()
second_name = name[-4:].lower()
print(first_name)
print(second_name)
print(name[-1])
