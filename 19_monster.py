#***** ADVENT OF CODE 2020 *****
#************ DAY 19 ************
#****************** Part 1 *****



# get input data

input_data = None
rules = None
messages = None

with open("19_monster_input.txt") as input:
    input_data = input.read().split("\n\n")       

messages = input_data[1].split("\n")
formatting_rules = [rule.split(": ") for rule in input_data[0].split("\n")]

for rule in formatting_rules:
    rule[0] = int(rule[0])
    rule[1] = rule[1].strip('"')
    if rule[1] not in "ab":
        if "|" not in rule[1]:
            rule[1] = [int(ref) for ref in rule[1].split()]
        else:
            rule[1] = [[int(ref) for ref in set.split()] for set in rule[1].split(" | ")]
        
rules = {rule[0] : rule[1] for rule in formatting_rules}

# continue here
