from typing import List

from final_classe.characters import Hero, Monster
from final_classe.items import Equipment


class Party:

    def __init__(self, heroes: List[Hero]) -> None:
        self.heroes = heroes
        self.gil = 0
        self.bag: List[Equipment] = []

    @property
    def leader(self):
        return self.heroes[0]

    @property
    def standing(self):
        return [hero for hero in self.heroes if hero.is_alive]

    def reward(self, monsters: List[Monster]) -> List[Hero]:

        xp = sum(monster.xp for monster in monsters)
        self.gil += sum(monster.gil for monster in monsters)

        for hero in self.standing:
            self.gil += hero.gil
            hero.gil = 0

        return [hero for hero in self.standing if hero.gain_xp(xp) > 0]

    def rest(self):

        for hero in self.heroes:
            hero.rest()