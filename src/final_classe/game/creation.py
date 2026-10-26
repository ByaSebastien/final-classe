from final_classe.characters import Hero
from final_classe.game.display import console

POINTS = 20
BASE_STAT = 10

def ask_int(prompt: str, low: int, high: int) -> int:

    answer = input(prompt)

    while not answer.isdigit() or int(answer) not in range(low,high+1):
        console.print(f"[red]Un nombre entre {low} et {high}, s'il vous plaît.[/]")
        answer = input(prompt)

    return int(answer)

def ask_name() -> str:

    name = ''

    while not name:
        console.print("[red]Un héros a besoin d'un nom.[/]")
        name = input("Nom de votre héro : ").strip()

    return name.title()

def create_hero(name: str) -> Hero:
    """Répartit les points entre FOR, MAG et DÉF ; la RÉS reçoit le reste."""
    console.print(f"Chaque statistique vaut {BASE_STAT}. Répartissez {POINTS} points.")
    remaining = POINTS
    bonus: dict[str, int] = {}
    for stat in ("FOR", "MAG", "DÉF"):
        points = ask_int(f"{stat} (+0 à +{remaining}) : ", 0, remaining)
        bonus[stat] = points
        remaining -= points
    bonus["RÉS"] = remaining
    console.print(f"RÉS reçoit les {remaining} points restants.")
    return Hero(
        name,
        strength=BASE_STAT + bonus["FOR"],
        magic=BASE_STAT + bonus["MAG"],
        defense=BASE_STAT + bonus["DÉF"],
        resistance=BASE_STAT + bonus["RÉS"],
    )