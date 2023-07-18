#***** ADVENT OF CODE 2020 *****
#************ DAY 14*************
#****************** Part 1 *****



# get input data

input_data = None

with open("14_bitmask_input.txt") as input:
    input_data = [input.strip("\n") for input in input.readlines()]

mask_list = list()
subdict = dict()

for item in input_data: # fix this, data isn't input correctly
    if item.startswith("mask"):
        mask_list.append(item[7:])
    else:
        split = item.split(" = ")
        mask_list.append({split[0] : int(split[1])})

# calculate values and write them to memory

def apply_mask(mask, value_str):
    changed_val = ""
    for i in range(len(mask)):
        if mask[i] == "X":
            changed_val += value_str[i]
        else:
            changed_val += mask[i]
    return changed_val

def convert_to_bin_36zeros(dec_value):
    return bin(dec_value)[2:].zfill(36)

def convert_to_dec(bin_string):
    return int("0b" + str(int(bin_string)), 2)
    

combined_memory = dict()
bitmask = ""

for item in mask_list:
    if type(item) == dict:
        for key, value in item.items():
            combined_memory[key] = convert_to_dec(apply_mask(bitmask, str(convert_to_bin_36zeros(value))))
    else:
        bitmask = item

# calculate sum of all values in combined memory

result = sum(combined_memory.values())

print("\nThe sum of all values in memory after completion of program initialization is:", result)




#****************** Part 2 *****

from itertools import permutations

# format input data so it is usable for new rules

# change apply mask function according to new rules

def apply_mask_2(mask, value_str):
    changed_val = ""
    for i in range(len(mask)):
        if mask[i] == "0":
            changed_val += value_str[i]
        else:
            changed_val += mask[i]
    return changed_val

def find_all_combos(n):
    combos = list()
    values = ["1" for i in range(n)] + ["0" for i in range(n)]
    for combo in permutations(values, n):
        if combo not in combos:
            combos.append(combo)
    return combos

def process_floating_bits(value_str):
    address_list = list()
    combos = find_all_combos(value_str.count("X"))
    for combo in combos:
        new_address = ""
        idx = 0
        for char in value_str:
            if char == "X":
                new_address += combo[idx]
                idx += 1
            else:
                new_address += char
        address_list.append(new_address)
    return address_list

# calculate result according to new rules

processed_mask_list = list()

for item in mask_list:
    if type(item) == dict:
        for key, value in item.items():
            processed_mask_list.append({int(key[4:-1]) : value})
    else:
        processed_mask_list.append(item)

# for item in processed_mask_list:
#     print(item)

combined_memory_2 = dict()
bitmask_2 = ""

for item in processed_mask_list:
    if type(item) == dict:
        for key, value in item.items():
            new_addresses = process_floating_bits(apply_mask_2(bitmask_2, convert_to_bin_36zeros(key)))
            for address in new_addresses:
                combined_memory_2[convert_to_dec(address)] = value
            
    else:
        bitmask_2 = item

# print(combined_memory_2)

# calculate sum of all values in combined memory

result_2 = sum(combined_memory_2.values())

print("\nThe sum of all values in memory after completion of program initialization according to new is:", result_2)

# Testing

# test_mask = "000000000000000000000000000000X1101X"

# new_addresses = process_floating_bits(test_mask)

# print()
# for address in new_addresses:
#     print(address)
