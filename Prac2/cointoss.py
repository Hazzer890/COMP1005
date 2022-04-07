#
# cointoss.py - simulate tossing a coin multiple times
#

import random

coin = ['heads', 'tails']
heads = 0
tails = 0
trials = input('AMOUNT OF TRIALS: ')

print('\nCOIN TOSS\n')

for index in range(int(trials)):
    if random.choice(coin) == 'heads':
        heads = heads + 1
    else:
        tails = tails + 1

print('\nThere were ', heads, ' heads and ',  tails, ' tails.\n')
