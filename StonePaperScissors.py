import random

print('Rock Paper Scissors Game')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties'% (wins,losses,ties))

    while True:
        print('Enter your choice: Rock - r, paper - p, scissors - s or quit - q')
        playerChoice = input('>')

        if playerChoice == 'q':
            print('Game Over')
            exit

        if playerChoice == 's' or playerChoice == 'p' or playerChoice == 'r':
            break

        print('Type one of r, p, s, or q.')

    if playerChoice == 'r':
        print("Rock vs ...")

    elif playerChoice == 'p':
        print("Paper vs ...")

    elif playerChoice == 's':
        print("Scissors vs ...")

    moveNumber = random.randint(1,3)

    if moveNumber == 1:
        computerMove = 'r'
        print('Rock')
    elif moveNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif moveNumber == 3:
        computerMove = 's'
        print('Scissors')

    if playerChoice == computerMove:
        print('It is a tie!')
        ties = ties + 1


    elif playerChoice == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1

    elif playerChoice == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1

    elif playerChoice == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1

    elif playerChoice == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1

    elif playerChoice == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1

    elif playerChoice == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1