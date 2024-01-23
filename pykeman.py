from npc import NPC
from utilz.constants import *


class Pykeman(NPC):

    def __init__(self):
        super().__init__(NPCHealth.pykemanHealth, NPCDamage.pykemanDamage, NPCArmour.pykemanArmour, NPCMagicResist.pykemanMagicResist, NPCMagic.pykemanMagic, NPCHunger.pykemanHunger, NPCMana.pykemanMana)
