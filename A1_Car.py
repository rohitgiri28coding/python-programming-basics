start = 'start'
stop = 'stop'
quit_game = 'quit'
print('Write \'start\' to start the car\nWrite \'stop\' to stop the car\n'
      'Write \'quit\' to quit the game')
while True:
    entry = input('>')
    entry = entry.lower()
    if entry == start:
        print("Dhrung..... Dhrung")
        print('Car started')
    elif entry == stop:
        print('Car stopped')
    elif entry == quit_game:
        break
