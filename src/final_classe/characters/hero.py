class Hero:
    BASE_HP = 600
    BASE_MP = 60
    DAMAGE_CAP = 9999

    def __init__(
            self,
            name: str,
            strength: int,
            magic: int,
            defense: int,
            resistance: int):

        if min(strength, magic, defense, resistance) < 1:
            raise ValueError("Chaque statistique doit au moins valoir 1")

        self.name = name
        self.strength = strength
        self.magic = magic
        self.defense = defense
        self.resistance = resistance
        self.max_hp = Hero.BASE_HP
        self.max_mp = Hero.BASE_MP
        self._hp = self.max_hp
        self._mp = self.max_mp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Un héro doit avoir un nom")
        self._name = value

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def mp(self) -> int:
        return self._mp

    @property
    def hp_ratio(self) -> float:
        return self.hp / self.max_hp

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> int:
        if not self.is_alive:
            return 0

        lost = min(amount, self.hp)

        self._hp -= lost

        return lost

    def heal(self, amount) -> int:
        if not self.is_alive:
            return 0

        gained = min(amount, self.max_hp - self.hp)

        self._hp += gained

        return gained

    def attack(self, target: Hero) -> int:
        damage = self.strength * 10 - target.defense * 5
        damage = max(1, min(Hero.DAMAGE_CAP, damage))
        return target.take_damage(damage)
