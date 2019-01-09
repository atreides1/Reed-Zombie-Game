from room import Room
from player import Player
import random


class Map:
    def __init__(self,list_of_rooms):
        self.list_of_rooms=list_of_rooms
        self.columns=5
        self.rows=5
        self.discoveredlocation=[]
        #Takes list of rooms to create map
    def discovered(self,position):
        self.visitedRooms()
        for i in self.discoveredlocation:
            if i.pos==position:
                return True
        return False
        #returns True if location is discovered
    def playerIn(self): #~~
        alist= self.list_of_rooms
        for i in alist:
            if i.playerIn==True:
                #print(i.pos)
                return i.pos
            
    def visitedRooms(self):
        for roomy in self.list_of_rooms:
            if roomy.visited and roomy not in self.discoveredlocation:
                self.discoveredlocation.append(roomy)
            #One of each of every discovered location!

    def getdescfrompos(self,position):
        self.visitedRooms()
        for i in (self.discoveredlocation):
            # print("In loop")
            # print(self.discoveredlocation[i].pos,position)
            if i.pos==position:
                return i.descNumber
        return 20
        #Finds the description number of rooms in discovered locations so as to return correct symbols

    def writeMap(self):
        y=4
        x=0
        symbol="?"
        #Default ^
        liststring=[]
        while y>=0:
            x=0
            while x<5:
                #Goes through all rooms and sees what their desc is
                tf=self.discovered([x,y])
                
                if tf==True:
                    #print("!",x,y)
                    ishere=self.playerIn()
                    #print([x,y],ishere)
                    if [x,y]==ishere:
                        symbol="*"
                    else:
                        num=self.getdescfrompos([x,y])
                        #special rooms get special symbols (commons, lib, chem, etc)
                        if num==0:
                            symbol="H"
                            #Home sweet home :)
                        elif num==1 or num==2 or num==3 or num==4 or num==5:
                            symbol="!"
                        elif num==6 or num==7 or num==8 or num==9 or num==10:
                            symbol="~"
                    
                else:
                    symbol="?"
                liststring.append(" ["+symbol+"] ")
                
                x+=1
            y-=1    
            #Makes and joins a very long strong with nice spacing and such
            liststring.append("\n\n")
            
        mystring=''.join(liststring)
        return mystring


