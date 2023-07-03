#***** ADVENT OF CODE 2020 *****
#************ DAY 4 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("04_passports_input.txt") as input:
    input_data = input.read().split("\n\n")

# count valid passports

valid = [True for passport in range(len(input_data))]

for i in range(len(input_data)):
    for item in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if item not in input_data[i]:
            valid[i] = False

print("\nThe number of valid passports is:", valid.count(True))



#****************** Part 2 *****


# import data into dictionary

passport_list = [line.split() for line in input_data]

passport_dicts = list()

for pp in passport_list:
    temp_dict = {}
    for entry in pp:
        temp_dict[entry[:3]] = entry[4:]
    passport_dicts.append(temp_dict)

dicts_to_be_removed = list()

for i in range(len(passport_dicts)):
    for item in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if item not in passport_dicts[i]:
            dicts_to_be_removed.append(passport_dicts[i])

for dict in dicts_to_be_removed:
    passport_dicts.remove(dict)

# convert and check values --- check, doesn't work yet

valid_dicts = list()

for dict in passport_dicts:
    for key, value in dict.items():
        if key == "byr":
            value = int(value)
            if value < 1920 or value > 2002:
                break
        elif key == "iyr":
            value = int(value)
            if value < 2010 or value > 2020:
                break
        elif key == "eyr":
            value = int(value)
            if value < 2020 or value > 2030:
                break
        elif key == "hgt":
            height = int(value[:-2])
            if value[-2:] == "cm":
                if height < 150 or height > 193:
                    break
            elif value[-2:] == "in":
                if height < 59 or height > 76:
                    break
        elif key == "hcl":
            if not value.startswith("#") or len(value) != 7:
                break
            for char in value:
                if char not in "0123456789abcdefgf":
                    break
        elif key == "ecl":
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                break
        elif key == "pid":
            if len(value) != 9:
                break
            for char in value:
                if char not in "0123456789":
                    break
        valid_dicts.append(dict)
        
for dict in valid_dicts:
    print(dict)