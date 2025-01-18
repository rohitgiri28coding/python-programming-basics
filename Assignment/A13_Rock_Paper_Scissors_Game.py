import random

choices = ['rock', 'paper', 'scissors']
player_pts = 0
comp_pts = 0
i = 0
while i < 5:
    player = None
    computer = random.choice(choices)
    while player not in choices:
        player = input('Choose rock, paper, scissors: ').lower()

    print('Computer: '+computer)
    print('Player: '+player)
    if player == computer:
        print('Both got 0 points.')
    elif choices.index(player) == choices.index(computer)+1 or choices.index(player)+2 == choices.index(computer):
        print('You got +1 points.\nComputer got -1 points.')
        player_pts += 1
        comp_pts -= 1
    else:
        print('You got -1 points.\nComputer got +1 points')
        player_pts -= 1
        comp_pts += 1
    i += 1
if player_pts == comp_pts:
    print('Tie!\nScore: {}'.format(comp_pts))
elif player_pts < comp_pts:
    print(f'You lost by {(comp_pts-player_pts)} points.')
else:
    print(f'You won by {(player_pts-comp_pts)} points.')
