from npc import NPC
from utilz.constants import *


class Knight(NPC):

    def __init__(self):
        super().__init__(NPCHealth.knightHealth, NPCDamage.knightDamage, NPCArmour.knightArmour,
                         NPCMagicResist.knightMagicResist, NPCMagic.knightMagic, NPCHunger.knightHunger,
                         NPCMana.knightMana)
