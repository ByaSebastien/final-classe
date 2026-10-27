from abc import ABC, abstractmethod


class Character(ABC):

    DAMAGE_CAP = 9999

    def __init__(
        self,
        name: str,
        hp: int,
        mp: int,
        strength: int,
        magic: int,
        defense: int,
        resistance: int,
        speed: int,
    ) -> None:
        if min(hp, strength, magic, defense, resistance, speed) < 1:
            raise ValueError("Chaque statistique vaut au moins 1")
        self.name = name
        self.strength = strength
        self.magic = magic
        self.defense = defense
        self.resistance = resistance
        self.speed = speed
        self.max_hp = hp
        self.max_mp = mp
        self._hp = hp
        self._mp = mp
        self.gil = 0

    @property
    @abstractmethod
    def title(self):
        """Ce qui s'affiche après le nom : le job du héros, ou « Monstre »."""

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def mp(self) -> int:
        return self._mp

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    @property
    def hp_ratio(self) -> float:
        return self.hp / self.max_hp

    def strike(self, target: Character, damage) -> int:
        damage = max(1,min(self.DAMAGE_CAP, damage))
        return target.take_damage(damage)

    def attack(self,target: Character) -> int:
        if not self.is_alive:
            return 0
        return self.strike(target, self.strength * 10 - target.defense * 5)

    def magic_damage(self, target: Character, power: int) -> int:
        if not self.is_alive:
            return 0
        return self.strike(target, self.magic * power - target.resistance * 5)

    def take_damage(self, amount: int) -> int:
        lost = min(amount, self.hp)
        self._hp -= lost
        return lost

    def heal(self, amount: int) -> int:
        if not self.is_alive:
            return 0
        gained = min(amount,self.max_hp - self.hp)
        self._hp += gained
        return gained
