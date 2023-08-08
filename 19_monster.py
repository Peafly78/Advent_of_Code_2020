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

# apply rules to messages

def rule_met(rule, letter):
    if rule == letter:
        return True
    return False

def is_reference(rule):
    return isinstance(rule, int):

def found_rule(rule):
    return isinstance(rule, str)

def message_compliant(message): # i guess it's too difficult for now
    starting_rule_ref = 0
    current_letter = message.pop(0)
    current_rule = rules[starting_rule_ref]
    sub_rules = None
    while current_rule:
        current_rule_part = current_rule.pop(0)
        while not found_rule(current_rule_part):
            while is_reference(current_rule_part):
                current_rule_part = rules[current_rule_part]
            else: 
                sub_rules = current_rule_part
                while sub_rules:
                    sub_rule = sub_rules.pop(0)
                    
            
        if rule_met(current_rule_part, current_letter):
            current_letter = message.pop(0)
            current_rule_part = current_rule.pop(0)
        else:
            return False
    

    return True

    else:
        current_rule = find_rule(current_rule)
    return False
