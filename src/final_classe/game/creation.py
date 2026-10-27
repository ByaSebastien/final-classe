from final_classe.characters import Hero, Soldier, BlackMage
from final_classe.game.display import console

POINTS = 20
BASE_STAT = 10

JOBS: list[type[Hero]] = [Soldier, BlackMage]  # des classes, rangées dans une liste

def choose_job() -> type[Hero]:
    """Le menu des jobs, construit à partir des classes : renvoie la classe choisie."""
    for number, job in enumerate(JOBS, start=1):
        console.print(
            f"  {number}. {job.JOB_NAME:<10} PV {job.BASE_HP}  PM {job.BASE_MP}  "
            f"VIT {job.SPEED}  compétence : {job.SKILL_NAME}"
        )
    return JOBS[ask_int("Votre job : ", 1, len(JOBS)) - 1]

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
    """Le job, puis les points entre FOR, MAG et DÉF ; la RÉS reçoit le reste."""
    job = choose_job()
    console.print(f"Chaque statistique vaut {BASE_STAT}. Répartissez {POINTS} points.")
    remaining = POINTS
    bonus: dict[str, int] = {}
    for stat in ("FOR", "MAG", "DÉF"):
        points = ask_int(f"{stat} (+0 à +{remaining}) : ", 0, remaining)
        bonus[stat] = points
        remaining -= points
    bonus["RÉS"] = remaining
    console.print(f"RÉS reçoit les {remaining} points restants.")
    return job(
        name,
        strength=BASE_STAT + bonus["FOR"],
        magic=BASE_STAT + bonus["MAG"],
        defense=BASE_STAT + bonus["DÉF"],
        resistance=BASE_STAT + bonus["RÉS"],
    )