#***** ADVENT OF CODE 2020 *****
#************ DAY 7 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("07_luggage_input.txt") as input:
    input_data = input.read().split("\n")

rules = [rule.split("contain") for rule in input_data]

rules_dict = {" ".join(rule[0].strip().split()[:2]) : rule[1].strip() for rule in rules}

# find shiny gold bag carry options

carry_option_count = 0
already_checked = list()
check_list = ["shiny gold"]

while check_list:
    key_to_be_checked = check_list.pop(0)
    already_checked.append(key_to_be_checked)
    for key, value in rules_dict.items():
        if key_to_be_checked in value:
            check_list.append(key)

print(f"\nThere are {len(set(already_checked))-1} options to carry a shiny gold bag.")

