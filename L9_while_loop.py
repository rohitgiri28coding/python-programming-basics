# while loops can have their own else statements

import random
num = random.randint(1, 10)

i = 0
while i <= 3:
    entered_number = input("Guess the number: ")
    if int(entered_number) == num:
        print('You won!')
        break
    else:
        print('Try Again')
else:
    print('You lost.....')

name = None  # None = null
while not name:
    name = input("What is your name?\n")
print('Hi '+name.capitalize(), ", Congratulation you won the game.")
