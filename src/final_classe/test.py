from final_classe.characters import Hero, Monster

flan = Monster("Flan", hp=450, mp=0, strength=14, magic=1, defense=18, resistance=4)
vaan = Hero("Vaan", strength=15, magic=15, defense=15, resistance=15)
print(vaan.cast_fire(flan), flan.hp, vaan.mp)
for _ in range(6):
    vaan.cast_fire(flan)
print(vaan.mp, vaan.can_cast_fire, vaan.cast_fire(flan))