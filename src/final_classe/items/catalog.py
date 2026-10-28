from final_classe.items.equipment import Equipment


def bronze_sword() -> Equipment:
    return Equipment("Épée de bronze", "arme", 100, strength=4)


def rod() -> Equipment:
    return Equipment("Bâton", "arme", 100, magic=4)


def leather_armor() -> Equipment:
    return Equipment("Armure de cuir", "armure", 100, defense=4)


def chain_mail() -> Equipment:
    return Equipment("Cotte de mailles", "armure", 300, defense=8, resistance=2)
