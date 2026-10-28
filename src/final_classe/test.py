from final_classe.characters import Soldier
from final_classe.items import catalog

cloud = Soldier("Cloud", 22, 12, 16, 10)
print(cloud.strength, cloud.defense)
cloud.equip(catalog.bronze_sword())
cloud.equip(catalog.leather_armor())
print(cloud.strength, cloud.defense, [item.name for item in cloud.equipment])
previous = cloud.equip(catalog.chain_mail())
print(previous.name, cloud.defense, cloud.resistance)