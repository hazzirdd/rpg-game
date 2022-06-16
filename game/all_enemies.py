import random
import time

class Enemy:
    def __init__(self, name, attack, accuracy ,health, c_drops, r_drops, l_drops, min_coin, max_coin, is_magical):
        self.name = name
        self.attack = attack
        self.accuracy = accuracy
        self.health = health
        self.c_drops = c_drops
        self.r_drops = r_drops
        self.l_drops = l_drops
        self.min_coin = min_coin
        self.max_coin = max_coin
        self.is_magical = is_magical

class MagicEnemy(Enemy):

    def __init__(self, name, attack, accuracy, health, c_drops, r_drops, l_drops, min_coin, max_coin, is_magical, magic): #ALL
        self.magic = magic # DEFINE NEW
        super().__init__(name, attack, accuracy, health, c_drops, r_drops, l_drops, min_coin, max_coin, is_magical) #SUPER(OLD)


    def print_magic(self):
        print(self.magic)

    def fire_attack():
        attack_type = random.randint(1,10)
        if attack_type < 3:
            fire_damage = False
            # print(f"Fire not inflicted. Fire Damage: {fire_damage}")
            time.sleep(.5)
        else:
            fire_damage = True
            print(f"Enemy inflicted you with fire!")
            time.sleep(2)
        
        return fire_damage
            

# Standard
goblin = Enemy('Goblin', 1, 2, 2, ['Goblin Ear'], ['Goblin Club', 'Shiny Necklace'], ['Goblin Cleaver', 'Goblin Trophy'], 0, 2, False )
wolf = Enemy('Wolf', 2, 4, 3, ['Wolf Hide', 'Wolf Fang'], ['Wolf Armor', 'Wolf Fang Spear'], ['Whire Wolf Armor', 'Wolf Trophy'], 0, 3, False)

# Magic
fire_myte = MagicEnemy('Fire Myte', 1, 2, 5, ['Fire Spirit'], ['Fire Core'], ['Fist of Fire'], 2, 4, True, 'Fire')

