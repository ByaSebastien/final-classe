"""Hit : un coup porté pendant un combat."""

from final_classe.characters.base import Character


class Hit:
    """Un coup porté : le nom de l'action, la cible, et les PV qu'elle a perdus."""

    def __init__(self, action: str, target: Character, damage: int) -> None:
        self.action = action
        self.target = target
        self.damage = damage
