# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda fn, enhances readability of the code

#           SYNTAX

#                       list = [ expression for item in iterable ]
#                       list = [ expression for item in iterable if condition]
#                       list = [ expression if/else for item in iterable ]

# Calculating square
squares = []

# M1 using for loop
for i in range(1, 11):
    squares.append(i*i)
print(squares)


# M2 using list comprehension (uses less line of code)
print(squares := [i*i for i in range(1, 11)])


# Filtering passed students
students = [100, 68, 45, 85, 75, 68, 26, 23]

# M1 using filter fn
print(passed_students := list(filter(lambda x: x >= 33, students)))


# M2 using list comprehension (enhances readability)
print(passed_student := [i for i in students if i >= 33])

# M3 or by using if/else

print(pass_student := [i if i >= 33 else "FAILED" for i in students])








