import random


def again():
    again = input('\nWould you like to play again? ')
    if 'yes' == again:
        play()
    else:
        exit()


def play():
    Score=0
    print('\nRock Paper Scissors Shoot!')
    weapon = input('Choose your weapon: ').lower()
    computer = ['rock', 'paper', 'scissors']
    computerchoice = random.choice(computer)
    win = 'You win! The computer chose ' + computerchoice
    lose = 'You lost. The computer chose ' + computerchoice

    if weapon == computerchoice:
        print('It is a draw! The computer chose', computerchoice)
        again()
    elif weapon == 'rock' and computerchoice == 'paper':
        print(lose)
        again()
    elif weapon == 'rock' and computerchoice == 'scissors':
        print(win)
        Score = Score+1
        print('Your score is ', Score)
        again()
    elif weapon == 'paper' and computerchoice == 'rock':
        print(win)
        again()
    elif weapon == 'paper' and computerchoice == 'scissors':
        print(lose)
        again()
    elif weapon == 'scissors' and computerchoice == 'rock':
        print(lose)
        again()
    elif weapon == 'scissors' and computerchoice == 'paper':
        print(win)
        again()

play()