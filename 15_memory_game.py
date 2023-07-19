#***** ADVENT OF CODE 2020 *****
#************ DAY 15 ************
#****************** Part 1 *****



# get input data

starting_numbers = [1,0,15,2,10,13]

# play game and create number list according to rules

count = len(starting_numbers)
last_place_dict = {starting_numbers[i] : i + 1 for i in range(len(starting_numbers)-1)}

current_num = starting_numbers[-1]

while count != 30000000:
    next_num = 0
    if current_num in last_place_dict:
        next_num = count - last_place_dict[current_num]
    last_place_dict[current_num] = count
    current_num = next_num
    count += 1

print(current_num)