def show(items):
    for i in items:
        print(i)
    print('-----------')


# sort method only works for lists
students = ['Rohit', 'Shikha', 'Swati', 'Abhishek', 'Roshni']
students.sort()                         # sorts the list alphabetically
show(students)
students.sort(reverse=True)             # sorts in reverse order
show(students)

# sorted fn can be used with tuples, dictionary, list, etc. w
student = ('Rohit', 'Shikha', 'Swati', 'Abhishek', 'Roshni')
sorted_students = sorted(student)
show(sorted_students)
sorted_students = sorted(student, reverse=True)
show(sorted_students)
sorted_student = sorted(students)
show(sorted_student)

# sorting a list of tuples

candidates = [('Rohit', 25, 'A++'),
              ('Shikha', 28, 'A++'),
              ('Abhishek', 27, 'A++'),
              ('Swati', 30, 'A++')]
age = lambda ages: ages[1]
candidates.sort(key=age)
show(candidates)

# sorting tuples of tuples
candidate = (('Rohit', 25, 'A++'),
             ('Shikha', 28, 'A++'),
             ('Abhishek', 27, 'A++'),
             ('Swati', 30, 'A++'))
name = lambda names: names[0]
sorted_candidates = sorted(candidate, key=name)
show(sorted_candidates)
