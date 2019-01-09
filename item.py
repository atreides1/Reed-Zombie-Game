import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc,weight):
        self.name = name
        self.desc = desc
        self.loc = None
        self.slot=None
        #Slot for equip
        self.weight= weight
        #Carry weight
        self.eatable=False
        #You can't eat armor/weapons and can't equip snax
        self.equippable=False
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)
    def getWeight(self): #~~
        return self.weight
class Armor(Item): #~~
    def __init__(self,name, desc,weight,damagereduction):
        Item.__init__(self,name, desc,weight)
        #Reduces %of damage (1 blocks all damage)
        self.damagereduction=damagereduction
        self.equipped=False
        self.slot="Armor"
        self.equippable=True
        self.eatable=False
class Weapon(Item): #~~
    def __init__(self,name, desc,weight,damagemod):
        Item.__init__(self,name, desc,weight)
        #Multiplicative mod on player damage
        self.damagemod=damagemod
        self.equipped=False
        self.slot="Weapon"
        self.equippable=True
        self.eatable=False
class Snacks(Item): #**
    def __init__(self, name, desc, weight, healthmod):
        Item.__init__(self, name, desc, weight)
        self.healthmod = healthmod
        self.eatable=True

class Bags(Item):
    def __init__(self,name, desc,weight,carrymod):
        Item.__init__(self,name, desc,weight)
        self.carrymod = carrymod
        self.equipped=False
        self.slot="Bag"
        self.equippable=True
        self.eatable=False

# class Key(Item): #~~
#     def __init__(self,name, desc,weight,damage,slot):
#         Item.__init__(self,name, desc,weight)
#         self.damage=damage
#         self.equip=False
#         self.slot="Key"
