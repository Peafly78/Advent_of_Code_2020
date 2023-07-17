#***** ADVENT OF CODE 2020 *****
#************ DAY 14*************
#****************** Part 1 *****



# get input data

input_data = None

with open("14_bitmask_input.txt") as input:
    input_data = [input.strip("\n") for input in input.readlines()]

mask_list = list()
subdict = dict()

for item in input_data:
    if item.startswith("mask"):
        mask_list.append(subdict)
        subdict["mask"] = item[7:]
    else:
        split = item.split(" = ")
        subdict[split[0]] = int(split[1])

mask_list.append(subdict)
del subdict
mask_list.pop(0)

print(mask_list)

# calculate values and write them to memory

combined_memory = dict()

def apply_mask(mask, value):
    changed_val = ""
    for i in range(len(mask)):
        if mask[i] == "X":
            changed_val += value[i]
        else:
            changed_val += mask[i]
    return changed_val

def convert_to_bin_36zeros(dec_value):
    return bin(dec_value)[2:].zfill(36)

def convert_to_dec(bin_value):
    pass # continue here

# then write to memory

dec_val = 11
bin_val = convert_to_bin_36zeros(dec_val)
print(bin_val)

changed_val = apply_mask(mask_list[0]["mask"], str(bin_val))
print(changed_val)
