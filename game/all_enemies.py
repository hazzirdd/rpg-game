class Enemy:
    def __init__(self, name, attack, accuracy ,health, c_drops, r_drops, l_drops, min_coin, max_coin):
        self.name = name
        self.attack = attack
        self.accuracy = accuracy
        self.health = health
        self.c_drops = c_drops
        self.r_drops = r_drops
        self.l_drops = l_drops
        self.min_coin = min_coin
        self.max_coin = max_coin

class MagicEnemy(Enemy):

    def __init__(self, name, attack, accuracy, health, c_drops, r_drops, l_drops, min_coin, max_coin, magic): #ALL
        self.magic = magic # DEFINE NEW
        super().__init__(name, attack, accuracy, health, c_drops, r_drops, l_drops, min_coin, max_coin) #SUPER(OLD)


    def print_magic(self):
        print(self.magic)

goblin = Enemy('Goblin', 1, 2, 2, ['Goblin Ear'], ['Goblin Club, Shiny Necklace'], ['Goblin Cleaver', 'Goblin Trophy'], 0, 2 )
wolf = Enemy('Wolf', 2, 5, 3, ['Wolf Hide', 'Wolf Fang'], ['Wolf Armor', 'Wolf Fang Spear'], ['Whire Wolf Armor', 'Wolf Trophy'], 0, 3)

fire_myte = MagicEnemy('Fire Myte', 2, 5, 5, ['Fire Spirit'], ['Fire Core'], ['Fist of Fire'], 2, 4, 'Fire')

