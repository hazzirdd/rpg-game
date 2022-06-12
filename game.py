import random, json, time


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
            "rare": {
                "Goblin Club": 1,
                "Shiny Necklace": 1
            },
            "legendary": {
                "Goblin Cleaver": 1,
                "Goblin Trophy":1
            },
            "coins":1
    }
  },
    "Wolf": {
        "attack": 2,
        "health": 3,
        "accuracy": 4,
        "drops": {
            "common": {
                "Wolf Skin": 1,
                "Wolf Fang": 1
            },
            "rare": {
                "Wolf Armor": 1,
                "Wolf Fang Spear": 1
            },
            "legendary": {
                "White Wolf Armor": 1,
                "Wolf Trophy": 1
            },
            "coin": 1,
        }
    }
}

weapons = {
    "God Sword": {
        "attack": 200,
        "accuracy":1000
    },
    'Wood Sword': {
        "attack": 1,
        "accuracy": 1
    }
}

consumables = {
    "health potion": 2 
}

player_stats = {
    "health": 10
}

inventory = {
    "Right Hand": "God Sword",
    "coin": 0,
    "consumables": {
        "health potion": 1
    },
}

current_enemy = {}

def create_enemy(foe):
    current_enemy.clear()

    foe_attack = enemies[foe]['attack']
    foe_accuracy = enemies[foe]['attack']
    foe_health = enemies[foe]['health']
    foe_name = foe

    current_enemy['name'] = foe_name
    current_enemy['attack'] = foe_attack
    current_enemy['accuracy'] = foe_accuracy
    current_enemy['health'] = foe_health


def battle(foe):
    move = int(input(f' ---------------\n Your health: {player_stats["health"]}\n---------------\n Attack (1)\n Inventory (2)\n Run Away (3)\n---------------\n'))
    if move == 1:
        attack(foe)
    elif move == 2:
        print('Opening Inventory...')
        time.sleep(1)
        print('---------------')

        for key, val in inventory.items():
            print(key, '-', val)

        inv_choice = int(input(f' ---------------\n Use Potion (1)\n Back (2)\n---------------\n'))
        if inv_choice == 1:
            use_potion = input('What potion do you use?\n')
            player_stats['health'] += consumables[use_potion]
            print(f"{use_potion} consumed! You are now at {player_stats['health']} health points")
            del inventory['consumables'][use_potion]
            battle(foe)
        else:
            battle(foe)


def attack(foe):

    weapon1 = inventory['Right Hand']
    weapon1_attack = weapons[weapon1]['attack']
    weapon1_accuracy = weapons[weapon1]['accuracy']

    foe_name = current_enemy['name']
    foe_attack = enemies[foe]['attack']
    foe_accuracy = enemies[foe]['attack']
    foe_health = enemies[foe]['health']

    player_accuracy_roll = random.randint(0, weapon1_accuracy)
    print(f'{player_accuracy_roll} out of {weapon1_accuracy}')
    foe_accuracy_roll = random.randint(0,foe_accuracy)

    if player_accuracy_roll != 0:
        print(f'The {foe_name} is hit!')
        time.sleep(1)
        current_enemy['health'] -= weapon1_attack
        print(f"The {foe_name}'s health is now {current_enemy['health']}")
        time.sleep(1)

    elif player_accuracy_roll == 0:
        print('You missed!')

    if current_enemy['health'] <= 0:
        print(f'The {foe_name} has been defeated!')
        get_drops(foe)
    else:
        if foe_accuracy_roll != 0:
            player_stats['health'] -= foe_attack
            time.sleep(1)
            print(f"The {foe_name} hit you for {foe_attack} damage")
            time.sleep(1)
            print(f"*You are now at {player_stats['health']} health points")
            battle(foe)
        else:
            time.sleep(1)
            print(f"The {foe_name} missed it's attack!")
            time.sleep(1)
            battle(foe)

def get_drops(foe):
    loot_rarity = random.randint(1,1000)

    if loot_rarity > 0 and loot_rarity < 801:
        loot = random.choice(list(enemies[foe]["drops"]["common"].keys()))
        loot_val = enemies[foe]['drops']['common'][loot]
        print(f"Obtained a common drop!: {loot}")
        if loot in inventory:
            inventory[loot] += 1
        else:
            inventory[loot] = loot_val
        print(inventory)
    
    elif loot_rarity > 800 and loot_rarity < 981:
        loot = random.choice(list(enemies[foe]["drops"]["rare"].keys()))
        print(f"Obtained a rare drop!: {loot}")
    
    else:
        loot = random.choice(list(enemies[foe]["drops"]["legendary"].keys()))
        print(f"Obtained a legendary drop!: {loot}")

def display_inventory():
    weapon1 = inventory['Right Hand']
    print(f"***************\n---INVENTORY---")
    print(f"Right Hand: {weapon1}\n---------------")
    print(f"Consumable Items: ")

    for key, value in inventory['consumables'].items():
        print(f"    {key} : {value}")

    print("***************")



ready_up = input("Ready for battle? [y/n]: ")

if ready_up == 'y':
    foe_list = list(enemies.keys())
    foe = random.choice(foe_list)

    print(f'---------------\n A {foe} has approached!')
    create_enemy(foe)
    battle(foe)
elif ready_up == 'i':
    display_inventory()

