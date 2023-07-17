#***** ADVENT OF CODE 2020 *****
#************ DAY 14*************
#****************** Part 1 *****



# get input data

input_data = None

with open("14_bitmask_input.txt") as input:
    input_data = [input.strip("\n") for input in input.readlines()]

print(input_data)

mask_list = list()
subdict = dict()

for item in input_data: # fix this, data isn't input correctly
    if item.startswith("mask"):
        mask_list.append(subdict)
        subdict["mask"] = item[7:]
    else:
        split = item.split(" = ")
        subdict[split[0]] = int(split[1])

mask_list.append(subdict)
del subdict
mask_list.pop(0)

# for dic in mask_list:
#     for key, value in dic.items():
#         print(key, " > ", value)
#     print()

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

for item in mask_list:
    bitmask = item["mask"]
    print("Bitmask:", bitmask)
    for key, value in item.items():
        if key == "mask":
            continue
        combined_memory[key] = convert_to_dec(apply_mask(bitmask, str(convert_to_bin_36zeros(value))))

for key, value in combined_memory.items():
    print(key, " --> ", value)

# calculate sum of all values in combined memory

result = sum(combined_memory.values())

print("\nThe sum of all values in memory after completion of program initialization is:", result)

# Testing

# dec_val = 11
# bin_val = convert_to_bin_36zeros(dec_val)
# print(bin_val)

# changed_val = apply_mask(mask_list[0]["mask"], str(bin_val))
# print(changed_val)

# changed_dec_val = convert_to_dec(changed_val)
# print(changed_dec_val)
