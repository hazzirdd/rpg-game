class Map:
    def __init__(self, name, max_x, min_x, max_y, min_y):
        self.name = name
        self.max_x = max_x
        self.min_x = min_x
        self.max_y = max_y
        self.min_y = min_y

    def __repr__(self, max_x, max_y):
        return f"{self.name} is a {max_x} x {max_y} size map"


map1 = Map("Baby's Dungeon", 10, 10, 10, 10)

x = 1
y = 6

direction = input("W, A, S, D").lower()
if direction == "w":
    x += 1
elif direction == "s":
    x -= 1
elif direction == "a":
    y -= 1
elif direction == "d":
    y += 1
else:
    print("direction invalid")
