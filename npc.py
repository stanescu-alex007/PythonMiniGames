import npc_states
from npc_states import *
from utilz.constants import *


class NPC(object):
    def __init__(self, hp, damage, armour, magic_resist, magic, hunger, mana):
        self.hp = hp
        self.damage = damage
        self.armour = armour
        self.magic_resist = magic_resist
        self.magic = magic
        self.hunger = hunger
        self.mana = mana
        self.alive = True

    def getState(self):
        if self.alive:
            return NPCStates.ALIVE
        else:
            return NPCStates.DEAD

    def getMana(self):
        return self.mana

    def takeBuffDamage(self, debuff):
        state = self.getState()
        if state == NPCStates.ALIVE:
            match debuff:
                case NPCDeBuff.BURNING:
                    self.hp -= NPCDeBuffDamage.fireDamage
                    print("AUCH IT'S FIREEEE!!!")
                    return
                case NPCDeBuff.POISONED:
                    self.hp -= NPCDeBuffDamage.poisonDamage
                    print("AUCH IT'S POISON!!!")
                    return
                case NPCDeBuff.STARVING:
                    self.hp -= NPCDeBuffDamage.starvingDamage
                    print("AUCH I NEED FOOD")
                    return
                case _:
                    print("yuhuuu I am healthy!!!!!")
                    return

    def healing(self):
        state = self.getState()

        if state == NPCStates.ALIVE:
            self.hp += NPCDeBuffDamage.healingHealth + int(10 / 100 * self.mana)
            self.mana -= 10 / 100 * NPCMana.knightMana

    def attack(self, victim):
        state = self.getState()
        if state == NPCStates.ALIVE:
            if victim.armour > 0:
                victim.hp -= int(50 / 100 * self.damage)
                victim.armour -= int(30 / 100 * self.damage)
                if victim.armour < 0:
                    victim.armour = 0
            else:
                victim.hp -= self.damage
                if victim.hp < 0:
                    victim.hp = 0

    def dead(self):
        if self.hp == 0:
            self.alive = False
