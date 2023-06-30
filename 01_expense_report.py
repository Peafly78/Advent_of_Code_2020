#***** ADVENT OF CODE 2020 *****
#************ DAY 1 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("01_expense_report_input.txt") as input:
    input_data = input.readlines()
    
expenses = [int(entry.strip("/n")) for entry in input_data]

print(expenses)

