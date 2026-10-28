"""Character : tout ce que les héros et les monstres partagent."""

from abc import ABC, abstractmethod


class Character(ABC):
    """Un combattant de Final Classe : un héros ou un monstre."""

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
        self._strength = strength
        self._magic = magic
        self._defense = defense
        self._resistance = resistance
        self._speed = speed
        self.max_hp = hp
        self.max_mp = mp
        self._hp = hp
        self._mp = mp
        self.gil = 0

    @property
    @abstractmethod
    def title(self) -> str:
        """Ce qui s'affiche après le nom : le job du héros, ou « Monstre »."""

    @property
    def strength(self) -> int:
        return self._strength

    @property
    def magic(self) -> int:
        return self._magic

    @property
    def defense(self) -> int:
        return self._defense

    @property
    def resistance(self) -> int:
        return self._resistance

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def hp(self) -> int:
        """Les PV actuels : en lecture seule."""
        return self._hp

    @property
    def mp(self) -> int:
        """Les PM actuels : en lecture seule."""
        return self._mp

    @property
    def is_alive(self) -> bool:
        """Vrai tant qu'il reste des PV."""
        return self._hp > 0

    @property
    def hp_ratio(self) -> float:
        """La part de PV restante, entre 0 et 1."""
        return self._hp / self.max_hp

    def strike(self, target: Character, damage: int) -> int:
        """Inflige des dégâts bornés entre 1 et 9999 ; renvoie les PV perdus par la cible."""
        damage = max(1, min(Character.DAMAGE_CAP, damage))
        return target.take_damage(damage)

    def attack(self, target: Character) -> int:
        """L'attaque physique : la FOR contre la DÉF de la cible."""
        return self.strike(target, self.strength * 10 - target.defense * 5)

    def magic_attack(self, target: Character, power: int) -> int:
        """L'attaque magique : la MAG contre la RÉS de la cible."""
        return self.strike(target, self.magic * power - target.resistance * 5)

    def take_damage(self, amount: int) -> int:
        """Retire des PV, sans descendre sous 0 ; renvoie les PV réellement perdus."""
        lost = min(amount, self._hp)
        self._hp -= lost
        return lost

    def heal(self, amount: int) -> int:
        """Rend des PV à un personnage debout, sans dépasser le maximum ; renvoie les PV rendus."""
        if not self.is_alive:
            return 0
        gained = min(amount, self.max_hp - self._hp)
        self._hp += gained
        return gained

    def lower_defense(self) -> None:
        self._defense = max(1, self.defense // 2)