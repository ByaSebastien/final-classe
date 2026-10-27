from typing import override

from final_classe.characters import Hero
from final_classe.characters.character import Character


class Soldier(Hero):

    BASE_HP = 700
    BASE_MP = 50
    SPEED = 12
    JOB_NAME = "Soldat"
    SKILL_NAME = "Omnislash"
    SKILL_COST = 12

    def skill_effect(self, target: Character) -> int:
        return sum(self.attack(target) for _ in range(3))

class BlackMage(Hero):

    BASE_HP = 520
    BASE_MP = 90
    SPEED = 10
    JOB_NAME = "Mage noir"
    SKILL_NAME = "Météor"
    SKILL_COST = 8
    SKILL_TEXT = "{user} lance Météor sur {target} : {value} dégâts."

    @override
    def skill_effect(self, target: Character) -> int:
        return self.magic_damage(target, 15)


