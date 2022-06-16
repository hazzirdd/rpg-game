import random

# Map structure
ten_by_ten_map = {
    "x1y1": "x",
    "x2y1": "x",
    "x3y1": "x",
    "x4y1": "x",
    "x5y1": "x",
    "x6y1": "x",
    "x7y1": "x",
    "x8y1": "x",
    "x9y1": "x",
    "x10y1": "x",
    "x1y2": "x",
    "x2y2": "x",
    "x3y2": "x",
    "x4y2": "x",
    "x5y2": "x",
    "x6y2": "x",
    "x7y2": "x",
    "x8y2": "x",
    "x9y2": "x",
    "x10y2": "x",
    "x1y3": "x",
    "x2y3": "x",
    "x3y3": "x",
    "x4y3": "x",
    "x5y3": "x",
    "x6y3": "x",
    "x7y3": "x",
    "x8y3": "x",
    "x9y3": "x",
    "x10y3": "x",
    "x1y4": "x",
    "x2y4": "x",
    "x3y4": "x",
    "x4y4": "x",
    "x5y4": "x",
    "x6y4": "x",
    "x7y4": "x",
    "x8y4": "x",
    "x9y4": "x",
    "x10y4": "x",
    "x1y5": "x",
    "x2y5": "x",
    "x3y5": "x",
    "x4y5": "x",
    "x5y5": "x",
    "x6y5": "x",
    "x7y5": "x",
    "x8y5": "x",
    "x9y5": "x",
    "x10y5": "x",
    "x1y6": "x",
    "x2y6": "x",
    "x3y6": "x",
    "x4y6": "x",
    "x5y6": "x",
    "x6y6": "x",
    "x7y6": "x",
    "x8y6": "x",
    "x9y6": "x",
    "x10y6": "x",
    "x1y7": "x",
    "x2y7": "x",
    "x3y7": "x",
    "x4y7": "x",
    "x5y7": "x",
    "x6y7": "x",
    "x7y7": "x",
    "x8y7": "x",
    "x9y7": "x",
    "x10y7": "x",
    "x1y8": "x",
    "x2y8": "x",
    "x3y8": "x",
    "x4y8": "x",
    "x5y8": "x",
    "x6y8": "x",
    "x7y8": "x",
    "x8y8": "x",
    "x9y8": "x",
    "x10y8": "x",
    "x1y9": "x",
    "x2y9": "x",
    "x3y9": "x",
    "x4y9": "x",
    "x5y9": "x",
    "x6y9": "x",
    "x7y9": "x",
    "x8y9": "x",
    "x9y9": "x",
    "x10y9": "x",
    "x1y10": "x",
    "x2y10": "x",
    "x3y10": "x",
    "x4y10": "x",
    "x5y10": "x",
    "x6y10": "x",
    "x7y10": "x",
    "x8y10": "x",
    "x9y10": "x",
    "x10y10": "x",
    "x0y1": "side_wall",
    "x0y2": "side_wall",
    "x0y3": "side_wall",
    "x0y4": "side_wall",
    "x0y5": "side_wall",
    "x0y6": "side_wall",
    "x0y7": "side_wall",
    "x0y8": "side_wall",
    "x0y9": "side_wall",
    "x0y10": "side_wall",
    "x1y11": "side_wall",
    "x2y11": "side_wall",
    "x3y11": "side_wall",
    "x4y11": "side_wall",
    "x5y11": "exit",
    "x6y11": "exit",
    "x7y11": "side_wall",
    "x8y11": "side_wall",
    "x9y11": "side_wall",
    "x10y11": "side_wall",
    "x0y11": "side_wall",
    "x1y11": "side_wall",
    "x2y11": "side_wall",
    "x3y11": "side_wall",
    "x4y11": "side_wall",
    "x5y11": "exit",
    "x6y11": "exit",
    "x7y11": "side_wall",
    "x8y11": "side_wall",
    "x9y11": "side_wall",
    "x10y11": "side_wall",
    "x11y1": "side_wall",
    "x11y2": "side_wall",
    "x11y3": "side_wall",
    "x11y4": "side_wall",
    "x11y5": "side_wall",
    "x11y6": "side_wall",
    "x11y7": "side_wall",
    "x11y8": "side_wall",
    "x11y9": "side_wall",
    "x11y10": "side_wall",
    "x1y0": "side_wall",
    "x2y0": "side_wall",
    "x3y0": "side_wall",
    "x4y0": "side_wall",
    "x5y0": "side_wall",
    "x6y0": "side_wall",
    "x7y0": "side_wall",
    "x8y0": "side_wall",
    "x9y0": "side_wall",
    "x10y0": "side_wall",
}

tiles = ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall",
"path", "path", "path", "path", "path", "path", "path", "path", "path",
"enemy", "enemy", "enemy",
"chest"
]


x = 5
y = 10

def create_small_map():
    x = 1
    y = 1

    # Coulumn 1 of 10
    count = 0
    while count <= 10:
        tile = random.choice(tiles)
        current_tile = f"x{x}y{y}"

        if current_tile in ten_by_ten_map:
            ten_by_ten_map[current_tile] = tile
            x += 1
            count += 1
        else:
            y = 2
            x = 1
            count = 10
            # print(f'Column {y - 1} complete. Moving on to column {y}')
        
    # Coulumn 2 of 10
    count = 0
    while count <= 10:
        tile = random.choice(tiles)
        current_tile = f"x{x}y{y}"

        if current_tile in ten_by_ten_map:
            ten_by_ten_map[current_tile] = tile
            x += 1
            count += 1
        else:
            y = 3
            x = 1
            count = 10
            # print(f'Column {y - 1} complete. Moving on to column {y}')

    # Coulumn 3 of 10
    count = 0
    while count <= 10:
        tile = random.choice(tiles)
        current_tile = f"x{x}y{y}"

        if current_tile in ten_by_ten_map:
            ten_by_ten_map[current_tile] = tile
            x += 1
            count += 1
        else:
            y = 4
            x = 1
            count = 10
            # print(f'Column {y - 1} complete. Moving on to column {y}')

    # Coulumn 4 of 10
    count = 0
    while count <= 10:
        tile = random.choice(tiles)
        current_tile = f"x{x}y{y}"

        if current_tile in ten_by_ten_map:
            ten_by_ten_map[current_tile] = tile
            x += 1
            count += 1
        else:
            y = 5
            x = 1
            count = 10
            # print(f'Column {y - 1} complete. Moving on to column {y}')

    # Coulumn 5 of 10
    count = 0
    while count <= 10:
        tile = random.choice(tiles)
        current_tile = f"x{x}y{y}"

        if current_tile in ten_by_ten_map:
            ten_by_ten_map[current_tile] = tile
            x += 1
            count += 1
        else:
            y = 6
            x = 1
            count = 10
            # print(f'Column {y - 1} complete. Moving on to column {y}')

        # Coulumn 6 of 10
    count = 0
    while count <= 10:
        tile = random.choice(tiles)
        current_tile = f"x{x}y{y}"

        if current_tile in ten_by_ten_map:
            ten_by_ten_map[current_tile] = tile
            x += 1
            count += 1
        else:
            y = 7
            x = 1
            count = 10
            # print(f'Column {y - 1} complete. Moving on to column {y}')

    # Coulumn 7 of 10
    count = 0
    while count <= 10:
        tile = random.choice(tiles)
        current_tile = f"x{x}y{y}"

        if current_tile in ten_by_ten_map:
            ten_by_ten_map[current_tile] = tile
            x += 1
            count += 1
        else:
            y = 8
            x = 1
            count = 10
            # print(f'Column {y - 1} complete. Moving on to column {y}')

# Coulumn 8 of 10
    count = 0
    while count <= 10:
        tile = random.choice(tiles)
        current_tile = f"x{x}y{y}"

        if current_tile in ten_by_ten_map:
            ten_by_ten_map[current_tile] = tile
            x += 1
            count += 1
        else:
            y = 9
            x = 1
            count = 10
            # print(f'Column {y - 1} complete. Moving on to column {y}')

    # Row 9 of 10
    count = 0
    while count <= 10:
        tile = random.choice(tiles)
        current_tile = f"x{x}y{y}"

        if current_tile in ten_by_ten_map:
            ten_by_ten_map[current_tile] = tile
            x += 1
            count += 1
        else:
            y = 10
            x = 1
            count = 10
            # print(f'Column {y - 1} complete. Moving on to column {y}')

    # Row 10 of 10
    count = 0
    while count <= 10:
        tile = random.choice(tiles)
        current_tile = f"x{x}y{y}"

        if current_tile in ten_by_ten_map:
            ten_by_ten_map[current_tile] = tile
            x += 1
            count += 1
        else:
            y = 10
            x = 1
            count = 10
            # print(f'Column {y - 1} complete.')

    ten_by_ten_map["x5y10"] = "path"
    ten_by_ten_map["x6y10"] = "path"
    ten_by_ten_map["x5y9"] = "path"
    ten_by_ten_map["x6y9"] = "path"
    ten_by_ten_map["x5y8"] = "path"
    ten_by_ten_map["x6y8"] = "path"

    ten_by_ten_map["x10y2"] = "wall"
    
    ten_by_ten_map["x11y1"] = "side_wall"
    ten_by_ten_map["x11y2"] = "side_wall"
    ten_by_ten_map["x11y3"] = "side_wall"
    ten_by_ten_map["x11y4"] = "side_wall"
    ten_by_ten_map["x11y5"] = "side_wall"
    ten_by_ten_map["x11y6"] = "side_wall"
    ten_by_ten_map["x11y7"] = "side_wall"
    ten_by_ten_map["x11y8"] = "side_wall"
    ten_by_ten_map["x11y9"] = "side_wall"
    ten_by_ten_map["x11y10"] = "side_wall"

    # print_map()

def print_map():
    for key, val in ten_by_ten_map.items():
        print(f'{key} is a {val}!')

create_small_map()