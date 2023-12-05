import npc_states
from npc_states import *


class NPC(object):
    def __init__(self, hp, damage, armour, magic, hunger):
        self.hp = hp
        self.damage = damage
        self.armour = armour
        self.magic = magic
        self.hunger = hunger
        self.alive = True

    def getState(self):
        if self.alive:
            return NPCStates.ALIVE
        else:
            return NPCStates.DEAD

    def takeDamage(self, debuff, damage):
        state = self.getState()
        if state == NPCStates.ALIVE:
            match debuff:
                case NPCDeBuff.BURNING:
                    self.hp -= damage
                    print("AUCH IT'S FIREEEE!!!")
                    return
                case NPCDeBuff.POISONED:
                    self.hp -= damage
                    print("AUCH IT'S POISON!!!")
                    return
                case NPCDeBuff.STARVING:
                    self.hp -= damage
                    print("AUCH I NEED FOOD")
                    return
                case _:
                    print("yuhuuu I am healthy!!!!!")
                    return
