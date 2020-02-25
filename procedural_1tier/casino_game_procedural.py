# -*-coding:utf-8 -*
import os
from math import ceil
from random import randrange

money = 5000
nbSelect = -1
bet = -1
roll = 1

print('welcome to the casino rolette game !')
game = str()
start = 'start'
quit = 'quit'
while (game.lower() != 'start') and (game.lower() != 'quit') : # lower() : lowercase the string game
        game = input("type start to play or quit to exit : ")
        if game.lower() == quit :
                roll = 0
        elif game.lower() == start :
                break
        else:
                continue
print('you have 5000$ now !')

while (money > 0) and (roll == 1) :

        nbSelect = -1
        bet = -1

        while (bet <= 0) or (bet > money) :
                bet = int(input('enter your bet please : ')) # amount of money to bet with
                try:
                        bet = int(bet)
                except ValueError:
                        print('enter an amount of money to bet ')
                        continue
                if bet <= 0:
                        print('not enough money (minimum is 1$)')
                elif bet > money:
                        print('you dont have that much money !')

        money = money - bet

        while (int(nbSelect) < 0) or (int(nbSelect) > 49):
                nbSelect = int(input('enter number between 0 and 49 : ')) # number selected to bet on

        nbRand = randrange(50) # random number between 0 and 49

        if nbSelect == nbRand :
                print('{0} = {1} You win !'.format(nbSelect, nbRand))
                money = money + bet + (bet * 3)
                print('your balance is : {}$'.format(money))
        elif (nbSelect % 2) == (nbRand % 2):
                print('{0} is same color as {1} You win !'.format(nbSelect, nbRand))
                money = money + bet + (bet * 0.5)
                print('your balance is : {}$'.format(money))
        else:
                print('{0} is diffrent color from {1} !'.format(nbSelect, nbRand))
                print('you lose!')
                print('your balance is : {}$'.format(money))

        if (money == 0):
                print('you lost all your money get out of here !!')
                break
        else:
                roll = int(input('type 1 to roll again, anything to exit : '))


os.system("pause")
