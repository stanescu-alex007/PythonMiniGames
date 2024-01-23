from npc import NPC
from utilz.constants import *


class Wizard(NPC):

    def __init__(self):
        super().__init__(NPCHealth.wizardHealth, NPCDamage.wizardDamage, NPCArmour.wizardArmour, NPCMagicResist.wizardMagicResist, NPCMagic.wizardMagic, NPCHunger.wizardHunger, NPCMana.wizardMana)
