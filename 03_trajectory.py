#***** ADVENT OF CODE 2020 *****
#************ DAY 3 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("03_trajectory_input.txt") as input:
    input_data = input.readlines()

tree_map = [row.strip()*3 for row in input_data]

for line in tree_map:
    print(line)

