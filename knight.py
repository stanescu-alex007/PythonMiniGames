from npc import NPC
from npc_states import *
from utilz.constants import *


class Knight(NPC):

    def __init__(self):
        super().__init__(NPCHealth.knightHealth, NPCDamage.knightDamage, NPCArmour.knightArmour,
                         NPCMagicResist.knightMagicResist, NPCMagic.knightMagic, NPCHunger.knightHunger,
                         NPCMana.knightMana)

    def healing(self):
        state = self.getState()

        if state == NPCStates.ALIVE:
            self.hp += NPCDeBuffDamage.healingHealth + int(10 / 100 * self.mana)
            if self.hp > NPCHealth.knightHealth:
                self.hp = NPCHealth.knightHealth
            self.mana -= int(10 / 100 * NPCMana.knightMana)
