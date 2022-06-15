import random, json, time, os

import map
import map_gen
import all_enemies

# enemie_dict = {}

# file = open('enemies.json')
# data = json.load(file)

# for i in data['enemies']:
#     enemie_dict[i] = 'test'

# file.close()

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
}

weapons = {
    "God Sword": {"attack": 200, "accuracy": 1000},
    "Wood Sword": {"attack": 1, "accuracy": 1},
    "Wolf Fang Spear": {"attack": 2, "accuracy": 2},
    "Goblin Club": {"attack": 2, "accuracy": 1},
    "Goblin Cleaver": {"attack": 3, "accuracy": 2},
    "Iron Sword": {"attack": 3, "accuracy": 1},
}

armors = {
    "Rags": {"health": 0},
    "Wolf Armor": {"health": 3},
    "White Wolf Armor": {"health": 6},
}

consumables = {"health potion": 2}

player_stats = {"health": 10, "max_health": 10}

inventory = {
    "Right Hand": "Wood Sword",
    "Armor": "Rags",
    "coin": 30,
    "consumables": {'health potion': 1},
    "loot bag": {"Goblin Ear": 1, "Wolf Armor": 1},
}

current_enemy = {}
current_location = {}

x = current_location["x"] = map_gen.x
y = current_location["y"] = map_gen.y


def create_enemy(foe):
    current_enemy.clear()

    foe_attack = enemies[foe].attack
    foe_accuracy = enemies[foe].accuracy
    foe_health = enemies[foe].health
    foe_name = foe

    current_enemy["name"] = foe_name
    current_enemy["attack"] = foe_attack
    current_enemy["accuracy"] = foe_accuracy
    current_enemy["health"] = foe_health


def use_potion():
    use_potion = input("What potion do you use?\n")
    if use_potion in inventory['consumables']:
        if player_stats["health"] + consumables[use_potion] < player_stats["max_health"]:
            player_stats["health"] += consumables[use_potion]
            print(
                f"{use_potion} consumed! You are now at {player_stats['health']} health points"
            )
            time.sleep(1)
            del inventory["consumables"][use_potion]
        else:
            print(f'Cannot exceed max health! {player_stats["health"]}/{player_stats["max_health"]} health points')
            time.sleep(1)
    else:
        print('Potion not found!')
        time.sleep(1)


def battle(foe, x, y):
    move = input(
            f'---------------\n Your health: {player_stats["health"]}\n {foe} health: {current_enemy["health"]}\n---------------\n Attack (1)\n Inventory (2)\n Run Away (3)\n---------------\n'
        )
    
    if move == '1':
        os.system("clear")
        attack(foe, x, y)
    elif move == '2':
        display_inventory(foe, x, y)
    else:
        os.system("clear")
        battle(foe, x, y)


def attack(foe, x, y):

    weapon1 = inventory["Right Hand"]
    weapon1_attack = weapons[weapon1]["attack"]
    weapon1_accuracy = weapons[weapon1]["accuracy"]

    foe_attack = enemies[foe].attack
    foe_accuracy = enemies[foe].accuracy
    foe_health = enemies[foe].health
    foe_name = foe

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
        current_enemy.clear()
        map_gen.ten_by_ten_map[f"x{x}y{y}"] = 'path'
        get_drops(foe)
        time.sleep(3.5)
        map.mapper(x, y)
        move(x, y)
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
        battle(foe, x, y)


def get_drops(foe):
    coin_min = enemies[foe].min_coin
    coin_max = enemies[foe].max_coin
    coins = random.randint(coin_min, coin_max)
    inventory["coin"] += coins

    loot_rarity = random.randint(1, 1000)

    if loot_rarity > 0 and loot_rarity < 801:
        loot = random.choice(enemies[foe].c_drops)
        print(f"------------\nObtained a common drop!: {loot}")
        print(f"*Coins Collected: {coins}\n------------")
        if loot in inventory:
            inventory["loot bag"][loot] += 1
        else:
            inventory["loot bag"][loot] = 1

    elif loot_rarity > 800 and loot_rarity < 981:
        loot = random.choice(enemies[foe].r_drops)
        print(f"------------\nObtained a rare drop!: {loot}")
        print(f"*Coins Collected: {coins}\n------------")
        if loot in inventory:
            inventory["loot bag"][loot] += 1
        else:
            inventory["loot bag"][loot] = 1

    else:
        loot = random.choice(enemies[foe].r_drops)
        print(f"------------\nObtained a legendary drop!: {loot}")
        print(f"*Coins Collected: {coins}\n------------")
        if loot in inventory:
            inventory["loot bag"][loot] += 1
        else:
            inventory["loot bag"][loot] = 1


def display_inventory(foe,x ,y ):
    os.system("clear")

    weapon1 = inventory["Right Hand"]
    armor = inventory["Armor"]
    coins = inventory["coin"]
    print(f"******************\n---INVENTORY---\nHealth: {player_stats['health']}/{player_stats['max_health']}\n---------------")
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
        if current_enemy:
            os.system("clear")
            battle(foe, x, y)
        elif current_location["x"] == 'town_square':
            town_square()
        else:
            os.system("clear")
            move(x, y)

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
            display_inventory(foe, x , y)
        else:
            print("Item not found in player inventory")
            display_inventory(foe, x , y)

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
            player_stats["max_health"] -= armors[armor]['health']
            player_stats["max_health"] += armors[new_armor]['health']
            if player_stats["health"] > player_stats["max_health"]:
                player_stats["health"] = player_stats["max_health"]
            display_inventory(foe, x, y)
        else:
            print("Item not found in player inventory")
            time.sleep(1)
            display_inventory(foe, x, y)

    elif inv_option == 4:
        use_potion()
        os.system("clear")
        display_inventory(foe, x, y)


def initiate_battle(x, y):
    os.system("clear")
    print('...')
    time.sleep(1)
    os.system("clear")
    
    common_enemies = ["Goblin"]
    uncommon_enemies = ["Wolf"]

    rarity = random.randint(1,1000)
    if rarity <= 701:
        foe = random.choice(common_enemies)
    else:
        foe = random.choice(uncommon_enemies)

    # foe_list = list(enemies.keys())
    # foe = random.choice(foe_list)
    print(f"---------------\n A {foe} has appeared!")

    create_enemy(foe)
    battle(foe, x, y)


def move(x, y):

    direction = input("W, A, S, D:\n").lower()
    if direction == "w":
        if map_gen.ten_by_ten_map[f"x{x}y{y + 1}"] == "wall" or map_gen.ten_by_ten_map[f"x{x + 1}y{y}"] == "side_wall":
            print('You hit a wall')
            time.sleep(.5)
            os.system('clear')
            time.sleep(.5)
            map.mapper(x,y)
            move(x, y)
        else:
            y += 1
            time.sleep(.3)
            move_check(x, y, direction)
            # map.mapper(x,y)
            move(x,y)

    elif direction == "s":
        if map_gen.ten_by_ten_map[f"x{x}y{y - 1}"] == "wall" or map_gen.ten_by_ten_map[f"x{x + 1}y{y}"] == "side_wall":
            print('You hit a wall')
            move(x, y)
        else:
            y -= 1
            time.sleep(.3)
            move_check(x, y, direction)
            # map.mapper(x,y)
            move(x,y)

    elif direction == "a":
        if map_gen.ten_by_ten_map[f"x{x - 1}y{y }"] == "wall" or map_gen.ten_by_ten_map[f"x{x + 1}y{y}"] == "side_wall":
            print('You hit a wall')
            move(x, y)
        else:
            x -= 1
            time.sleep(.3)
            move_check(x, y, direction)
            # map.mapper(x,y)
            move(x,y)

    elif direction == "d":
        if map_gen.ten_by_ten_map[f"x{x + 1}y{y}"] == "wall" or map_gen.ten_by_ten_map[f"x{x + 1}y{y}"] == "side_wall":
            print('You hit a wall')
            move(x, y)
        else:
            x += 1
            time.sleep(.3)
            move_check(x, y, direction)
            # map.mapper(x,y)
            move(x,y)

    else:
        print("direction invalid")
        time.sleep(.3)
        os.system("clear")
        move(x, y)

    os.system("clear")

def move_check(x, y, direction):
    
    dict_key = f"x{x}y{y}"

    if map_gen.ten_by_ten_map[dict_key] == "exit":
        confirm = input("Leave the dungeon? [y/n]:  ")
        if confirm == "y":
            os.system("clear")
            print(f"Leaving the dungeon...")
            time.sleep(1)
            town_square()
        else:
            move(map_gen.x, map_gen.y)
    elif map_gen.ten_by_ten_map[dict_key] == "enemy":
        initiate_battle(x, y)
    elif map_gen.ten_by_ten_map[dict_key] == "chest":
        print('You found a chest!')
        time.sleep(2)
        map_gen.ten_by_ten_map[dict_key] == 'path'
    else: 
        pass
    os.system("clear")
    map.mapper(x,y)


def town_square():

    current_location["x"] = 'town_square'

    os.system("clear")
    print("Welcome to the town square, traveler!\n---------------")
    choice = int(input("What would you like to?\n  Enter The Dungeon (1)\n  Inventory(2)\n  Shop(3)\n  Rest(4)\n---------------\n"))

    if choice == 1:
        os.system("clear")
        map.mapper(5,10)
        move(5, 10)
    elif choice == 2:
        display_inventory(None, None, None)
    elif choice == 3:
        shop_chump()
    elif choice == 4:
        player_stats["health"] = player_stats["max_health"]
        os.system("clear")
        print("zzzZZZzzzZZZz...")
        time.sleep(3)
        os.system("clear")
        print("You feel rested and ready!")
        time.sleep(2)
        town_square()
    else:
        town_square()

def shop_chump():
    os.system("clear")
    print("---------------\nOie! Name's Chump, take a look at what we have to offer, lad!\n---------------")
    print('Buy Health Potion --3 coins-- (1)')
    print('Buy Iron Sword -- 10 coins -- (2)')
    print('Sell Items (3)')
    print('Back (4)')
    print(f"---------------\nMy Coins: {inventory['coin']}")
    shop_choice = int(input('---------------\nWhat do ye fancy?\n'))

    if shop_choice == 1:
        if inventory["coin"] >= 3:
            inventory["coin"] -= 3
            print('Thanks a million!')
            if 'health potion' in inventory["consumables"]:
                inventory["consumables"]['health potion'] += 1
            else:
                inventory["consumables"]['health potion'] = 1
            time.sleep(2)
            shop_chump()
        else: 
            print('OIE! You trynna rob me, mate? Come back when you got some coin.')
        
    elif shop_choice == 2:
        if inventory["coin"] >= 10:
            inventory["coin"] -= 10
            print("Tis a shiny beauty she is, careful mate! Here you go!")
            if 'Iron Sword' in inventory:
                inventory["loot bag"]['Iron Sword'] += 1
            else:
                inventory["loot bag"]['Iron Sword'] = 1
            time.sleep(2)
            shop_chump()
        else:
            print('OIE! You trynna rob me, mate? Come back when you got some coin!')
            time.sleep(3)
            shop_chump()
    elif shop_choice == 3:
        os.system("clear")
        if inventory["loot bag"]:

            print('---------------\nLoot Bag:')
            for item in inventory["loot bag"]:
                print(item)
            print('---------------')

            sell_item = input("Ooo nice stuf there lad, what can Chump take off your hands?\n---------------\nSell:  ")
            print('---------------')

            if sell_item in inventory["loot bag"]:
                if sell_item in item_values:
                    sell_confirm = input(f"Oie, I'll buy this {sell_item} off of ye for {item_values[sell_item]} coin, Deal? [y/n]\n")
                    if sell_confirm == 'y':
                        if inventory["loot bag"][sell_item] == 1:
                            del inventory["loot bag"][sell_item]
                        else:
                            inventory["loot bag"][sell_item] -= 1
                        print("Good deal!")
                        inventory["coin"] += item_values[sell_item]
                        time.sleep(2)
                        shop_chump()
                    else:
                        print("Well stop waisting my time then mate!")
                        time.sleep(3)
                        shop_chump()
                else:
                    print(f'Oie sorry mate, Chump cant but this {sell_item}. Very sketchy, it is.')
            else:
                print("What kinda stunty stunt ye tryna pull? A fast one?")
                time.sleep(3)
                shop_chump()
        else:
            print("This a joke mate? You aint got squat in your loot bag!")
            time.sleep(2.5)
            shop_chump()

    elif shop_choice == 4:
        print("Oie! Come again then, mate!")
        time.sleep(2.5)
        town_square()                                
    else:
        print("I'm stright confused mate, what do you want?")
        time.sleep(3)
        town_square()

def main():
    town_square()

begin = input("Begin the Game? [y/n]:  ")
if begin == "y":
    main()
else:
    print('Maybe another time!')

main()
