rows = int(input("Enter the no of rows: "))
columns = int(input("Enter no of columns: "))
symbol = (input("Enter the symbol to be used: "))

for i in range(rows):
    for j in range(columns):
        print(symbol, end=' ')    # use end to change the normal ending of print statement, i.e., \n
    print()
