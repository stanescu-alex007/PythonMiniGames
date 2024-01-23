from npc import NPC
from utilz.constants import *


class Archer(NPC):

    def __init__(self):
            super().__init__(NPCHealth.archerHealth, NPCDamage.archerDamage, NPCArmour.archerArmour, NPCMagicResist.archerMagicResist, NPCMagic.archerMagic, NPCHunger.archerHunger, NPCMana.archerMana)
