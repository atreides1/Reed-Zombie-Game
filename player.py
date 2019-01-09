import os
import updater
import random
from item import Item,Weapon,Armor, Snacks, Bags

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def FightArt(clearchoice,inputchoice):
    #Small bit of art during ifght scenes
    if clearchoice==True:
        clear()
    print("                       .....   ")
    print("                      C C  /  ")
    print("                     /<   /     ")
    print("        ___ ________/_#__=o   ")
    print("        /(- /(\_\______   \    ")
    print("        \ ) \ )_   \o     \     ")
    print("        /|\ /|\     |'     |    ")
    print("                    |     _|  ")
    print("                    /o   __\    ")

    if inputchoice==True:
        input("Press enter to continue...")

class Player:
    def __init__(self):
        self.timeAlive=1
        #We keep count
        self.location = None
        self.items = []
        self.maxhealth=65
        self.health = 65
        self.alive = True
        self.weapon=False
        self.armor=False
        self.key=False
        #If they have one this is true
        self.damagemod=1
        self.damage=2*self.damagemod
        #Base damage=2, can add bonus later in game
        self.bonusDamage=0
        self.damagereduction=0
        #Added w armor
        self.myweaponname="No weapon" #~~
        self.myarmorname="No armor"
        self.mykeyname="No key"
        #For displaying inf "me"
        self.myweapon=None
        self.myarmor=None
        self.mykey=None
        #Items that take up slots
        self.zombieKillCounter = 0
        self.carrymod = 0
        #Added to by bags
        self.carrying=0 #~~
        self.carryingCap=10
        self.xp=0
        self.level=1
        self.mybagname = "No bag"
        self.mybag = None
        self.wonGame=False
        self.recentAction=""
        #For printing situation after a minute action
        self.spawnCounter=0
        self.monsterSlayer=False
        #Did ya JUST kill a monster?
    def levelUp(self):
        #Lets you pick stats to modify after 10 zombie kills , restores health
        if self.xp >= 100:

            print("You have leveled up! You are now level " + str(self.level+1))
            i = input("Which stat would you like increase? (damage, health, ...)")
            if i.lower() == "damage":
                # self.damagemod += 1
                self.bonusDamage+=1
                self.damage=(2*self.damagemod)+self.bonusDamage
                self.health = self.maxhealth
                self.xp=0
                self.level += 1
                self.recentAction=("Damage increased to "+str(self.damage)+"!"+"\nHealth fully restored!")
            elif i.lower() == "health":
                self.maxhealth += 8
                self.health=self.maxhealth
                self.xp=0
                self.level += 1
                self.recentAction=("Max health increased to " + str(self.maxhealth)+"!"+"\nHealth fully restored!")
            else:
                print("Not a valid stat!")
                self.levelUp()
        else:
            return None
    def goDirection(self, direction):
        self.location = self.location.getDestination(direction)
        # self.directions_list.append(direction)#~~
    def pickup(self, item): #~~
        if self.carrying+item.weight<=self.carryingCap: #~~
            self.carrying=self.carrying+item.weight
            self.items.append(item)
            item.loc = self
            self.location.removeItem(item)
        else:
            self.recentAction=('Too heavy!')
    def drop(self,item): #~~
        if item.slot==None:
            self.items.remove(item)
            self.carrying=self.carrying-item.weight   #~~
            # item.loc=self.location
            self.location.addItem(item)
        #Unequips item based on slot if you're holding it
        elif item.equipped==True:
            if item.slot == "Weapon":
                self.unequipWeapon(self.myweapon)
            elif item.slot == "Armor":
                self.unequipArmor(self.myarmor)
            elif item.slot == "Bag":
                self.unequipBag(self.mybag)
            else:
                self.unequipKey(self.mykey)
            self.items.remove(item)
            self.carrying=self.carrying-item.weight   #~~
            # item.loc=self.location
            self.location.addItem(item)
    def showInventory(self):
        #Has item stacking
            clear()
            if self.carrying == 0:
                self.recentAction = ("You don't have any items!\nTry exploring some more.")
            else:
                print("You are currently carrying:")
                print()
                k=[]
                for i in self.items:
                    k.append(i.name)
                temp=list(set(k))

                for i in temp:
                    print(i+" x "+str(k.count(i)))
                    #print(i)
                print("You are carrying " + str(self.carrying) + " pounds out of " + str(self.carryingCap))
                print()
                input("Press enter to continue...")
    def playerItem(self, name): #~~
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def eat(self, item): #**
        #Eats and heals (or harms you)
        if self.health+item.healthmod>=self.maxhealth:
            self.health=self.maxhealth
        else:
            self.health += item.healthmod
        if item in self.items:
            self.carrying-=item.weight
            self.items.remove(item)
        elif item in self.location.items:
            self.location.removeItem(item)
    #Equips proper slot and then mods correct stats
    def equipWeapon(self, weapon):
        self.damagemod=weapon.damagemod
        self.damage=2*self.damagemod+self.bonusDamage
        weapon.equipped = True
        self.myweapon=weapon
        self.myweaponname=weapon.name
    def equipArmor(self, armor):
        armor.equipped = True
        self.myarmor=armor
        self.myarmorname=armor.name
        self.damagereduction=armor.damagereduction
    def equipKey(self, key):
        key.equipped = True
        self.mykey=key
        self.mykeyname=key.name
    def equipBag(self, bag):
        bag.equipped = True
        self.mybag = bag
        self.mybagname=bag.name
        self.carrymod = bag.carrymod
        self.carryingCap += self.carrymod
        self.recentAction=("Carrying Capacity is now " + str(self.carryingCap))

    def equip(self, item): #~~
        if item.equipped:
            if item.slot == "Weapon":
                self.unequipWeapon(self.myweapon)
            elif item.slot == "Armor":
                self.unequipArmor(self.myarmor)
            elif item.slot == "Bag":
                self.unequipBag(self.mybag)

            else:
                self.unequipKey(self.mykey)

            self.recentAction=("Replaced your "+item.slot.lower()+" with "+item.name)

        if item.slot == "Weapon":
            self.equipWeapon(item)
            self.recentAction=("You are now holding: " + item.name)
        elif item.slot == "Armor":
            self.equipArmor(item)
            self.recentAction=("You are now wearing: " + item.name)
        elif item.slot == "Bag":
            self.equipBag(item)
            self.recentAction=("You are now using " + item.name)
        else:
            self.equipKey(item)
            self.recentAction=("You are now holding: " + item.name)
    def unequipWeapon(self, item): #~~
        self.myweaponname = "No weapon"
        self.myweapon = None
        item.equipped = False
        self.damage=2+self.bonusDamage
        self.damagemod=1

    def unequipArmor(self, item): #~~
        self.myarmorname= "No armor"
        self.myarmor = None
        item.equipped = False
        self.damagereduction=0
    def unequipKey(self, item): #~~
        self.mykeyname="No key"
        self.mykey = None
        item.equipped = False
    def unequipBag(self, item): #**
        self.mybagname="No bag"
        self.mybag = None
        item.equipped = False
    def unequip(self, item): #~~
        #just drop items to unequip
        if not self.item.equipped:
            print("Not wearing "+item.name)
        else:
            if item.slot == "Weapon":
                self.unequipWeapon(item)
            elif item.slot == "Armor":
                self.unequipWeapon(item)
            elif item.slot == "Bag":
                self.unequipBag(item)
            elif item.slot == "Key":
                self.unequipKey(item)
            else:
                print("That just didn't work.")
    def spawnItems(self):
        #Spawn items in the case that you jsut killed a zombie!
        if self.monsterSlayer==True:
            oboy=random.randint(1,30)
            if oboy>10:
                rf=Snacks("Rotten Flesh","It's a little slimey. Not good for eating.",.5,-8)
                rf.putInRoom(self.location)
            else:
                c=Snacks("Candy","You really should try to eat healthier...",.5,8)
                c.putInRoom(self.location)
                if oboy<5:
                    rf=Snacks("Rotten Flesh","It's a little slimey. Not good for eating.",.5,-8)
                    rf.putInRoom(self.location)
                    w=Weapon("Shotgun","Pow pow!",4,3.25)
                    w.putInRoom(self.location)
            self.monsterSlayer=False

    def attackMonster(self, mon): #~~
        clear()
        while self.health >= 0 and mon.health >= 0:
            clear()
            FightArt(False,False)
            print("")
            print("Your health is " + str(round(self.health,2)) + ".")
            print(mon.name + "'s health is " + str(mon.health) + ".")
            #**
            self.health -= round(mon.damage*(1-self.damagereduction),1)
            mon.health -= round(self.damage,1)
            print("")
            print("You attacked "+mon.name +" for "+ str(round(self.damage,2))+" damage.")
            print(mon.name+" attacked you for "+str(round(mon.damage*(1-self.damagereduction),2)) +" damage.")
            input("Press enter to continue...")
        if self.health <= 0:
            self.alive=False
        elif mon.health <= 0:
            self.health=round(self.health,1)
            print("You win. Your health is now " + str(round(self.health,2)) + ".")
            self.monsterSlayer=True
            self.spawnItems()
            #If you win, world drops items, kill counter increases, and xp goes up. @100 u lvl up successfully
            if mon in self.location.monsters:
                self.location.removeMonster(mon)
                updater.deregister(mon)

            self.zombieKillCounter += 1
            #you can change specific xp bonuses for each monster class
            self.xp += mon.xpMod
            self.levelUp()

            print("Level: "+str(self.level)+"  Experience: "+str(self.xp))
            print("Zombies Killed: "+str(self.zombieKillCounter))
            print()
            input("Press enter to continue...")
            return True
        else:
            self.alive=False
