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

# Testing

