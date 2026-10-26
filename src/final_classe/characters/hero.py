"""Le héros : ses statistiques, ses PV et ses PM."""


class Hero:
    """Un héros de Final Classe."""

    BASE_HP = 600
    BASE_MP = 60
    DAMAGE_CAP = 9999

    def __init__(self, name: str, strength: int, magic: int, defense: int, resistance: int) -> None:
        if min(strength, magic, defense, resistance) < 1:
            raise ValueError("Chaque statistique vaut au moins 1")
        self.name = name  # passe par le setter
        self.strength = strength
        self.magic = magic
        self.defense = defense
        self.resistance = resistance
        self.max_hp = Hero.BASE_HP
        self.max_mp = Hero.BASE_MP
        self._hp = self.max_hp
        self._mp = self.max_mp

    @property
    def name(self) -> str:
        """Le nom du héros."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        value = value.strip()
        if not value:
            raise ValueError("Un héros a besoin d'un nom")
        self._name = value

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

    def attack(self, target: Hero) -> int:
        """Frappe la cible ; renvoie les PV qu'elle a perdus."""
        damage = self.strength * 10 - target.defense * 5
        damage = max(1, min(Hero.DAMAGE_CAP, damage))
        return target.take_damage(damage)

    def take_damage(self, amount: int) -> int:
        """Retire des PV, sans descendre sous 0 ; renvoie les PV réellement perdus."""
        lost = min(amount, self._hp)
        self._hp -= lost
        return lost

    def heal(self, amount: int) -> int:
        """Rend des PV à un héros debout, sans dépasser le maximum ; renvoie les PV rendus."""
        if not self.is_alive:
            return 0
        gained = min(amount, self.max_hp - self._hp)
        self._hp += gained
        return gained
