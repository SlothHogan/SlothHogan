import random, sys
print('ROCK, PAPER, SCISSORS')

#These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:     #The manin game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:   #The player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':     #Quit the game
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
          break    #Break out of player input loop.
        print('Type one of r, p, s, or q.')
  #Display what the player chose:
    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('Scissors versus...')


        #Display what the computer chose:
        randomNumber = random.randit(1, 3)
        if randomNumber == 1:
            computerMove = 'r'
            print('Rock')
        elif randomNumber == 2:
            computerMove = 'p'
            print('Paper')
        elif randomNumber == 3:
            computerMove = 's'
            print('Scissor')

        #Display and record the win/loss/tie:
        if playerMove == computerMove:
            print('Its a tie')
            ties = ties + 1
        elif playerMove == 'r' and computerMove == 's':
            print('You win!')
            wins = wins +1
        elif playerMove == 'p' and computerMove =='r':
            print('You win!')
            wins = wins +1
        elif playerMove == 's' and computerMove == 'p':
            print('You win!')
            wins = wins +1
        elif playerMove == 'r' and computerMove == 'p':
            print('You lose!')
            losses = losses +1
        elif playerMove == 'p' and computerMove == 's':
            print('You lose!')
            losses = losses +1
        elif playerMove == 's' and computerMove == 'r':
            print('You lose!')
            losses = losses +1


# Write your code here :-)
