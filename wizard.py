from npc import NPC
from npc_states import *
from utilz.constants import *


class Wizard(NPC):

    def __init__(self):
        super().__init__(NPCHealth.wizardHealth, NPCDamage.wizardDamage, NPCArmour.wizardArmour,
                         NPCMagicResist.wizardMagicResist, NPCMagic.wizardMagic, NPCHunger.wizardHunger,
                         NPCMana.wizardMana)

    def healing(self):
        state = self.getState()

        if state == NPCStates.ALIVE:
            self.hp += NPCDeBuffDamage.healingHealth + int(20 / 100 * self.mana)
            if self.hp > NPCHealth.wizardHealth:
                self.hp = NPCHealth.wizardHealth
            self.mana -= 10 / 100 * NPCMana.wizardMana
