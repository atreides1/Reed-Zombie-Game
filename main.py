#ITEM STACKING ON FLOOR, IN INV
from room import Room
from player import Player
from item import Item,Weapon,Armor, Snacks, Bags
from monster import Monster
from mappy import Map
from misc import Reed,Chem,craft,Scholz,Nog,CSO,Library,Commons,Rubble
import os
import updater
import random
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#prints the objective for the player
def objective():
    clear()
    print("Welcome to Reed College!")
    print("Or at least it was Reed...")
    print("Feel free to have a look around")
    print("and oh yeah...")
    print()
    print("Be sure to watch out for zombies")
    print()
    print()
    print("For now your only hope is to collect as many")
    print("samples of rotten flesh as you can. Maybe  ")
    print("there's something you can use in the chem lab")
    print("to try to find a cure. ")
    print ("Just press help for possible actions")
    print("Or use command 'objective' to see this again")
    input("Good luck and be safe... <3")
objective()
#creates a Player object
player = Player()


# def new_room(self,col,row,desc):
#     self.col=col
#     self.row=row
#     self.desc= desc
#     self.coordinates.append(make_position(self.col,self.row))
#     return self.Room(self.desc)

# def rand_desc(self,key):
#     for descriptions in room_descs{}
#Can have a list of values that are in a list,

#the overall function that creates the world with randomized rooms
def createWorld():
    #Making of the grid of rooms:
    alist=[1,2,3,4,5,6,7,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10,10,10,10] #~~
    #Associates every room with a distinct description #. Fancy rooms only appear once
    player_start=[0]
    #decriptions for all rooms
    desc_list=["You stand in your old dorm, Scholz.\nRubber floors and claustrophobic hallways await,\nbut it is a place you call home.","You have entered Tir Na Nog, land of the young.\nCheesy snacks, 20 sided die, and magic cards litter the room.\nOh, not to mention zombie tracks.\nYou look around, the windows are covered with paintings,\none catches your eye: a giant sky squid.", "You have entered twenty-eight west,\nthe former home of community safety officers-\nnow home to trashed paperwork and the smell of zombie. \nMaybe you could find a weapon...","You have entered the Chem building.\nWhat would have been a beautiful sight-\na wall of windows up ahead- is smashed, unfortunately.\nMaybe there's still something sueful left in here.","You have entered the Library, or the Hauser Fun Dome.\nNot so fun anymore.\nBooks lie scattered around, limp and sad.","You have entered Commons, once an okay place to eat.\nNow, an okay place to be eaten.","It's cold, wet, and foggy out.\nNot too different from the 'good ol days'","You walk past the crumbled remains of Vollum.\nAt least you wont have to go to lecture anymore.","It's pretty spooky out here.\nMaybe I should find some shelter.","Nothing interesting to see here.","The stench of zombies lingers in the air.\nFresh footprints prove they're not too far gone."]
    #Descs: 0:Scholz, 1:Nog, 2:28 3:Chem 4:Lib 5:Commons 6:Cold out 7: Vollum 8:NOthing interesting 9:Zombie flesh
    blist=[]
    #picks a random room and appends it to blist for the sake of testing if all rooms have spawned correctly
    def rand_choice(alist):
        x=random.choice(alist)
        blist.append(x)
        alist.remove(x)
        a=alist
        b=blist
        return x
    #chooses a random description from the list
    def rand_desc(alist,desc_list):
        y=rand_choice(alist)
        z=desc_list[y]
        return z
    #function that generates the rooms
    def createRooms():
        roomslist=[]
        #its place on the grid in (x,y) coordinates
        roompos=[]
        xstart=0
        ystart=0
        mylist=[]
        count=1
        #generates a coordinate plane + random coordinate for each room
        while xstart<5:
            ystart=0
            while ystart<5:
                if len(roomslist)==12:
                    newroom=Room(xstart,ystart,"("+str(count)+")",rand_desc(player_start,desc_list),0)
                    ystart=ystart+1
                    count=count+1
                else:
                    roomdesc= rand_desc(alist,desc_list)
                    room_desc_num=desc_list.index(roomdesc)
                    newroom=Room(xstart,ystart,"("+str(count)+")",roomdesc,room_desc_num)
                    ystart=ystart+1
                    count=count+1
                roomslist.append(newroom)
                roompos.append(newroom.pos)

            xstart=xstart+1
        return roomslist
    blah=createRooms()
    def connections(blah):
        #creates connections between the rooms
        #blah is the list of rooms with coordinates
        i=0

        while blah[i].pos[0]<5 and i<24:
            # print(blah[i].pos)
            if blah[i].pos==[4,4]:
                i=i+1
                # print("done")
            elif blah[i+1].pos[1]==0:
                i+=1
            else:
                # print(blah[i].pos,"south",blah[i+1].pos,"north")
                Room.connectRooms(blah[i],"north",blah[i+1],"south")
                i+=1
        x=0
        while blah[x].pos[0]<5 and x<24:
            # print(blah[x].pos)
            if blah[x+5].pos==[4,4]:
                Room.connectRooms(blah[x],"east",blah[x+5],"west")
                # print(blah[x].pos,"east",blah[x+5].pos,"west")
                x=24

                # print("done")
            elif blah[x+5].pos[0]==4:
                Room.connectRooms(blah[x],"east",blah[x+5],"west")
                x+=1
            else:
                # print(blah[x].pos,"east",blah[x+5].pos,"west")
                Room.connectRooms(blah[x],"east",blah[x+5],"west")
                x+=1
        player.location=blah[12]
        blah[12].visited=True
        blah[12].playerIn=True
    connections(blah)
    return blah
#spawning random items, chooses item rarity based on a random number
def giveRandom():
    return random.randint(1,30)
def spawnItems():
        ls = []
        #if the # of days is greater than 2 and the room has no items (Starting condition)
        if roomslist[12].items==[] and player.items==[] and player.timeAlive<2:

            i = Item("Rock", "This is just a rock.",9)
            w = Weapon("Pencil","A bit dull but still useful for stabbing.",.5,1.5)
            ww = Weapon("Nerf Gun","You remember the chant of an old movie...\n'You'll shoot you're eye out.'",3,2)
            vv = Bags("Plastic Bag", "A torn plastic bag", 0, 4)
            aa = Armor("Blanket","Stylish AND protective!",3,0.15)
            cc=Snacks("Candy","You really should try to eat healthier...",.5,8)
            ccc=Snacks("Candy","You really should try to eat healthier...",.5,8)
            dd=Snacks("Rotten Flesh","It's a little slimey. Not good for eating.",.5,-8)
            ls = [i, w, ww, vv, aa, cc, ccc, dd]
            for n in ls:
                n.putInRoom(random.choice(roomslist))
            start=Weapon("Pencil","A bit dull but still useful for stabbing.",1,1.5)
            start.putInRoom(roomslist[12])
        #Did the player JUST kill a monster, game spawns items based on luck. Rotten flesh mostly for end goal
        elif player.monsterSlayer==True:
            oboy=giveRandom()
            if oboy>10:
                rf=Snacks("Rotten Flesh","It's a little slimey. Not good for eating.",.5,-8)
                rf.putInRoom(player.location)
            else:
                c=Snacks("Candy","You really should try to eat healthier...",.5,8)
                c.putInRoom(player.location)
                if oboy<5:
                    rf=Snacks("Rotten Flesh","It's a little slimey. Not good for eating.",.5,-8)
                    rf.putInRoom(player.location)
                    w=Weapon("Shotgun","Pow pow!",4,3.25)
                    w.putInRoom(player.location)
            player.monsterSlayer=False
        #When time passes, random items sometimes spawn on random places around the map
        else:
            r=giveRandom()
            if r>3:
                ls=[]
                if r>28:
                    cc=Snacks("Doughnuts","One big bucket of doughnuts.",2.5,25)
                    aa = Armor("Coat","It protects from rain. What about zombies?",4,0.25)
                    ls.append(cc)
                    ls.append(aa)
                elif r==28:
                    cc=Bags("Backpack","Stuff it full of candy and flesh then call it a night.", 0, 8)
                    aa=Snacks("Noodles","The nutrition label says it has at least 4 grams of fiber!",1.5,14)
                    ls.append(cc)
                    ls.append(aa)
                elif r<28 and r>6:
                    cc=Snacks("Candy","You really should try to eat healthier...",.5,8)
                    ls.append(cc)
                elif r<7:
                    cc=Snacks("Rotten Flesh","It's a little slimey. Not good for eating.",.5,-8)
                    ls.append(cc)
                for n in ls:
                    n.putInRoom(random.choice(roomslist))


def printSituation(roomslist):
    clear()
    print(player.location.desc)
    print()
    # print(player.location.pos,"  ",player.location.name)
    #Descs: 0:Scholz, 1:Nog, 2:28 3:Chem 4:Lib 5:Commons 6:Cold out 7: Vollum 8:NOthing interesting 9:Zombie flesh
    #matches ascii art with room desc, rubble if it's a lame room
    if player.location.descNumber==0:
        Scholz(False,False)
    elif player.location.descNumber==1:
        Nog(False,False)
    elif player.location.descNumber==2:
        CSO(False,False)
    elif player.location.descNumber==3:
        Chem(False,False)
    elif player.location.descNumber==4:
        Library(False,False)
    elif player.location.descNumber==5:
        Commons(False,False)
    elif player.location.descNumber>5:
        Rubble(False,False)
    #Game keeps track of zombies spawning each turn, tells you if more than one or just one spawns
    if player.spawnCounter!=0:
            if player.spawnCounter==1:
                print("A chill runs down your spine as though to say\n'a zombie just spawned somewhere'.")
                player.spawnCounter=0
            else:
                print("A chill runs down your spine as though to say\n'"+str(player.spawnCounter)+" zombies just spawned somewhere'.")
                player.spawnCounter=0
    #Gives a desc of most recent attempt without clearing whole screen/press enter to continue
    if player.recentAction!="":   #~~
        print(player.recentAction)
        print()
        player.recentAction=""
    if player.location.hasMonsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.hasItems():
        print("This room contains the following items:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)

#help function
def showHelp():#~~
    clear()
    print("map -- Displays a map of campus")
    print("objective -- Shows the introduction screen again")
    print("go <direction> -- moves you in the given direction")
    print("craft -- attempt to find a cure")
    #The cure is zombie flesh. Must be in chem lab. Success rate: 25%
    print("inventory -- opens your inventory")
    print("pickup <item> -- picks up the item")
    print("drop <item> -- drops the item")
    print("me -- displays current stats")#~~
    print("attack <monster> -- attacks the zombie you've targeted.")
    print("inspect <item> -- checks room and inventory for item and gives description")
    print("wait -- waits for one unit of time. Health recovers over time.")
    print("    wait <number> -- waits for the given units of time")
    print("equip <item> -- equips an item in your inventory")
    print("    Note: You may only wear one of each item type!")
    print("eat <item> -- consumes item (You can eat off the floor)")
    print("quit -- Ends game. Your progress will not be saved.")
    print()
    input("Press enter to continue...")


#creating the world and map! Roomslist is named so that it can be used later.
roomslist=createWorld()
playerMap=Map(roomslist)#~~
playerMap.visitedRooms()
maparooni=playerMap.writeMap()

#print(k)
#to spawn items
spawnItems()
playing = True
#to spawn monster
def spawn():
    #is based off number of days you are alive
    #picks a random number, the more time alive, the higher the num can be
    if player.timeAlive>=1 and player.timeAlive<=18:
        sorandom=random.randint(0,5)
        return sorandom
    elif player.timeAlive>19 and player.timeAlive<=28:
        sorandom=random.randint(0,7)
        return sorandom
    elif player.timeAlive>29 and player.timeAlive<=38:
        sorandom=random.randint(0,9)
        return sorandom
    elif player.timeAlive>39 and player.timeAlive<=48:
        sorandom=random.randint(0,12)
        return sorandom
    else:
        return 8
def spawnMany(roomslist):
    #actually spawns the monsters, assigning them a random name
    nameslist=["ZomSarah","ZomPalak","ZomSamuel","ZomNancy","ZomTom","ZomShawn","ZomNoah","ZomLiam","ZomMason","ZomJacob","ZomBilly","ZomSierra","ZomMercy","ZomVikram","ZomJames","ZomDora","ZomAlexander","ZomMichael","ZomBenjamin","ZomEmma","ZomMark","ZomAva","ZomIsabella","ZomMia","ZomAbigail","ZomEmily","ZomCharlotte","ZomHarper","ZomTori"]
    j=spawn()
    # print(j,"!!!")
    while j>0:
        rand=random.random()
        if rand>.65:
            player.spawnCounter+=1
            #spawns in a random room with a random name
            name=random.choice(nameslist)
            room=random.choice(roomslist)
            Monster(name,30,room)
        j-=1

#monsters randomly attack the player
def monsterAttack():
    if player.location.hasMonsters():
        #there is a fifty-fifty chance
        n = random.randint(0,100)
        #change 50 to change %cahnce of attack
        if n >  50:
            m = random.choice(player.location.monsters)
            print(str(m.name)+ " attacks you!")
            input("Press enter to continue...")
            clear()
            player.attackMonster(m)
            if player.alive==False:
                return
    else:
        return
#if the game is being played, reset commandSuccess and timePasses
while playing and player.alive:
    printSituation(roomslist)
    commandSuccess = False
    timePasses = False

    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        commandWords = command.split()

        if commandWords==[]: #~~
            print("Try 'help' for possible commands!")
            commandSuccess = False
        elif commandWords[0].lower() == "go":   #~~ Make it so game doesn't crash if invalid direction
            targetName = str(command[3:].lower())
            # print(targetName)
            a=player.location.isExit(targetName)
            #print(a)
            if a:
                #playerIn is so that the map tracks your location with a *(asterisk)
                player.location.playerIn=False #~~
                player.goDirection(commandWords[1].lower())
                player.location.playerIn=True
                player.location.visited=True#~~
                print()
                #creates the map (in mappy.py) and stores whether the player has visted a room
                playerMap=Map(roomslist)#~~
                playerMap.visitedRooms()
                maparooni=playerMap.writeMap()

                timePasses = True
            else: #~~
                print("Not a valid direction.")
                commandSuccess = False

        elif commandWords[0].lower() == "map": #~~
            #prints the map
            clear()
            Reed(False,False)
            print(maparooni)
            #Isn't the little legend cute?!?!
            print("Key:    '*' -- You are here               N       ")
            print("        '?' -- Undiscovered               |       ")
            print("        'H' -- Home                  W ---|--- E  ")
            print("        '~' -- Discovered                 |       ")
            print("        '!' -- Special location           S       ")
            print()
            print()
            input("Press enter to continue...")
        elif commandWords[0].lower() == "wait":
            #waits for one unit of time
            #**
            targetName = command[5:]
            print(targetName)
            if targetName=='' or targetName=='1':
                timePasses = True
            else:
                #waits for multiple units of time
                t = int(targetName)
                print(t)
                for i in range(0, t-1):
                    #for each day, create items, update, health, and the finally time will pass
                    if player.health<player.maxhealth:
                        player.health+=1
                    spawnItems()
                    spawnMany(roomslist)
                    updater.updateAll()
                    player.timeAlive+=1
                    timePasses = True
                clear()
                print("Day: "+str(player.timeAlive)+"  Health: "+str(player.health))
                #saame as above but iot in the player situation since this is separate
                if player.spawnCounter!=0:
                    if player.spawnCounter==1:
                        print("A chill runs down your spine as though to say:\n'a zombie just spawned somewhere'.")
                        player.spawnCounter=0
                    else:
                        print("A chill runs down your spine as though to say:\n'"+str(player.spawnCounter)+" zombies just spawned somewhere'.")
                        player.spawnCounter=0
                input("Press enter to continue...")

        elif commandWords[0].lower() == "eat": #**
            #eats item off of ground or in inventory
            targetName = command[4:]
            target = player.playerItem(targetName)
            groundtarget= player.location.getItemByName(targetName)
            if target in player.items or groundtarget in player.location.items:
                # if target!=False:
                #     # if target.slot:
                if target in player.items:
                    if target.eatable==True:
                        player.eat(target)
                        player.recentAction=str("You ate " +target.name+"\nHealth: "+str(round(player.health,2))+"/"+str(player.maxhealth))
                    else:
                        clear()
                        player.recentAction="You tried eating an uneatable item.\nYou're lucky you don't have to get your stomach pumped."

                elif groundtarget in player.location.items:
                    if groundtarget.eatable==True:
                        player.eat(groundtarget)
                        player.recentAction=str("You ate the " +groundtarget.name+" off the ground. Gross. :/\nHealth: "+str(round(player.health,2))+"/"+str(player.maxhealth))
                    else:
                        clear()
                        player.recentAction="You tried eating an uneatable item.\nYou're lucky you don't have to get your stomach pumped."

            else:
                print("No such item.")
                commandSuccess=False
        elif commandWords[0].lower() == "me":#~~ #**
            #prints status of player and map
            clear()
            Reed(False,False)
            print(maparooni)
            print("    Hint: Use command 'map' for just the map and its key.")
            print()
            print("Health: " + str(round(player.health,2))+"/"+str(player.maxhealth))
            print("Level: "+str(player.level))
            print("Experince until next level: "+str(100-player.xp))
            print("Bag: "+str(player.mybagname))
            print("Carry Weight: " + str(player.carrying)+"/"+str(player.carryingCap))
            print("Weapon: "+str(player.myweaponname))
            print(" My Damage: "+str(player.damage))
            print("Armor: "+str(player.myarmorname))
            print(" Damage reduction: -"+str(100*player.damagereduction)+"%")
            print("Key: "+str(player.mykeyname))
            # print("You are alive? " + str(player.alive))
            print("Zombies Killed: "+str(player.zombieKillCounter))
            print("Time Alive: "+str(player.timeAlive)+" days")
            input("Press enter to continue...")
        elif commandWords[0].lower() == "objective": #~~
            #prints the objective of the game
            objective()
        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            #pickups the item and adds it to inventory
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            #if it exists, add to inventory and print
            if target != False:
                player.recentAction=("You have added " + str(targetName.lower()) + " to your inventory.")
                player.pickup(target)
            #if it doesn't exist, print no item
            else:
                print("No such item.")
                commandSuccess = False
        #craft an item
        elif commandWords[0].lower() =='craft':
            #if player is in the chem building, they can craft using zombie flesh
            if player.location.descNumber==3:
                craft(player)
            else:
                commandSuccess=False
                input("You search fruitlessly for a good place to sit and tinker.\nMaybe somewhere a little more sciency would work better...")


        elif commandWords[0].lower() == "drop":  #~~
            #players can drop specific items
            targetName = command[5:]
            target = player.playerItem(targetName)

            if target in player.items:
                if target!=False:
                    player.recentAction=("You gently toss your "+str(targetName.lower())+" on the ground.")
                    player.drop(target)

            else:
                print("Not carrying "+targetName+"!")
                commandSuccess = False
        elif commandWords[0].lower() == "equip": #~~
            #equips a powerup
            targetName = command[6:]
            target = player.playerItem(targetName)
            if target != False:
                if target.equippable==False:
                    print("Can't equip that!")
                    commandSuccess=False
                else:
                    player.equip(target)
            else:
                print("Are you sure you've got that?\nMaybe try picking up the item first." )
                commandSuccess = False
        elif commandWords[0].lower() == "inventory":
            player.showInventory()
        elif commandWords[0].lower() == "help":
            showHelp()
        elif commandWords[0].lower() == "quit": #~~ Renamed exit or whatever this was
            print("Wow, rude.")
            print("The world isn't gonna save itself!")
            print("You have defeated " + str(player.zombieKillCounter) + " zombies.")
            print("You survived "+str(player.timeAlive)+" days.")
            playing = False
        elif commandWords[0].lower() == "attack":
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                player.attackMonster(target)
            else:
                print("No such monster.")

        elif commandWords[0].lower() == "inspect":  #~~
            targetName = command[8:].lower()
            target = player.playerItem(targetName)
            groundtarget= player.location.getItemByName(targetName)
            if target in player.items or groundtarget in player.location.items:
                if target in player.items:
                    player.recentAction=("In inventory. " +target.name+": "+ target.desc + " Weight: " + str(target.weight))
                elif groundtarget in player.location.items:

                    player.recentAction=("On ground. " +groundtarget.name+": "+ groundtarget.desc + " Weight: " + str(groundtarget.weight))
            else:
                print("No such item.")
        else:
            print("Not a valid command")
            commandSuccess = False


    if timePasses == True:
        #Does these things every time time has passed (walking, waiting etc)
        monsterAttack()
        spawnItems()
        spawnMany(roomslist)
        if player.health<player.maxhealth: #~~
            player.health+=1
        player.timeAlive+=1

        if player.health<player.maxhealth: #~~
            player.health+=1


        updater.updateAll()

if player.alive==False and player.wonGame==True:
    clear()
    print("You win!")
    print("You have defeated " + str(player.zombieKillCounter) + " zombies.")
    print("You survived "+str(player.timeAlive)+" days.")
    input("Press enter to continue...")
    playing=False
# if player.wonGame:
#     playing=False
elif player.wonGame==False and player.health<=0 or player.alive==False: #~~
    clear()
    print("You lose.")
    print("You have defeated " + str(player.zombieKillCounter) + " zombies.")
    print("You survived "+str(player.timeAlive)+" days.")
    input("Try better next time.")
    player.alive=False
