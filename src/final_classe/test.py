import random

from final_classe.characters import Soldier, BlackMage, Flan, Wolf

random.seed(1)
cloud = Soldier("Cloud", 22, 12, 16, 10)
lulu = BlackMage("Lulu", 10, 22, 12, 16)
flan, wolf = Flan(), Wolf()
print(cloud.title, cloud.max_hp, cloud.speed)
print(lulu.use_skill(flan), lulu.mp)
print(cloud.use_skill(wolf), wolf.hp)
hit = flan.act([cloud, lulu])[0]
print(hit.action, hit.target.name, hit.damage)