#***** ADVENT OF CODE 2020 *****
#************ DAY 12 ************
#****************** Part 1 *****



# get input data

input_data = None

with open("12_navigation_input.txt") as input:
    input_data = [(instr[0], int(instr[1:].strip("\n"))) for instr in input.readlines()]

# create ship class

class Ship:
    def __init__(self, pos=[0, 0], dir="E"):
        self.pos = pos
        self.dir = dir
    
    def get_dir(self):
        return self.dir
    
    def get_pos(self):
        return self.pos
    
    def change_dir(self, dir):
        self.dir = dir     
    
    def move(self, steps, dir=None):
        if not dir:
            dir = self.dir
        if dir == "E":
            self.pos[1] += steps
        elif dir == "W":
            self.pos[1] -= steps
        elif dir == "S":
            self.pos[0] += steps
        elif dir == "N":
            self.pos[0] -= steps
    
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

# Testing

test_ship = Ship()

for item in input_data:
    process_instruction(test_ship, item)

print("\nThe Manhattan Distance between the ship's current location and the starting location is:", test_ship.get_distance())
print()
