import all_enemies
import random

dict_enemies = {
    "Goblin": all_enemies.goblin,
    "Fire Myte": all_enemies.fire_myte,
    "Wolf": all_enemies.wolf
}

foe = random.choice(list(dict_enemies))

fire_damage = False

print(fire_damage)

def attack_ask():
    attack = input("attack? [y/n]:  ")
    fight(attack)

def fight(attack):
    if attack == "y":
        if fire_damage == False:
            print("burn check:")
            fire_damage = all_enemies.MagicEnemy.fire_attack()
        attack_ask()

attack_ask()