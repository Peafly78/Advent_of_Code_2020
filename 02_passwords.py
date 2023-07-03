#***** ADVENT OF CODE 2020 *****
#************ DAY 2 ************
#****************** Part 1 *****


from collections import namedtuple


# get input data

input_data = None

with open("02_passwords_input.txt") as input:
    input_data = input.readlines()

instructions_passwords = [item.strip("\n").split(": ") for item in input_data]

for item in instructions_passwords:
    item[0] = item[0].split()
    item[0][0] = item[0][0].split("-")

InstrPw = namedtuple("InstrPw", ["min", "max", "char", "pw"])
        
instr_pws = list()

for instr_pw in instructions_passwords:
    instr_pws.append(InstrPw(int(instr_pw[0][0][0]), int(instr_pw[0][0][1]), instr_pw[0][1], instr_pw[1]))

# count how many passwords are valid

valid_count = 0

for entry in instr_pws:
    char_count = entry.pw.count(entry.char)
    if char_count >= entry.min and char_count <= entry.max:
        valid_count += 1

print("\nThe total number of valid passwords is:", valid_count)


