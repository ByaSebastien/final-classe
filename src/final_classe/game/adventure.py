"""Le déroulement de la partie."""

from final_classe.characters import Hero
from final_classe.game.display import banner, console, hero_sheet


def prologue() -> None:
    """Nibelheim, il y a cinq ans : un duel perdu d'avance."""
    console.print("[italic]Nibelheim, il y a cinq ans…[/]\n")
    cloud = Hero("Cloud", strength=20, magic=12, defense=15, resistance=13)
    sephiroth = Hero("Sephiroth", strength=50, magic=60, defense=99, resistance=99)
    while cloud.is_alive and sephiroth.is_alive:
        console.print(hero_sheet(cloud))
        console.print(hero_sheet(sephiroth))
        damage = cloud.attack(sephiroth)
        console.print(f"Cloud frappe Sephiroth : [bold]{damage}[/] dégât(s).")
        damage = sephiroth.attack(cloud)
        console.print(f"Sephiroth frappe Cloud : [bold red]{damage}[/] dégâts.\n")
    console.print(hero_sheet(cloud))
    console.print("\nSephiroth : « Tu n'es qu'une marionnette. »")
    console.print("[italic]Un jour, tu reviendras. Et cette fois, tu seras prêt.[/]")


def run() -> None:
    """Lance la partie."""
    console.print(banner())
    prologue()
