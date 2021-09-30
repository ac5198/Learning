import random


print ('Rock Paper Scissors Shoot!')
weapon = (input('Choose your weapon: '))

computer = ['rock', 'paper', 'scissors']
computerchoice = random.choice(computer)

if weapon == computerchoice:
    print ('It is a draw! The computer chose', computerchoice)
elif weapon == 'rock' and computerchoice == 'paper':
    print ('You lost. The computer chose', computerchoice)
elif weapon == 'rock' and computerchoice == 'scissors':
    print('You win! The computer chose', computerchoice)
elif weapon == 'paper' and computerchoice == 'rock':
    print('You win! The computer chose', computerchoice)
elif weapon == 'paper' and computerchoice == 'scissors':
    print('You lost. The computer chose', computerchoice)
elif weapon == 'scissors' and computerchoice == 'rock':
    print('You lost. The computer chose', computerchoice)
elif weapon == 'scissors' and computerchoice == 'paper':
    print('You win! The computer chose', computerchoice)