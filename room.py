import random

class Room:
    def __init__(self,xcoord,ycoord,name=None,description=None,descNumber=None):
        self.desc = description
        self.name=name
        self.monsters = []
        self.exits = []
        self.items = []
        #~~
        #Most of these are used for mapping the rooms, pos=position, descNum for finding which room is which
        self.xcoord=xcoord
        self.ycoord=ycoord
        self.pos=[xcoord,ycoord]
        self.visited=False   
        self.descNumber=descNumber
        self.playerIn=False
        
    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])
    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]
    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)
    def exitNames(self):
        return [x[0] for x in self.exits]
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def addMonster(self, monster):
        self.monsters.append(monster)
        # print(self.pos,self.monsters)
    def removeMonster(self, monster):
        # print(monster,"<Monster",self.monsters)
        self.monsters.remove(monster)
    def hasItems(self):
        return self.items != []
    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasMonsters(self):
        return self.monsters != []
    def getMonsterByName(self, name):
        for i in self.monsters:
            if i.name.lower() == name.lower():
                return i
        return False
    def randomNeighbor(self):
        return random.choice(self.exits)[1]
    def isExit(self,destination): #~~
        if self.getDestination(destination)==None:
            return False
        else:
            return True