#***** ADVENT OF CODE 2020 *****
#************ DAY 1 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("01_expense_report_input.txt") as input:
    input_data = input.readlines()
    
expenses = [int(entry.strip("/n")) for entry in input_data]

# find complementaries to 2020

def find_two(num, expenses):
    for entry in expenses:
        complementary = num-entry
        if complementary in expenses:
            return entry * complementary

print("\nThe result is:", find_two(2020, expenses))



#****************** Part 2 *****


# find 3 parts of 2020

result = 0

for entry in expenses:
    complementary = 2020-entry
    temp = find_two(complementary, expenses)
    if temp:
        result = entry * temp

print("\nThe new result is:", result)