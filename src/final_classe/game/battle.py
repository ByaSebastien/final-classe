from final_classe.characters import Hero, Monster
from final_classe.game.creation import ask_int
from final_classe.game.display import console, hero_sheet, monster_line


def fight(hero: Hero, monster: Monster) -> bool:
    console.print(f"\n[bold red]Combat: {hero.name} contre {monster.name}")
    turns = 1
    while hero.is_alive and monster.is_alive:
        console.print(f"\n[bold]--- Tour {turns} ---[/]")
        console.print(hero_sheet(hero))
        console.print(monster_line(monster))

        choice = -1

        while choice not in range(1,3):
            choice = ask_int(f"1. Attaquer 2. Feu ({Hero.FIRE_COST} PM)\n>",1, 2)

            if choice == 2 and not hero.can_cast_fire:
                console.print("[red]Pas assez de PM ![/]")
                choice = -1
            elif choice == 1:
                damage = hero.attack(monster)
                console.print(f"{hero.name} attaque {monster.name} : [bold]{damage}[/] dégâts.")
            else :
                damage = hero.cast_fire(monster)
                console.print(f"{hero.name} lance Feu sur {monster.name} : [bold]{damage}[/] dégâts.")

        if monster.is_alive:
            damage = monster.attack(hero)
            console.print(f"{monster.name} attaque {hero.name} : [bold red]{damage}[/] dégâts.")
        else:
            console.print(f"[green]{monster.name} est vaincu ![/]")

        turns += 1

    won = hero.is_alive
    console.print("\n[bold green]Victoire ![/]" if won else f"\n[bold red]{hero.name} est K.O…[/]")
    return won
