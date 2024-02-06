from npc import NPC
from npc_states import *
from utilz.constants import *


class Archer(NPC):

    def __init__(self):
        super().__init__(NPCHealth.archerHealth, NPCDamage.archerDamage, NPCArmour.archerArmour,
                         NPCMagicResist.archerMagicResist, NPCMagic.archerMagic, NPCHunger.archerHunger,
                         NPCMana.archerMana)

    def healing(self):
        state = self.getState()

        if state == NPCStates.ALIVE:
            self.hp += NPCDeBuffDamage.healingHealth + int(10 / 100 * self.mana)
            if self.hp > NPCHealth.archerHealth:
                self.hp = NPCHealth.archerHealth
            self.mana -= 10 / 100 * NPCMana.archerMana
