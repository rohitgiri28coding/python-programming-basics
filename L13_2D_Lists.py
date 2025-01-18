matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[0][1])

# Printing all elements in matrix
for row in matrix:
    for items in row:
        print(items)

main_course = ['chawl', 'dal', 'sabji', 'raita']
extra = ['papad', 'salad', 'fried mirchi', 'achar']
dessert = ['aam', 'watermelon', 'dahi', 'ice cream']

meal = [main_course, extra, dessert]
print(meal)
print(meal[0])
print(meal[1][1])
