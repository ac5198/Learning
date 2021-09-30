import random


print ('Rock Paper Scissors Shoot!')
weapon = (input('Choose your weapon: '))
print (weapon)

computer = ['rock', 'paper', 'scissors']
computerchoice = random.choice(computer)

#Computer choice
print ('The computer chose: ' + computerchoice)

if weapon == computerchoice:
    print ('It is a draw!')
elif weapon == 'rock' and computerchoice == 'paper':
    print ('You lose')
elif weapon == 'rock' and computerchoice == 'scissors':
    print('You win!')
elif weapon == 'paper' and computerchoice == 'rock':
    print('You win')
elif weapon == 'paper' and computerchoice == 'scissors':
    print('You lose')
elif weapon == 'scissors' and computerchoice == 'rock':
    print('You lose')
elif weapon == 'scissors' and computerchoice == 'paper':
    print('You win!')