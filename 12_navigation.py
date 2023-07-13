#***** ADVENT OF CODE 2020 *****
#************ DAY 12 ************
#****************** Part 1 *****



# get input data

input_data = None

with open("12_navigation_input.txt") as input:
    input_data = [(instr[0], int(instr[1:].strip("\n"))) for instr in input.readlines()]

# create ship class

class Ship:
    def __init__(self, pos=(0, 0), dir="E"):
        self.pos = pos
        self.dir = dir
    
    def get_dir(self):
        return self.dir
    
    def get_pos(self):
        return self.pos
    
    def change_dir(self, dir):
        self.dir = dir

    def change_pos(self, pos):
        self.pos = pos   
    
    def move(self, steps, dir=None, start=None):
        if not dir:
            dir = self.dir
        if not start:
            start = list(self.pos)
        if dir == "E":
            start[1] += steps
        elif dir == "W":
            start[1] -= steps
        elif dir == "S":
            start[0] += steps
        elif dir == "N":
            start[0] -= steps
        self.change_pos(tuple(start))
    
    def get_distance(self):
        return abs(self.pos[0] + self.pos[1])

# create function to turn ship according to instructions 

turning_directions = {
    "E": {"R": {90: "S", 180: "W", 270: "N", 360: "E"},
          "L": {90: "N", 180: "W", 270: "S", 360: "E"}},
    "S": {"R": {90: "W", 180: "N", 270: "E", 360: "S"},
          "L": {90: "E", 180: "N", 270: "W", 360: "S"}},
    "W": {"R": {90: "N", 180: "E", 270: "S", 360: "W"},
          "L": {90: "S", 180: "E", 270: "N", 360: "W"}},
    "N": {"R": {90: "E", 180: "S", 270: "W", 360: "N"},
          "L": {90: "W", 180: "S", 270: "E", 360: "N"}}
}

def turn_ship(ship, leftright, deg):
    ship.change_dir(turning_directions[ship.get_dir()][leftright][deg])

# create function to process instructions

def process_instruction(ship, instruction):
    command = instruction[0]
    how_far = instruction[1]
    if command == "F":
        ship.move(how_far)
    elif command in "ESWN":
        ship.move(how_far, command)
    elif command in "LR":
        turn_ship(ship, command, how_far)
    else:
        print("invalid instruction")

# calculate Manhattan Distance between current position and start position

# test_ship = Ship()

# for item in input_data:
#     process_instruction(test_ship, item)

# print("\nThe Manhattan Distance between the ship's current location and the starting location is:", test_ship.get_distance())
# print()

#****************** Part 2 *****



# create functions to rotate waypoint

def bind_wp_to_ship(pos_ship, wp, dir, distance): 
    wp.change_pos(pos_ship)
    print("binding:", wp.get_pos())
    wp.move(distance[0], dir[0])
    print("binding:", wp.get_pos())
    wp.move(distance[1], dir[1])
    print("binding:", wp.get_pos())
    print("ship stays at:", pos_ship)

def find_dir_wp(pos_ship, wp):
    dir_0 = None
    dir_1 = None
    if pos_ship[0] < wp.pos[0]:
        dir_0 = "S"
    else:
        dir_0 = "N"
    if pos_ship[1] < wp.pos[1]:
        dir_1 = "E"
    else:
        dir_1 = "W"
    print("The waypoint lies:", [dir_0, dir_1])
    return [dir_0, dir_1]


def rotate_waypoint(pos_ship, wp, leftright, deg, distance): # continue here -- unfinished
    loc_wp = find_dir_wp(pos_ship, wp)
    dir = [turning_directions[loc_wp[0]][leftright][deg], turning_directions[loc_wp[1]][leftright][deg]]
    print("New direction:", dir)
    bind_wp_to_ship(pos_ship, wp, dir, distance)

# create function to process instructions according to new rules

#continue here    

# Testing

print()
flag_ship = Ship()
print(flag_ship.get_pos())
print(flag_ship.get_dir())

waypoint = Ship((10, 20))
print(waypoint.get_pos())
print(waypoint.get_dir())

flag_ship.change_pos((2, 2))
bind_wp_to_ship(flag_ship.get_pos(), waypoint, ["S", "E"], [1, 2])
print(flag_ship.get_pos())
print(waypoint.get_pos())

rotate_waypoint(flag_ship.get_pos(), waypoint, "R", 90, [1, 2])

print(flag_ship.get_pos())
print(waypoint.get_pos())

