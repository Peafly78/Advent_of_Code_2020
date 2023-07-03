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

print("\n Number of trees encountered on trajectory:", trees_encountered)