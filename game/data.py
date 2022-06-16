import all_enemies

item_values = {
    "Goblin Ear": 1,
    "Goblin Club": 5,
    "Shiny Necklace": 8,
    "Goblin Cleaver": 9,
    "Goblin Trophy": 10,
    "Wolf Skin": 1,
    "Wolf Fang": 1,
    "Wolf Armor": 3,
    "White Wolf Armor": 8,
    "Wolf Fang Spear": 5,
    "Wolf Trophy": 10,
    "Rags": 0,
    "Wood Sword": 1,
    "God Sword": 0,
    "Iron Sword": 5,
    "health potion": 1,
}

enemies = {
    "Goblin": all_enemies.goblin,
    "Wolf": all_enemies.wolf,
    "Fire Myte": all_enemies.fire_myte
}

weapons = {
    "God Sword": {"attack": 200, "accuracy": 1000},
    "Wood Sword": {"attack": 1, "accuracy": 1},
    "Wolf Fang Spear": {"attack": 2, "accuracy": 2},
    "Goblin Club": {"attack": 2, "accuracy": 1},
    "Goblin Cleaver": {"attack": 3, "accuracy": 1},
    "Iron Sword": {"attack": 3, "accuracy": 1},
    "Steel Sword": {"attack": 3, "accuracy": 3}
}

armors = {
    "Rags": {"health": 0},
    "Wolf Armor": {"health": 3},
    "White Wolf Armor": {"health": 6},
    "God Armor": {"health": 1000}
}

consumables = {
    "health potion": 2,
    "holywater potion": 1,
}

player_stats = {"health": 90, "max_health": 100}

inventory = {
    "Right Hand": "Wood Sword",
    "Armor": "Rags",
    "coin": 0,
    "consumables": {'health potion': 2, 'holywater potion':2},
    "loot bag": {'God Armor': 1},
}