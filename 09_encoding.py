#***** ADVENT OF CODE 2020 *****
#************ DAY 9 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("09_encoding_input.txt") as input:
    input_data = [int(input.strip("\n")) for input in input.readlines()]

# find entry violating rules                 

for i in range(25, len(input_data)):
    preamble = input_data[i-25:i]
    match_found = False
    for num in preamble:
        diff = input_data[i]-num
        if diff != num and diff in preamble:
            match_found = True
            break
    if not match_found:
        print(f"\nThe violating value is:", input_data[i])
        break