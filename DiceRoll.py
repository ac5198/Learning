import random
decision = True
while decision:
    print('You rolled a', random.randint(1, 6))
    decision = ('yes') in input('Do you want to roll again? ').lower()