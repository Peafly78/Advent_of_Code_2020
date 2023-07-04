#***** ADVENT OF CODE 2020 *****
#************ DAY 6 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("06_customs_input.txt") as input:
    input_data = input.read().split("\n\n")

# calculate sum of yes answers

combined_yes_answers = [set(person).difference(set("\n")) for person in input_data]

sum_of_yes = sum([len(group) for group in combined_yes_answers])

print("\nThe sum of the combined 'Yes' answers is:", sum_of_yes)



#****************** Part 2 *****


# calculate number of questions everyone in a group answered with 'yes'

all_yes = [person.split("\n") for person in input_data]

all_yes_char_count = 0

for group in all_yes:
    joined = "".join(group)
    all_yes_chars = list()
    for char in joined:
        if joined.count(char) == len(group) and char not in all_yes_chars:
            all_yes_chars.append(char)
    all_yes_char_count += len(all_yes_chars)

print("\nThe sum of the all yes answers is:", all_yes_char_count) 
    