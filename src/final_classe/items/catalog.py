"""Le catalogue : chaque fonction fabrique une pièce neuve."""

from final_classe.items.equipment import Equipment
from final_classe.items.materia import AttackMateria, HealMateria, Materia, SummonMateria


def bronze_sword() -> Equipment:
    """Une épée simple."""
    return Equipment("Épée de bronze", "arme", 100, strength=4)


def rod() -> Equipment:
    """Le bâton des mages."""
    return Equipment("Bâton", "arme", 100, magic=4)


def leather_armor() -> Equipment:
    """Une armure légère."""
    return Equipment("Armure de cuir", "armure", 100, defense=4)


def chain_mail() -> Equipment:
    """Une armure plus lourde, qui protège aussi un peu de la magie."""
    return Equipment("Cotte de mailles", "armure", 300, defense=8, resistance=2)


def mythril_sword() -> Equipment:
    """Une épée solide, avec deux emplacements de materia."""
    return Equipment("Épée de mythril", "arme", 600, strength=8, slots=2)


def mythril_rod() -> Equipment:
    """Un bâton qui canalise la magie, avec deux emplacements."""
    return Equipment("Bâton de mythril", "arme", 600, magic=8, slots=2)


def mythril_armor() -> Equipment:
    """Une armure de mythril, avec un emplacement."""
    return Equipment("Armure de mythril", "armure", 600, defense=10, resistance=6, slots=1)


def ribbon() -> Equipment:
    """Bonus ★ 1. Le Ruban : l'accessoire légendaire."""
    return Equipment("Ruban", "accessoire", 2000, resistance=12, speed=2)


def fire() -> Materia:
    """Feu."""
    return AttackMateria("Feu", 8, 12, "feu")


def ice() -> Materia:
    """Glace."""
    return AttackMateria("Glace", 8, 12, "glace")


def thunder() -> Materia:
    """Foudre."""
    return AttackMateria("Foudre", 8, 12, "foudre")


def cure() -> Materia:
    """Soin."""
    return HealMateria("Soin", 10, 12)


def ifrit() -> Materia:
    """Bonus ★★ 3. Ifrit : Flammes de l'enfer sur tous les ennemis."""
    return SummonMateria("Ifrit", 90, 90, "feu")


def shiva() -> Materia:
    """Bonus ★★ 3. Shiva : Poussière de diamant sur tous les ennemis."""
    return SummonMateria("Shiva", 30, 20, "glace")


def ramuh() -> Materia:
    """Bonus ★★ 3. Ramuh : Jugement divin sur tous les ennemis."""
    return SummonMateria("Ramuh", 30, 20, "foudre")
