#***** ADVENT OF CODE 2020 *****
#************ DAY 9 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("09_encoding_input.txt") as input:
    input_data = [int(input.strip("\n")) for input in input.readlines()]

# find entry violating rules                 

violating_idx = None

for i in range(25, len(input_data)):
    preamble = input_data[i-25:i]
    match_found = False
    for num in preamble:
        diff = input_data[i]-num
        if diff != num and diff in preamble:
            match_found = True
            break
    if not match_found:
        violating_idx = i
        break

print(f"\nThe violating value is:", input_data[violating_idx])



#****************** Part 2 *****


# find encryption weakness

encryption_weakness = None
contiguous_set = list()

for num in input_data[:violating_idx]:
    while sum(contiguous_set) > input_data[violating_idx]:
        contiguous_set.pop(0)

    if sum(contiguous_set) == input_data[violating_idx]:
        encryption_weakness = min(contiguous_set) + max(contiguous_set)
        break
      
    contiguous_set.append(num)
    
print("\nFound encryption weakness:", encryption_weakness)