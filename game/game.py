import random, json, time, os


# enemie_dict = {}

# file = open('enemies.json')
# data = json.load(file)

# for i in data['enemies']:
#     enemie_dict[i] = 'test'

# file.close()

enemies = {
    "Goblin": {
        "attack": 1,
        "health": 1,
        "accuracy": 5,
        "drops": {
            "common": {
                "Goblin Ear": 1,
            },
            "rare": {"Goblin Club": 1, "Shiny Necklace": 1},
            "legendary": {"Goblin Cleaver": 1, "Goblin Trophy": 1},
            "coin min": 0,
            "coin max": 2,
        },
    },
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

weapons = {
    "God Sword": {"attack": 200, "accuracy": 1000},
    "Wood Sword": {"attack": 1, "accuracy": 1},
    "Wolf Fang Spear": {"attack": 2, "accuracy": 2},
    "Goblin Club": {"attack": 2, "accuracy": 1},
    "Goblin Cleaver": {"attack": 3, "accuracy": 1},
}

armors = {
    "Rags": {"health": 0},
    "Wolf Armor": {"health": 3},
    "White Wolf Armor": {"health": 6},
}

consumables = {"health potion": 2}

player_stats = {"health": 10, "max_health": 10}

inventory = {
    "Right Hand": "God Sword",
    "Armor": "Rags",
    "coin": 0,
    "consumables": {"health potion": 1},
    "loot bag": {"God Sword": 1, "Wolf Armor": 1},
}

current_enemy = {}


def create_enemy(foe):
    current_enemy.clear()

    foe_attack = enemies[foe]["attack"]
    foe_accuracy = enemies[foe]["attack"]
    foe_health = enemies[foe]["health"]
    foe_name = foe

    current_enemy["name"] = foe_name
    current_enemy["attack"] = foe_attack
    current_enemy["accuracy"] = foe_accuracy
    current_enemy["health"] = foe_health


def use_potion():
    use_potion = input("What potion do you use?\n")
    player_stats["health"] += consumables[use_potion]
    print(
        f"{use_potion} consumed! You are now at {player_stats['health']} health points"
    )
    del inventory["consumables"][use_potion]


def battle(foe):
    move = int(
        input(
            f'---------------\n Your health: {player_stats["health"]}\n {foe} health: {current_enemy["health"]}\n---------------\n Attack (1)\n Inventory (2)\n Run Away (3)\n---------------\n'
        )
    )
    if move == 1:
        os.system("clear")
        attack(foe)
    elif move == 2:
        os.system("clear")
        print("Opening Inventory...")
        time.sleep(1)
        print("---------------")

        for key, val in inventory.items():
            print(key, "-", val)

        inv_choice = int(
            input(f" ---------------\n Use Potion (1)\n Back (2)\n---------------\n")
        )
        if inv_choice == 1:
            use_potion()
            battle(foe)
        else:
            os.system("clear")
            battle(foe)


def attack(foe):

    weapon1 = inventory["Right Hand"]
    weapon1_attack = weapons[weapon1]["attack"]
    weapon1_accuracy = weapons[weapon1]["accuracy"]

    foe_name = current_enemy["name"]
    foe_attack = enemies[foe]["attack"]
    foe_accuracy = enemies[foe]["attack"]
    foe_health = enemies[foe]["health"]

    player_accuracy_roll = random.randint(0, weapon1_accuracy)
    print(f"{player_accuracy_roll} out of {weapon1_accuracy}")
    foe_accuracy_roll = random.randint(0, foe_accuracy)

    if player_accuracy_roll != 0:
        print(f"The {foe_name} is hit!")
        time.sleep(1)
        current_enemy["health"] -= weapon1_attack
        print(f"The {foe_name}'s health is now {current_enemy['health']}")
        time.sleep(1)

    elif player_accuracy_roll == 0:
        print("You missed!")

    if current_enemy["health"] <= 0:
        print(f"The {foe_name} has been defeated!")
        get_drops(foe)
        start()
    else:
        if foe_accuracy_roll != 0:
            player_stats["health"] -= foe_attack
            time.sleep(1)
            print(f"The {foe_name} hit you for {foe_attack} damage")
            time.sleep(1)
            print(f"*You are now at {player_stats['health']} health points")
            time.sleep(1)
        else:
            time.sleep(1)
            print(f"The {foe_name} missed it's attack!")
            time.sleep(1)

    if player_stats["health"] <= 0:
        print("Your health has hit zero!")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("GAME OVER!")
    else:
        battle(foe)


def get_drops(foe):
    coin_min = enemies[foe]["drops"]["coin min"]
    coin_max = enemies[foe]["drops"]["coin max"]
    coins = random.randint(coin_min, coin_max)
    inventory["coin"] += coins

    loot_rarity = random.randint(1, 1000)

    if loot_rarity > 0 and loot_rarity < 801:
        loot = random.choice(list(enemies[foe]["drops"]["common"].keys()))
        loot_val = enemies[foe]["drops"]["common"][loot]
        print(f"------------\nObtained a common drop!: {loot}")
        print(f"*Coins Collected: {coins}\n------------")
        if loot in inventory:
            inventory["loot bag"][loot] += 1
        else:
            inventory["loot bag"][loot] = loot_val

    elif loot_rarity > 800 and loot_rarity < 981:
        loot = random.choice(list(enemies[foe]["drops"]["rare"].keys()))
        loot_val = enemies[foe]["drops"]["rare"][loot]
        print(f"------------\nObtained a rare drop!: {loot}")
        if loot in inventory:
            inventory["loot bag"][loot] += 1
        else:
            inventory["loot bag"][loot] = loot_val

    else:
        loot = random.choice(list(enemies[foe]["drops"]["legendary"].keys()))
        loot_val = enemies[foe]["drops"]["legendary"][loot]
        print(f"------------\nObtained a legendary drop!: {loot}")
        if loot in inventory:
            inventory["loot bag"][loot] += 1
        else:
            inventory["loot bag"][loot] = loot_val


def display_inventory():
    os.system("clear")

    weapon1 = inventory["Right Hand"]
    armor = inventory["Armor"]
    coins = inventory["coin"]
    print(f"******************\n---INVENTORY---")
    print(f"Right Hand: {weapon1}\nArmor:  {armor}\nCoins: {coins}\n---------------")
    print(f"Consumable Items: ")

    for key, value in inventory["consumables"].items():
        print(f"    {key} : {value}")

    print("Loot Bag: ")

    for key, value in inventory["loot bag"].items():
        print(f"    {key} : {value}")

    print("******************")

    inv_option = int(
        input(
            f"Options:\n  Back(1)\n  Change Right Hand(2)\n  Change Armor(3)\n  Use Potion(4)\n"
        )
    )

    if inv_option == 1:
        os.system("clear")
        start()

    elif inv_option == 2:
        new_right_hand = input(f"Change {weapon1} to:  ")
        if new_right_hand in inventory["loot bag"]:
            if weapon1 in inventory["loot bag"]:
                inventory["loot bag"][weapon1] += 1
                del inventory["loot bag"][new_right_hand]
            else:
                inventory["loot bag"][weapon1] = 1
                del inventory["loot bag"][new_right_hand]
            inventory["Right Hand"] = new_right_hand
            display_inventory()
        else:
            print("Item not found in player inventory")
            display_inventory()

    elif inv_option == 3:
        new_armor = input(f"Change {armor} to:  ")
        if new_armor in inventory["loot bag"]:
            if armor in inventory["loot bag"]:
                inventory["loot bag"][armor] += 1
                del inventory["loot bag"][new_armor]
            else:
                inventory["loot bag"][armor] = 1
                del inventory["loot bag"][new_armor]
            inventory["Armor"] = new_armor
            display_inventory()
        else:
            print("Item not found in player inventory")
            time.sleep(1)
            display_inventory()

    elif inv_option == 4:
        use_potion()
        os.system("clear")
        start()


def start():
    ready_up = input("Battle (1)\nCheck Inventory (2)\n")

    if ready_up == "1":
        os.system("clear")

        foe_list = list(enemies.keys())
        foe = random.choice(foe_list)

        print(f"---------------\n A {foe} has approached!")
        create_enemy(foe)
        battle(foe)
    elif ready_up == "2":
        display_inventory()


def main():
    start()


main()
