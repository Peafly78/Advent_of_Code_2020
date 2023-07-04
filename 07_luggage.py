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

already_checked = list()
check_list = ["shiny gold"]

while check_list:
    key_to_be_checked = check_list.pop(0)
    already_checked.append(key_to_be_checked)
    for key, value in rules_dict.items():
        if key_to_be_checked in value:
            check_list.append(key)

print(f"\nThere are {len(set(already_checked))-1} options to carry a shiny gold bag.")


#****************** Part 2 *****


# find out number of bags to buy

print()
print(rules_dict)

counting_dict = {key : value.split(", ") for key, value in rules_dict.items()}

print()
print(counting_dict)
print()

# stuck here, finish later

total_bags_needed = 0
check_list_2 = [(1,"shiny gold")]
temp_dict = dict()

while check_list_2:
    key_to_be_checked = check_list_2.pop(0)
    for entry in counting_dict[key_to_be_checked]:
        temp_list = entry.split()
        if temp_list[0] == "no":
            continue
        multiplier = int(temp_list[0])
        # bags_needed = int(temp_list[0])
        next_color = " ".join(temp_list[1:3])
        # total_bags_needed += bags_needed
        check_list_2.append(next_color)
        print(check_list_2)
        print(total_bags_needed)
        
        


