#!python3
#Random number generator just because

import random

while True:
    print('Tell me what range you want your random numbers in (enter them one at a time)')
    myRange1 = int(input())
    if myRange1 == int:
        continue
    print('and')
    myRange2 = int(input())
    if myRange2 == int:
        continue
    print('How many numbers do you want to generate?')
    numOfDice = int(input())
    if numOfDice == int:
        break
    
    for i in range(numOfDice):
        r = random.randint(myRange1, myRange2)
        print(r)
    break
