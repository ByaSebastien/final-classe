"""Le combat : l'équipe contre un groupe de monstres, dans l'ordre de la VIT."""

from collections.abc import Sequence

from final_classe.characters import Character, Hero, Monster
from final_classe.game.creation import ask_int
from final_classe.game.display import console, hero_line, monster_line


def standing(characters: Sequence[Character]) -> list[Character]:
    """Les personnages encore debout."""
    return [character for character in characters if character.is_alive]


def by_speed(character: Character) -> int:
    """La clé de tri du tour : la VIT."""
    return character.speed


def choose_target(characters: Sequence[Character], prompt: str = "Cible") -> Character:
    """Le joueur choisit une cible ; pas de question s'il n'y en a qu'une."""
    if len(characters) == 1:
        return characters[0]
    for number, character in enumerate(characters, start=1):
        console.print(f"  {number}. {character.name} (PV {character.hp}/{character.max_hp})")
    return characters[ask_int(f"{prompt} : ", 1, len(characters)) - 1]


def skill_targets(hero: Hero, heroes: list[Hero], monsters: list[Monster]) -> list[Character]:
    """Les cibles de la compétence, d'après SKILL_TARGET."""
    if hero.SKILL_TARGET == "ennemis":
        return standing(monsters)
    if hero.SKILL_TARGET == "allié":
        return [choose_target(standing(heroes), "Allié")]
    return [choose_target(standing(monsters))]


def hero_turn(hero: Hero, heroes: list[Hero], monsters: list[Monster]) -> None:
    """Le tour d'un héros : le joueur choisit son action."""
    hero.start_turn()
    skill = f"{hero.SKILL_NAME} ({hero.SKILL_COST} PM)"
    potion = f"Potion (x{hero.potions})"
    menu = f"[bold]{hero.name}[/] : 1. Attaquer  2. {skill}  3. {potion}  4. Se défendre"
    while True:
        console.print(menu)
        choice = ask_int("> ", 1, 4)
        if choice == 4:
            hero.defend()
            console.print(f"{hero.name} se met en garde : les coups reçus sont divisés par deux.")
            return
        if choice == 1:
            target = choose_target(standing(monsters))
            damage = hero.attack(target)
            console.print(f"{hero.name} attaque {target.name} : [bold]{damage}[/] dégâts.")
            if not target.is_alive:
                console.print(f"[green]{target.name} est vaincu ![/]")
            return
        if choice == 2:
            if not hero.can_use_skill:
                console.print("[red]Pas assez de PM ![/]")
                continue
            targets = skill_targets(hero, heroes, monsters)
            value = hero.use_skill(*targets)
            names = ", ".join(target.name for target in targets)
            text = hero.SKILL_TEXT.format(
                user=hero.name, skill=hero.SKILL_NAME, target=names, value=value
            )
            console.print(text)
            for target in targets:
                if target in monsters and not target.is_alive:
                    console.print(f"[green]{target.name} est vaincu ![/]")
            return
        if hero.potions == 0:
            console.print("[red]Plus de potion ![/]")
            continue
        console.print(f"{hero.name} boit une potion : [green]+{hero.drink_potion()} PV[/]")
        return


def monster_turn(monster: Monster, heroes: list[Hero]) -> None:
    """Le tour d'un monstre : il agit, et le combat affiche chaque coup."""
    for hit in monster.act(heroes):
        damage = f"[bold red]{hit.damage}[/] dégâts"
        console.print(f"{monster.name} : {hit.action} sur {hit.target.name}, {damage}.")
        if not hit.target.is_alive:
            console.print(f"[red]{hit.target.name} est K.O.[/]")
    if monster.is_alive and monster.warning:
        console.print(f"[yellow]{monster.warning}[/]")


def fight(heroes: list[Hero], monsters: list[Monster]) -> bool:
    """Le combat d'équipe ; renvoie True si l'équipe gagne."""
    names = ", ".join(monster.name for monster in monsters)
    console.print(f"\n[bold red]Combat contre {names}[/]")
    turn = 0
    while standing(heroes) and standing(monsters):
        turn += 1
        console.print(f"\n[bold]--- Tour {turn} ---[/]")
        for hero in heroes:
            console.print(hero_line(hero))
        for monster in standing(monsters):
            console.print(monster_line(monster))
        order = sorted([*heroes, *monsters], key=by_speed, reverse=True)
        queue = " → ".join(character.name for character in standing(order))
        console.print(f"[dim]Ordre du tour : {queue}[/]")  # bonus ★ 2
        for character in order:
            if not character.is_alive or not standing(heroes) or not standing(monsters):
                continue
            # Pas une cascade de cas par espèce : on sépare les deux camps.
            # Pour un héros, le joueur décide ; un monstre décide seul.
            if isinstance(character, Hero):
                hero_turn(character, heroes, monsters)
            elif isinstance(character, Monster):
                monster_turn(character, heroes)
    won = bool(standing(heroes))
    console.print("\n[bold green]Victoire ![/]" if won else "\n[bold red]L'équipe est K.O…[/]")
    return won
