#***** ADVENT OF CODE 2020 *****
#************ DAY 4 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("04_passports_input.txt") as input:
    input_data = input.read().split("\n\n")


valid = [True for passport in range(len(input_data))]

for i in range(len(input_data)):
    for item in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if item not in input_data[i]:
            valid[i] = False

print("\nThe number of valid passports is:", valid.count(True))

