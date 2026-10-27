"""Le déroulement de la partie."""

from final_classe.characters import BlackMage, Flan, Hero, Monster, Sephiroth, Soldier, Wolf
from final_classe.game.battle import fight
from final_classe.game.creation import ask_name, create_hero
from final_classe.game.display import banner, console, hero_sheet


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
    """L'XP va à chaque héros debout ; les gils, au héros du joueur."""
    xp = sum(monster.xp for monster in monsters)
    gil = sum(monster.gil for monster in monsters)
    heroes[0].gil += gil
    console.print(f"Butin : [yellow]+{xp} XP[/] pour chaque héros debout, [yellow]+{gil} gils[/]")
    for hero in heroes:
        if hero.is_alive and hero.gain_xp(xp) > 0:
            console.print(f"[bold yellow]{hero.name} passe au niveau {hero.level} ![/]")


def run() -> None:
    """Lance la partie : le prologue, la création du héros, puis les Plaines de Dalmasca."""
    console.print(banner())
    prologue()
    console.print("\n[bold]Cinq ans plus tard…[/]")
    hero = create_hero(ask_name())
    lulu = BlackMage("Lulu", strength=10, magic=22, defense=12, resistance=16)
    heroes = [hero, lulu]
    for member in heroes:
        console.print(hero_sheet(member))
    console.print("\n[bold cyan]=== Les Plaines de Dalmasca ===[/]")
    waves = [[Flan()], [Wolf("Loup A"), Wolf("Loup B")], [Flan(), Wolf()]]
    for monsters in waves:
        if not fight(heroes, monsters):
            console.print("[bold red]=== Game over ===[/]")
            return
        reward(heroes, monsters)
        for member in heroes:
            member.rest()
        console.print("L'équipe se repose : PV et PM au maximum.")
    console.print("\n[bold green]Les Plaines de Dalmasca sont traversées ![/]")
