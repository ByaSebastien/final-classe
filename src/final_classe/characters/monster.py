"""Le monstre : les mêmes statistiques que le héros."""
import random
from typing import override, Sequence, List

from final_classe.characters.character import Character
from final_classe.characters.hit import Hit


class Monster(Character):
    """Un monstre de Final Classe."""

    NAME = "Monstre"
    HP = 100
    MP = 0
    STRENGTH = 10
    MAGIC = 1
    DEFENSE = 1
    RESISTANCE = 1
    SPEED = 10
    XP = 0
    GIL = 0

    def __init__(
        self,
        name: str | None = None
    ) -> None:
        super().__init__(
            name or self.NAME,
            self.HP,
            self.MP,
            self.STRENGTH,
            self.MAGIC,
            self.DEFENSE,
            self.RESISTANCE,
            self.SPEED
        )
        self.xp = self.XP
        self.gil = self.GIL

    @property
    @override
    def title(self) -> str:
        return self.NAME

    def act(self, heroes: Sequence[Character]) -> List[Hit]:
        target = random.choice([hero for hero in heroes if hero.is_alive])
        damage = self.attack(target)
        return [Hit("attaque",target, damage)]
