
try:
    with open('C:\\Users\\DOS\\OneDrive\\venv\\Lib\\site-packages\\pip-22.3.1.dist-info\\LICENSE.txt') as file:
        print(file.read())
    print(file.closed)           # with open method closes the file automatically
except FileNotFoundError:
    print('File not found')

