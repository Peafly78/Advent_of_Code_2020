#***** ADVENT OF CODE 2020 *****
#************ DAY 15 ************
#****************** Part 1 *****



# get input data

starting_numbers = [1,0,15,2,10,13]

# play game and create number list according to rules

playing_numbers = starting_numbers[:]

current_num = playing_numbers[-1]

while len(playing_numbers) < 2020:
    if current_num not in playing_numbers[:-1]:
        current_num = 0
    else:
        reversed_playing_list = playing_numbers[:-1]
        reversed_playing_list.reverse()
        current_num = reversed_playing_list.index(current_num)+1
    playing_numbers.append(current_num)


print(playing_numbers[-1])
