"""Les personnages : ils ne lisent ni n'affichent rien."""

from final_classe.characters.character import Character
from final_classe.characters.bestiary import Flan, Sephiroth, Wolf
from final_classe.characters.hero import Hero
from final_classe.characters.hit import Hit
from final_classe.characters.jobs import BlackMage, Soldier
from final_classe.characters.monster import Monster

__all__ = [
    "BlackMage",
    "Character",
    "Flan",
    "Hero",
    "Hit",
    "Monster",
    "Sephiroth",
    "Soldier",
    "Wolf",
]