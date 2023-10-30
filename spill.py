import pygame

class Player():
    def __init__(self,name,hitpoints,position):
        self.name   =name
        self.hitpoints=hitpoints
        self.position=position
    def update():
        print("update")
    def printStats(self):
        print(self.name,self.hitpoints,self.position)

position =[100,10]
player1 = Player("Peter Griffin",100,position)
player1.update()
