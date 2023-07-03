#***** ADVENT OF CODE 2020 *****
#************ DAY 3 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("03_trajectory_input.txt") as input:
    input_data = input.readlines()

tree_map = [row.strip()*100 for row in input_data]

# calculate trees encountered on trajectory

trees_encountered = 0

current_row = 0
current_col = 0

for i in range(len(tree_map)-1):
    current_row += 1
    current_col += 3
    if tree_map[current_row][current_col] == "#":
        trees_encountered += 1

print("\nNumber of trees encountered on trajectory:", trees_encountered)



#****************** Part 1 *****


#create function to calculate trees encountered

def locate_trees(map, right_plus, down_plus):
    trees_encountered = 0
    current_row = 0
    current_col = 0
    for i in range(len(map)//down_plus-1):
        current_row += down_plus
        current_col += right_plus
        if map[current_row][current_col] == "#":
            trees_encountered += 1
    return trees_encountered

trees_multiplied = 1

instructions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for instruction in instructions:
    trees_encountered = locate_trees(tree_map, instruction[0], instruction[1])
    trees_multiplied *= trees_encountered

print("\nYou encounter a whole lot of trees, namely:", trees_multiplied)
