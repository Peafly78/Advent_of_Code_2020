#***** ADVENT OF CODE 2020 *****
#************ DAY 18 ************
#****************** Part 1 *****



# get input data

input_data = None

with open("18_maths_input.txt") as input:
    input_data = [operation.strip("\n") for operation in input.readlines()]

print(input_data)

# format operation

calculations = list()

for calc in input_data:
    calculation = list()
    for char in calc:
        if char == " ":
            continue
        elif char in "0123456789":
            calculation.append(int(char))
        else:
            calculation.append(char)
    calculations.append(calculation)

print(calculations)

# reorder calculations

def reorder(calc): # enters infinite loop -- correct
    new_order = list()
    flag = False
    skip = 0
    while skip < len(calc):
        for i in range(skip, len(calc)):
            if flag:
                flag = False
                break
            if calc[i] == "(":
                sub_calc = calc[i+1:]
                for j in range(len(sub_calc)):
                    if sub_calc[j] == ")":
                        sub_calc = sub_calc[:j]
                        new_order.append(sub_calc)
                        skip += i+j
                        flag = True
                        break
            else:
                new_order.append(calc[i])
                skip += 1
        
    return new_order

reordered_calcs = [reorder(calc) for calc in calculations]

print(reordered_calcs)

# define helper functions

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

operations = {"+" : add, "*" : multiply}

def solve(calc):
    result = calc.pop(0)
    operator = None
    while calc:
        next = calc.pop(0)
        if not isinstance(next, int):
            operator = next
        else:
            result = operations[operator](result, next)
    return result

# calculate result

# results = list()

# for calc in calculations:
#     results.append(solve(calc))

# print(results)

