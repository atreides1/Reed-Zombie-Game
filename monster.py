import random
import updater

class Monster:
    def __init__(self, name, health, room,damagemod=1): #~~Added damaage
        self.name = name
        self.health = health
        self.room = room
        self.damage=2
        self.xpMod = 10
        room.addMonster(self)
        updater.register(self)
    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())
    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)
    # def die(self):
    #     self.room.removeMonster(self)
    #     updater.deregister(self)
class ZombiePerson(Monster):
    pass
class ZombieDog(Monster):
    pass
class ZombieButterfly(Monster):
    pass
class ZombieBoss(Monster):
    pass



