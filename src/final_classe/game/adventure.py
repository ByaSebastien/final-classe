"""Le déroulement de la partie."""

from final_classe.characters import (
    Ahriman,
    Bomb,
    Cactuar,
    Flan,
    Hero,
    Malboro,
    Monster,
    Sephiroth,
    Soldier,
    Wolf,
)
from final_classe.game.battle import fight
from final_classe.game.creation import ask_name, create_hero
from final_classe.game.display import banner, console, hero_sheet
from final_classe.game.recruit import recruit


def prologue() -> None:
    """Nibelheim, il y a cinq ans : un duel perdu d'avance."""
    console.print("[italic]Nibelheim, il y a cinq ans…[/]\n")
    # Cloud, cinq ans plus tôt : moins aguerri que la recrue qu'on rencontrera ensuite.
    cloud = Soldier("Cloud", strength=20, magic=12, defense=15, resistance=13)
    sephiroth = Sephiroth()
    while cloud.is_alive:
        damage = cloud.attack(sephiroth)
        console.print(f"Cloud frappe Sephiroth : [bold]{damage}[/] dégât(s).")
        damage = sephiroth.attack(cloud)
        console.print(f"Sephiroth frappe Cloud : [bold red]{damage}[/] dégâts.")
    console.print(f"\n{hero_sheet(cloud)}")
    console.print(f"Sephiroth : PV {sephiroth.hp}/{sephiroth.max_hp}")
    console.print("\nSephiroth : « Tu n'es qu'une marionnette. »")
    console.print("[italic]Un jour, tu reviendras. Et cette fois, tu seras prêt.[/]")


def reward(heroes: list[Hero], monsters: list[Monster]) -> None:
    """L'XP va à chaque héros debout ; les gils, et ceux volés, au héros du joueur."""
    xp = sum(monster.xp for monster in monsters)
    gil = sum(monster.gil for monster in monsters)
    for hero in heroes[1:]:  # les gils volés par un compagnon rejoignent la bourse commune
        gil += hero.gil
        hero.gil = 0
    heroes[0].gil += gil
    console.print(f"Butin : [yellow]+{xp} XP[/] pour chaque héros debout, [yellow]+{gil} gils[/]")
    for hero in heroes:
        if hero.is_alive and hero.gain_xp(xp) > 0:
            console.print(f"[bold yellow]{hero.name} passe au niveau {hero.level} ![/]")


def cross(zone: str, heroes: list[Hero], waves: list[list[Monster]]) -> bool:
    """Traverse une zone, vague après vague ; renvoie False si l'équipe tombe."""
    console.print(f"\n[bold cyan]=== {zone} ===[/]")
    for monsters in waves:
        if not fight(heroes, monsters):
            console.print("[bold red]=== Game over ===[/]")
            return False
        reward(heroes, monsters)
        for hero in heroes:
            hero.rest()
        console.print("L'équipe se repose : PV et PM au maximum.")
    console.print(f"\n[bold green]{zone} : traversée ![/]")
    return True


def run() -> None:
    """Le prologue, la création du héros, le recrutement, puis deux zones."""
    console.print(banner())
    prologue()
    console.print("\n[bold]Cinq ans plus tard…[/]")
    heroes = recruit(create_hero(ask_name()))
    for hero in heroes:
        console.print(hero_sheet(hero))
    plains: list[list[Monster]] = [
        [Flan()],
        [Wolf("Loup A"), Wolf("Loup B")],
        [Flan(), Wolf("Loup alpha", hp=600, strength=20)],  # bonus ★★★ 5 : **kwargs
    ]
    forest: list[list[Monster]] = [
        [Bomb(), Ahriman()],
        [Cactuar()],
        [Bomb("Bombo A"), Bomb("Bombo B"), Ahriman()],
        [Malboro()],
    ]
    if cross("Les Plaines de Dalmasca", heroes, plains):
        cross("La Forêt de Macalania", heroes, forest)
