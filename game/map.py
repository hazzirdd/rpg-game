# import os
# import time

# import game

import telnetlib
import map_gen

class Map:
    def __init__(self, name, max_x, min_x, max_y, min_y):
        self.name = name
        self.max_x = max_x
        self.min_x = min_x
        self.max_y = max_y
        self.min_y = min_y

    def __repr__(self, max_x, max_y):
        return f"{self.name} is a {max_x} x {max_y} size map"
    
dungeon = {
    "x1y1": "wall",
    "x2y1": "wall",
    "x3y1": "wall",
    "x4y1": "wall",
    "x5y1": "wall",
    "x6y1": "wall",
    "x7y1": "wall",
    "x8y1": "wall",
    "x9y1": "wall",
    "x10y1": "wall",
    "x1y2": "wall",
    "x2y2": "path",
    "x3y2": "enemy",
    "x4y2": "path",
    "x5y2": "path",
    "x6y2": "path",
    "x7y2": "path",
    "x8y2": "enemy",
    "x9y2": "path",
    "x10y2": "wall",
    "x1y3": "wall",
    "x2y3": "path",
    "x3y3": "enemy",
    "x4y3": "path",
    "x5y3": "path",
    "x6y3": "path",
    "x7y3": "path",
    "x8y3": "path",
    "x9y3": "path",
    "x10y3": "wall",
    "x1y4": "wall",
    "x2y4": "wall",
    "x3y4": "wall",
    "x4y4": "wall",
    "x5y4": "wall",
    "x6y4": "wall",
    "x7y4": "wall",
    "x8y4": "path",
    "x9y4": "path",
    "x10y4": "wall",
    "x1y5": "path",
    "x2y5": "path",
    "x3y5": "path",
    "x4y5": "path",
    "x5y5": "path",
    "x6y5": "path",
    "x7y5": "path",
    "x8y5": "enemy",
    "x9y5": "path",
    "x10y5": "wall",
    "x1y6": "path",
    "x2y6": "path",
    "x3y6": "path",
    "x4y6": "path",
    "x5y6": "enemy",
    "x6y6": "path",
    "x7y6": "path",
    "x8y6": "path",
    "x9y6": "path",
    "x10y6": "wall",
    "x1y7": "wall",
    "x2y7": "wall",
    "x3y7": "wall",
    "x4y7": "wall",
    "x5y7": "wall",
    "x6y7": "path",
    "x7y7": "path",
    "x8y7": "path",
    "x9y7": "enemy",
    "x10y7": "wall",
    "x1y8": "wall",
    "x2y8": "path",
    "x3y8": "path",
    "x4y8": "path",
    "x5y8": "path",
    "x6y8": "path",
    "x7y8": "enemy",
    "x8y8": "path",
    "x9y8": "path",
    "x10y8": "wall",
    "x1y9": "wall",
    "x2y9": "path",
    "x3y9": "enemy",
    "x4y9": "path",
    "x5y9": "path",
    "x6y9": "path",
    "x7y9": "path",
    "x8y9": "path",
    "x9y9": "path",
    "x10y9": "wall",
    "x1y10": "wall",
    "x2y10": "wall",
    "x3y10": "wall",
    "x4y10": "wall",
    "x5y10": "wall",
    "x6y10": "wall",
    "x7y10": "wall",
    "x8y10": "wall",
    "x9y10": "wall",
    "x10y10": "wall",
    "x0y5": "exit",
    "x0y6": "exit"
}


# map1 = Map("Baby's Dungeon", 10, 10, 10, 10)

x = 1
y = 6

# def move(x, y):
#     os.system("clear")
#     print(f"{x}:{y}")
#     direction = input("W, A, S, D\n").lower()
#     if direction == "w":
#         y += 1
#         move_check(x, y, direction)
#     elif direction == "s":
#         y -= 1
#         move_check(x, y, direction)
#     elif direction == "a":
#         x -= 1
#         move_check(x, y, direction)
#     elif direction == "d":
#         x += 1
#         move_check(x, y, direction)
#     else:
#         print("direction invalid")


# def move_check(x, y, direction):
    
#     dict_key = f"x{x}y{y}"
    
#     if dungeon[dict_key] == "wall":
#         print(f"{dict_key} is a wall!")
#         if direction == "w":
#             y -= 1
#         elif direction == "s":
#             y += 1
#         elif direction == 'a':
#             x += 1
#         else:
#             x -= 1
#         time.sleep(.5)
#         move(x, y)
#     elif dungeon[dict_key] == "exit":
#         print(f"You have left the dungeon!")
#     elif dungeon[dict_key] == "enemy":
#         game.start()
#     else: 
#         move(x, y)


# move(x, y)

positions = {
    "x1y1": 261,
    "x2y1": 263,
    "x3y1": 265,
    "x4y1": 267,
    "x5y1": 269,
    "x6y1": 271,
    "x7y1": 273,
    "x8y1": 275,
    "x9y1": 277,
    "x10y1": 279,
    "x1y2": 233,
    "x2y2": 235,
    "x3y2": 237,
    "x4y2": 239,
    "x5y2": 241,
    "x6y2": 243,
    "x7y2": 245,
    "x8y2": 247,
    "x9y2": 249,
    "x10y2": 251,
    "x1y3": 205,
    "x2y3": 207,
    "x3y3": 209,
    "x4y3": 211,
    "x5y3": 213,
    "x6y3": 215,
    "x7y3": 217,
    "x8y3": 219,
    "x9y3": 221,
    "x10y3": 223,
    "x1y4": 177,
    "x2y4": 179,
    "x3y4": 181,
    "x4y4": 183,
    "x5y4": 185,
    "x6y4": 187,
    "x7y4": 189,
    "x8y4": 191,
    "x9y4": 193,
    "x10y4": 195,
    "x1y5": 149,
    "x2y5": 151,
    "x3y5": 153,
    "x4y5": 155,
    "x5y5": 157,
    "x6y5": 159,
    "x7y5": 161,
    "x8y5": 163,
    "x9y5": 165,
    "x10y5": 167,
    "x1y6": 121,
    "x2y6": 123,
    "x3y6": 125,
    "x4y6": 127,
    "x5y6": 129,
    "x6y6": 131,
    "x7y6": 133,
    "x8y6": 135,
    "x9y6": 137,
    "x10y6": 139,
    "x1y7": 93,
    "x2y7": 95,
    "x3y7": 97,
    "x4y7": 99,
    "x5y7": 101,
    "x6y7": 103,
    "x7y7": 105,
    "x8y7": 107,
    "x9y7": 109,
    "x10y7": 111,
    "x1y8": 65,
    "x2y8": 67,
    "x3y8": 69,
    "x4y8": 71,
    "x5y8": 73,
    "x6y8": 75,
    "x7y8": 77,
    "x8y8": 79,
    "x9y8": 81,
    "x10y8": 83,
    "x1y9": 37,
    "x2y9": 39,
    "x3y9": 41,
    "x4y9": 43,
    "x5y9": 45,
    "x6y9": 47,
    "x7y9": 49,
    "x8y9": 51,
    "x9y9": 53,
    "x10y9": 55,
    "x1y10": 9,
    "x2y10": 11,
    "x3y10": 13,
    "x4y10": 15,
    "x5y10": 17,
    "x6y10": 19,
    "x7y10": 21,
    "x8y10": 23,
    "x9y10": 25,
    "x10y10": 27,
    # "x0y1": 0,
    # "x0y2": 0,
    # "x0y3": 0,
    # "x0y4": 0,
    # "x0y5": 0,
    # "x0y6": 0,
    # "x0y7": 0,
    # "x0y8": 0,
    # "x0y9": 0,
    # "x1y11": 0,
    # "x2y11": 0,
    # "x3y11": 0,
    # "x4y11": 0,
    # "x5y11": 0,
    # "x6y11": 0,
    # "x7y11": 0,
    # "x0y11": 0,
    # "x8y11": 0,
    # "x9y11": 0,
    # "x10y11": 0,
    # "x11y1": 0,
    # "x11y2": 0,
    # "x11y3": 0,
    # "x11y4": 0,
    # "x11y5": 0,
    # "x11y6": 0,
    # "x11y7": 0,
    # "x11y8": 0,
    # "x11y9": 0,
    # "x11y10":0,
    # "x1y0": 0,
    # "x3y0": 0,
    # "x4y0": 0,
    # "x5y0": 0,
    # "x6y0": 0,
    # "x7y0": 0,
    # "x8y0": 0,
    # "x9y0": 0,
    # "x2y0": 0,
    # "x10y0": 0,
}

def mapper(x, y):
    
    quardinants = f"x{x}y{y}"
    current_position = positions[quardinants]

    if current_position == "x5y11":
        map = '''
            ■ ■ ■ ■ ▣ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            '''
    elif current_position == "x6y11":
        map = '''
            ■ ■ ■ ■ ■ ▣ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            '''
    else:
        map = '''
        ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            '''

        position_marker = "▣"
        wall_marker = "▤"
        
        temp = list(map)
        temp[current_position] = position_marker
        map = "".join(temp)

        map_wall = map_gen.ten_by_ten_map.keys()

        walls = [key for key, val in map_gen.ten_by_ten_map.items() if val == "wall"]

        for quardinant in walls:
            position = positions[quardinant]
            print(f"{quardinant} : {position}")
            temp[position] = wall_marker
            map = "".join(temp)


    print(map)