import random

x = random.randint(1, 6)
y = random.random()

print('Dice rolled: '+str(x))
print(f"Random num b/w 1 to 100: {int(y*100)}")

myList = ['rock', 'paper', 'scissors']
print('Rock, paper, scissors, shoot: '+random.choice(myList))

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'K', 'Q', 'J', 'A']
random.shuffle(cards)
print(f'Shuffled card = {cards}')

