#!python3
# -*-coding:utf-8 -*
import os
from math import ceil
from random import randrange
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from manager import Player, Dealer, PeopleManager
import subprocess as sp
import database_module as db

if __name__ == "__main__":

	def mainMenu(player) :
		game = str()
		start = 'start'
		print('welcome to the casino rolette game !')
		while (game.lower() != 'start') and (game.lower() != 'quit') : # lower() : lowercase the string game
			game = input("type start to play or anything to exit : ")
			if (game.lower() == 'start') :
				name = input('what should i call you ! : ')
				player.setName(name)
				return 1
			else:
				return 0

	def bet(player):
		while (player.getBet() <= 0) or (player.getBet() > player.getMoney()):
			bet1 = input('enter your bet please : ')
			player.setBet(bet1)
			try:
				bet = int(player.getBet())
				player.setBet(bet)
			except ValueError:
				print('enter an amount of money to bet ')
			continue
			if (player.getBet() <= 0) :
				print('not enough money (minimum is 1$)')
			elif (player.getBet() > player.getMoney()) :
				print('you dont have that much money !')

	def betOn(player):
		try:
			beton = int(player.getBetOn())
			player.setBetOn(beton)
		except ValueError:
			print('only numbers between 0 and 49 are acceptable !')
		while (player.getBetOn() < 0) or (player.getBetOn() > 49):
			bet = int(input('enter number between 0 and 49 : ')) # number selected to bet on
			player.setBetOn(bet)

	def score(player, dealer):
		money = int(player.getMoney())
		bet = int(player.getBet())
		beton = int(player.getBetOn())
		if (player.getBetOn() == dealer.getnbRand()) :
			print('{0} = {1} You win !'.format(player.getBetOn(), dealer.getnbRand()))
			newmoney = money + bet + (bet * 3)
			player.setMoney(newmoney)
			print('your balance is : {}$'.format(newmoney))
		elif ((player.getBetOn() % 2) == (dealer.getnbRand() % 2)) :
			print('{0} is same color as {1} You win !'.format(player.getBetOn(), dealer.getnbRand()))
			newmoney = money + bet + (bet * 0.5)
			player.setMoney(newmoney)
			print('your balance is : {}$'.format(newmoney))
		else :
			print('{0} is diffrent color from {1} !'.format(player.getBetOn(), dealer.getnbRand()))
			print('you lose!')
			newmoney = player.getMoney()
			print('your balance is : {}$'.format(newmoney))

	def game(player, dealer):
		if (mainMenu(player)):
			print('Hi {}'.format(player.getName()))
			print('you have {}$ now !'.format(player.getMoney()))
			roll = 1
			while (player.getMoney() > 0) and (roll == 1):
				roll = 0
				bet(player)
				money = player.getMoney() - player.getBet()
				player.setMoney(money)
				betOn(player)
				dealer.throw()
				score(player, dealer)
				player.setBetOn(-1)
				player.setBet(0)
				if (player.getMoney() == 0):
					print('sorry {} you lost all your money get out of here !!'.format(player.getName))
					break
				else:
					roll = int(input('type 1 to roll again, anything to exit : '))


	manager = PeopleManager(address=('127.0.0.1', 50000), authkey=b'abc')
	manager.connect()
	PeopleManager.register("getPlayer")
	PeopleManager.register("getDealer")
	#PeopleManager.register("mainMenu")
	#PeopleManager.register("bet")
	#PeopleManager.register("betOn")
	#PeopleManager.register("score")
	#PeopleManager.register("game")
	#PeopleManager.register("setName")
	playername = input('enter player name : ')
	player = manager.getPlayer(playername)
	dealer = manager.getDealer("dealer1")

	#name = 'Diref'
	player.setName(playername)
	#print ("name = {} ".format(player.getName()))
	#print (player.getMoney())

	game(player, dealer)
	db.add_data(player.getName(), player.getMoney())
	scorep = db.get_data(player.getName())
	print ("name : {} ".format(scorep[0]))
	#print ("name : {} ".format(scorep[1]))
