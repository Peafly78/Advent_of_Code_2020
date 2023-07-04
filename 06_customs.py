#***** ADVENT OF CODE 2020 *****
#************ DAY 6 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("06_customs_input.txt") as input:
    input_data = input.read().split("\n\n")

# calculate sum of yes answers

combined_yes_answers = [len(set(person).difference(set("\n"))) for person in input_data]

sum_of_yes = sum(combined_yes_answers)

print("\nThe sum of the combined 'Yes' answers is:", sum_of_yes)