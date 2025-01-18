# Like list, tuples are collection of items but,
# they are non-mutable in nature, so we can only find index and count elements

num = (1, 2, 3)
print(num)
print(num[0])

# Unpacking = can be used with tuples as well as with lists

x, y, z = num   # This is a shorthand for writing x = num[0], y = num[1], z = num[2]

print(x*y*x*z)

student1 = ('Rohit', 5.7, 20)
print(student1.count(20))
print(student1.index(5.7))
