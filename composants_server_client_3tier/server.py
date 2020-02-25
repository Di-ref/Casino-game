#!python3
# -*-coding:utf-8 -*
import os
from math import ceil
from random import randrange
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from manager import Player, Dealer, PeopleManager

manager = PeopleManager(address=('', 50000), authkey=b'abc')

def getPlayer(name):
   if manager.hasPlayer(name):
      return manager.players[name]
   else:
      player = Player()
      manager.addPlayer(name, player)
      manager.register(name, lambda: player)
      return manager.players[name]

PeopleManager.register("getPlayer", getPlayer)

def getDealer(name):
   if manager.hasDealer(name):
      return manager.dealers[name]
   else:
      dealer = Dealer()
      manager.addDealer(name, dealer)
      manager.register(name, lambda: dealer)
      return manager.dealers[name]

PeopleManager.register("getDealer", getDealer)




#PeopleManager.register("mainMenu", mainMenu)

        


#PeopleManager.register("bet", bet)




#PeopleManager.register("betOn", betOn)




#PeopleManager.register("score", score)




#PeopleManager.register("game", game)


if __name__ == "__main__":
   server = manager.get_server()
   server.serve_forever()
   debug=True
