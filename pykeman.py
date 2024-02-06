from npc import NPC
from npc_states import *
from utilz.constants import *


class Pykeman(NPC):

    def __init__(self):
        super().__init__(NPCHealth.pykemanHealth, NPCDamage.pykemanDamage, NPCArmour.pykemanArmour,
                         NPCMagicResist.pykemanMagicResist, NPCMagic.pykemanMagic, NPCHunger.pykemanHunger,
                         NPCMana.pykemanMana)

    def healing(self):
        state = self.getState()

        if state == NPCStates.ALIVE:
            self.hp += NPCDeBuffDamage.healingHealth + int(10 / 100 * self.mana)
            if self.hp > NPCHealth.pykemanHealth:
                self.hp = NPCHealth.pykemanHealth
            self.mana -= 10 / 100 * NPCMana.pykemanMana
