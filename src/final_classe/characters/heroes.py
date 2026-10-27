"""Hero : un héros a toujours un job, qui fixe ses PV, ses PM, sa VIT et sa compétence."""

from abc import abstractmethod
from typing import override

from final_classe.characters.base import Character


class Hero(Character):
    """Un héros de Final Classe. Abstraite : on crée toujours un job."""

    BASE_HP = 600
    BASE_MP = 60
    SPEED = 10
    JOB_NAME = "Héros"
    SKILL_NAME = "Compétence"
    SKILL_COST = 0
    SKILL_TARGET = "ennemi"  # « ennemi », « allié », ou « ennemis » : tous les ennemis
    SKILL_TEXT = "{user} utilise {skill} sur {target} : {value} dégâts."
    POTION_HEAL = 200

    def __init__(self, name: str, strength: int, magic: int, defense: int, resistance: int) -> None:
        super().__init__(
            name, self.BASE_HP, self.BASE_MP, strength, magic, defense, resistance, self.SPEED
        )
        self.potions = 3
        self.level = 1
        self.xp = 0
        self.guarding = False  # en garde : les coups reçus sont divisés par deux

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
    def title(self) -> str:
        """Le nom du job."""
        return self.JOB_NAME

    @property
    def can_use_skill(self) -> bool:
        """Vrai s'il reste assez de PM pour la compétence."""
        return self._mp >= self.SKILL_COST

    @property
    def xp_to_next(self) -> int:
        """L'XP qu'il faut pour passer au niveau suivant."""
        return self.level * 100

    def use_skill(self, *targets: Character) -> int:
        """La méthode modèle : paie les PM une fois, puis applique l'effet à chaque cible."""
        if not self.can_use_skill:
            return 0
        self._mp -= self.SKILL_COST
        return sum(self.skill_effect(target) for target in targets)

    @abstractmethod
    def skill_effect(self, target: Character) -> int:
        """L'effet de la compétence sur une cible : chaque job écrit le sien."""

    def start_turn(self) -> None:
        """Le début du tour du héros : il quitte sa garde."""
        self.guarding = False

    def defend(self) -> None:
        """Se met en garde jusqu'à son prochain tour."""
        self.guarding = True

    @override
    def take_damage(self, amount: int) -> int:
        """En garde, le héros n'encaisse que la moitié du coup."""
        if self.guarding:
            amount //= 2
        return super().take_damage(amount)

    def drink_potion(self) -> int:
        """Boit une potion ; renvoie les PV rendus, ou 0 s'il n'en reste plus."""
        if self.potions == 0:
            return 0
        self.potions -= 1
        return self.heal(Hero.POTION_HEAL)

    def rest(self) -> None:
        """Entre deux combats : tous les PV et les PM, même après un K.O."""
        self._hp = self.max_hp
        self._mp = self.max_mp

    def gain_xp(self, amount: int) -> int:
        """Ajoute de l'XP ; renvoie le nombre de niveaux gagnés."""
        self.xp += amount
        levels = 0
        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level += 1
            self.max_hp += 100
            self.max_mp += 10
            self.strength += 3
            self.magic += 3
            self.defense += 3
            self.resistance += 3
            levels += 1
        if levels:  # un nouveau niveau remet les PV et les PM au maximum
            self.rest()
        return levels
