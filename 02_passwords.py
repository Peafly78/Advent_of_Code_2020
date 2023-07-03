#***** ADVENT OF CODE 2020 *****
#************ DAY 2 ************
#****************** Part 1 *****


from collections import namedtuple


# get input data

input_data = None

with open("02_passwords_input.txt") as input:
    input_data = input.readlines()

print(input_data)

instructions_passwords = [item.strip("\n").split(": ") for item in input_data]

for item in instructions_passwords:
    item[0] = item[0].split()
    item[0][0] = item[0][0].split("-")
    for pos in item[0][0]:
        pos = int(pos)

print(instructions_passwords)

InstrPw = namedtuple("InstrPw", ["min", "max", "char", "pw"])
        
instr_pws = list()

for instr_pw in instructions_passwords:
    instr_pws.append(InstrPw(instr_pw[0][0][0], instr_pw[0][0][1], instr_pw[0][1], instr_pw[1]))

for item in instr_pws:
    print(tuple(item))

