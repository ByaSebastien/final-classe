"""Equipment : une pièce d'équipement, ses bonus, et ses emplacements de materia."""

from final_classe.items.materia import Materia


class Equipment:
    """Une arme, une armure… : un emplacement, un prix, des bonus, et des materias."""

    def __init__(
        self,
        name: str,
        slot: str,
        price: int,
        strength: int = 0,
        magic: int = 0,
        defense: int = 0,
        resistance: int = 0,
        speed: int = 0,
        slots: int = 0,
    ) -> None:
        self.name = name
        self.slot = slot  # « arme », « armure » ou « accessoire »
        self.price = price
        self.strength = strength
        self.magic = magic
        self.defense = defense
        self.resistance = resistance
        self.speed = speed
        self.slots = slots  # le nombre d'emplacements de materia
        self.materias: list[Materia] = []  # la pièce A DES materias

    def attach(self, materia: Materia) -> bool:
        """Monte une materia ; renvoie False s'il n'y a plus d'emplacement libre."""
        if len(self.materias) >= self.slots:
            return False
        self.materias.append(materia)
        return True

    def detach(self, materia: Materia) -> bool:
        """Bonus ★★★ 5 : retire une materia ; renvoie False si elle n'est pas montée ici."""
        if materia not in self.materias:
            return False
        self.materias.remove(materia)
        return True
