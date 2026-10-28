
class Equipment:

    def __init__(
            self,
            name: str,
            slot: str,
            price: int,
            strength: int = 0,
            magic: int = 0,
            defense: int = 0,
            resistance: int = 0,
            speed: int = 0
                 ):
        self.name = name
        self.slot = slot
        self.price = price
        self.strength = strength
        self.magic = magic
        self.defense = defense
        self.resistance = resistance
        self.speed = speed