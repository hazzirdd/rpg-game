import all_enemies
import random

dict_enemies = {
    "Goblin": all_enemies.goblin,
    "Wolf": {
        "attack": 2,
        "health": 3,
        "accuracy": 4,
        "drops": {
            "common": {"Wolf Skin": 1, "Wolf Fang": 1},
            "rare": {"Wolf Armor": 1, "Wolf Fang Spear": 1},
            "legendary": {"White Wolf Armor": 1, "Wolf Trophy": 1},
            "coin min": 0,
            "coin max": 4,
        },
    },
}
foe = 'Goblin'

goblin = dict_enemies["Goblin"]

rand = random.choice(dict_enemies[foe].l_drops)
loot_val = random.choice(all_enemies.wolf.r_drops)
print(rand)