#***** ADVENT OF CODE 2020 *****
#************ DAY 17 ************
#****************** Part 1 *****

from itertools import permutations

# get input data

input_data = None

with open("17_cubes_input.txt") as input:
    input_data = [[cube for cube in row.strip("\n")] for row in input.readlines()]

# create cube class with states active and inactive

class Cube:
    def __init__(self, coords, active=False):
        self.coords = coords
        self.active = active
        z = coords[0]
        y = coords[1]
        x = coords[2]
        self.neighbors = [
            (z,y,x+1), (z,y,x-1), (z,y+1,x), (z,y+1,x+1), (z,y+1,x-1), (z,y-1,x), 
            (z,y-1,x+1), (z,y-1,x-1), (z+1,y,x), (z+1,y,x+1), (z+1,y,x-1),(z+1,y+1,x), 
            (z+1,y+1,x+1), (z+1,y+1,x-1), (z+1,y-1,x), (z+1,y-1,x+1), (z+1,y-1,x-1), (z-1,y,x), 
            (z-1,y,x+1), (z-1,y,x-1),(z-1,y+1,x), (z-1,y+1,x+1), (z-1,y+1,x-1), (z-1,y-1,x), 
            (z-1,y-1,x+1), (z-1,y-1,x-1)
            ]
    
    def __repr__(self):
        return "c"
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def toggle_state(self):
        if self.active:
            self.deactivate()
        else:
            self.activate()
    
    def display(self):
        if self.active:
            return "#"
        return "."
    
    def is_neighbor(self, cube_coords):
        for i in range(3):
            if self.coords[i] - cube_coords[i] not in [1, 0, -1]:
                return False
        return True

# create 3-dimensional matrix that holds active and inactive cubes

pocket_dimension = [[[Cube((z,y,x)) for x in range(50)] for y in range(50)] for z in range(3)]

# change cubes state to active where appropriate according to input data

for y in range(len(input_data)):
    for x in range(len(input_data[0])):
        if input_data[y][x] == "#":
            pocket_dimension[1][y+20][x+20].activate()

# create function to emulate changes

def count_active_neighbors(grid, cube):
    count = 0
    for neighbor in cube.neighbors:
        print(list(neighbor))
            # count += 1
    return count

def simulation(grid):
    to_be_toggled = list()
    for plane in grid:
        for row in plane:
            for cube in row:
                if not cube.active and count_active_neighbors(grid, cube) == 3:
                    to_be_toggled.append(cube)
                else:
                    if count_active_neighbors(grid, cube) not in [2, 3]:
                        to_be_toggled.append(cube)
    for item in to_be_toggled:
        item.toggle_state()

# display grid

def display_grid(grid):
    print()
    for row in grid:
        for cube in row:
            if cube.active:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# count active cubes

def count_active_cubes(matrix):
    count = 0
    for plane in matrix:
        for row in plane:
            for cube in row:
                if cube.active:
                    count += 1
    return count

# Testing

for plane in pocket_dimension:
    display_grid(plane)

print(count_active_cubes(pocket_dimension))

simulation(pocket_dimension)

for plane in pocket_dimension:
    display_grid(plane)

print(count_active_cubes(pocket_dimension))

# test_cube = Cube((10,15,20))
# print(test_cube)
# for neighbor in test_cube.neighbors:
#     print(neighbor)

# print(len(test_cube.neighbors), "-->", len(set(test_cube.neighbors)))