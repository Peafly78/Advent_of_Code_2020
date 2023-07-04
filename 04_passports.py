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

cleaned_data = [input_data[i] for i in range(len(input_data)) if valid[i]]

#****************** Part 2 *****


# import data into dictionary

passport_list = [line.split() for line in cleaned_data]

passport_dicts = list()

for pp in passport_list:
    temp_dict = {}
    for entry in pp:
        temp_dict[entry[:3]] = entry[4:]
    passport_dicts.append(temp_dict)

for dict in passport_dicts:
    print(dict)

# convert and check values --- check, doesn't work yet

for dict in passport_dicts:
    dict["valid"] = True
    for key, value in dict.items():
        if key == "byr":
            value = int(value)
            if value < 1920 or value > 2002:
                dict["valid"] = False
                break
        elif key == "iyr":
            value = int(value)
            if value < 2010 or value > 2020:
                dict["valid"] = False
                break
        elif key == "eyr":
            value = int(value)
            if value < 2020 or value > 2030:
                dict["valid"] = False
                break
        elif key == "ecl":
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                dict["valid"] = False
                break
        elif key == "pid":
            if len(value) != 9:
                dict["valid"] = False
                break
            for char in value:
                if char not in "0123456789":
                    dict["valid"] = False
                    break
        elif key == "hcl":
            if not value.startswith("#") or len(value) != 7:
                dict["valid"] = False
                break
            for char in value:
                if char not in "#0123456789abcdefgf":
                    dict["valid"] = False
                    break
        elif key == "hgt":
            if len(value) < 4:
                dict["valid"] = False
                break
            else:
                height = int(value[:-2])
                if value[-2:] == "cm":
                    if height < 150 or height > 193:
                        dict["valid"] = False
                        break
                elif value[-2:] == "in":
                    if height < 59 or height > 76:
                        dict["valid"] = False
                        break
        else:
            continue

valid_dicts = [dict for dict in passport_dicts if dict["valid"]]

print("\nThe number of valid passports after validation is:", len(valid_dicts))
