# list = used to store multiple items in a single variable

names = ['Rohit', 'Shikha', 'Swati', 'Abhishek', 'Kanhaiya', 'Sanju', 'Kusum', 10]
print(names)
print(names[0:])
print(names[1:-1])
print(names[1])
for n in names:
    print(n)
names.remove(10)     # Removes the element
names.insert(7, 10)  # Inserts a element in the given index
names.pop()          # Removes the last element
names.sort()         # Arranges the list alphabetically
print(names)
names.clear()        # Removes all the element of the list

# append vs extend keyword
# The append() method is used to add a single element to the end of a list.
# It modifies the original list by appending the element as a single item.

# The extend() method is used to add multiple elements to the end of a list.
# It takes an iterable (such as a list or tuple) as an argument
# and appends each element individually to the original list.
