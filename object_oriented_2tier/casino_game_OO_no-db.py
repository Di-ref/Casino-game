#!python3
# -*-coding:utf-8 -*
import os
from math import ceil
from random import randrange


class player:
        def __init__(self):
                self.name = 'player1'
                self.money = 5000
                self.bet = 0
                self.betOn = -1

        def printName(self):
                print("Hello " + self.name)
class dealer:
        def __init__(self):
                self.name = 'dealer'
                self.nbRand = 0

        def throw(self): # random number between 0 and 49
                self.nbRand = randrange(50) 

def mainMenu(player):
        game = str()
        start = 'start'
        print('welcome to the casino rolette game !')
        while (game.lower() != 'start') and (game.lower() != 'quit') : # lower() : lowercase the string game
                game = input("type start to play or anything to exit : ")
                if (game.lower() == 'start') :
                        player.name = input('what should i call you ! : ')
                        return 1
                else:
                        return 0     

def bet(player):
        while (player.bet <= 0) or (player.bet > player.money):
                player.bet = input('enter your bet please : ')
                try:
                        player.bet = int(player.bet)
                except ValueError:
                        print('enter an amount of money to bet ')
                continue
                if player.bet <= 0:
                        print('not enough money (minimum is 1$)')
                elif player.bet > player.money:
                        print('you dont have that much money !')

def betOn(player):
        try:
                player.betOn = int(player.betOn)
        except ValueError:
                print('only numbers between 0 and 49 are acceptable !')
        while (player.betOn < 0) or (player.betOn > 49):
                player.betOn = int(input('enter number between 0 and 49 : ')) # number selected to bet on
                
def score(player, dealer):
        if player.betOn == dealer.nbRand :
                print('{0} = {1} You win !'.format(player.betOn, dealer.nbRand))
                player.money = player.money + player.bet + (player.bet * 3)
                print('your balance is : {}$'.format(player.money))
        elif (player.betOn % 2) == (dealer.nbRand % 2):
                print('{0} is same color as {1} You win !'.format(player.betOn, dealer.nbRand))
                player.money = player.money + player.bet + (player.bet * 0.5)
                print('your balance is : {}$'.format(player.money))
        else:
                print('{0} is diffrent color from {1} !'.format(player.betOn, dealer.nbRand))
                print('you lose!')
                print('your balance is : {}$'.format(player.money))

def game(player, dealer):
        if (mainMenu(player)):
                print('Hi {}'.format(player.name))
                print('you have {}$ now !'.format(player.money))
                roll = 1
                while (player.money > 0) and (roll == 1):
                        roll = 0
                        bet(player)
                        player.money = player.money - player.bet
                        betOn(player)
                        dealer.throw()
                        score(player, dealer)
                        player.betOn = -1
                        player.bet = 0
                        if (player.money == 0):
                                print('sorry {} you lost all your money get out of here !!'.format(player.name))
                                break
                        else:
                                roll = int(input('type 1 to roll again, anything to exit : '))

player1 = player()
dealer1 = dealer()

game(player1, dealer1)

os.system("pause")
