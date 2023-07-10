#***** ADVENT OF CODE 2020 *****
#************ DAY 10 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("10_joltage_input.txt") as input:
    input_data = [int(input.strip("\n")) for input in input.readlines()]

input_data.sort()

# find built-in joltage adapter rating

joltage_diff_1 = 0
joltage_diff_3 = 1

if input_data[0] == 1:
    joltage_diff_1 += 1
if input_data[0] == 3:
    joltage_diff_3 += 1

for i in range(len(input_data)-1):
    if input_data[i+1] - input_data[i] == 1:
        joltage_diff_1 += 1
    elif input_data[i+1] - input_data[i] == 3:
        joltage_diff_3 += 1

print("\nThe number of 1-jolt differences multiplied by the number of 3-jolt differences is:", joltage_diff_1 * joltage_diff_3)

