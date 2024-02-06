from enum import auto, Enum


class NPCStates(Enum):
    ALIVE = auto()
    DEAD = auto()


class NPCEffects(Enum):
    FROZEN = auto()
    STUNNED = auto()
    RAGE = auto()
    HEALING = auto()


class NPCDeBuff(Enum):
    STARVING = auto()
    POISONED = auto()
    BURNING = auto()

