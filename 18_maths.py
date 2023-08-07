#***** ADVENT OF CODE 2020 *****
#************ DAY 18 ************
#****************** Part 1 *****



# get input data

input_data = None

with open("18_maths_input.txt") as input:
    input_data = [operation.strip("\n") for operation in input.readlines()]

print(input_data)

# find subcalculations

def find_subcalc(calc): # test with input
    start = 0
    end = len(calc)
    nesting_level = 0
    for i in range(len(calc)):
        if calc[i] == "(":
            start = i+1
            nesting_level += 1
        if calc[i] == ")":
            nesting_level -= 1
            if nesting_level == 0:
                end = i
    return calc[start:end]
            

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

def reorder(calc): 
    print("reordering:", calc)
    new_order = list()
    flag = False
    skip = 0
    while skip < len(calc):
        for i in range(skip, len(calc)):
            if flag:
                flag = False
                break
            print("processing:", i, calc[i])
            if calc[i] == "(":
                print("found subcalc")
                sub_calc = calc[i+1:]
                print("remaining:", sub_calc)
                nesting_level = 1
                for j in range(len(sub_calc)):
                    if sub_calc[j] == "(":
                        nesting_level += 1
                        print("increased nesting level to:", nesting_level)
                    elif sub_calc[j] == ")":
                        nesting_level -= 1
                        print("decreased nesting level to:", nesting_level)
                        if nesting_level != 0:
                            continue
                        sub_calc = sub_calc[:j]
                        while "(" in sub_calc:
                            sub_calc = reorder(sub_calc)
                        print(sub_calc)
                        new_order.append(sub_calc)
                        skip += i+j
                        print("skipping:", skip)
                        flag = True
                        break
                continue
            else:
                new_order.append(calc[i])
                skip += 1
        
    return new_order

reordered_calcs = [reorder(calc) for calc in calculations]

for calc in reordered_calcs:
    print(calc)

# define helper functions

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

operations = {"+" : add, "*" : multiply}

def solve(calc):
    result = 0
    operator = "+"
    while calc:
        next = calc.pop(0)
        if not isinstance(next, list):
            if not isinstance(next, int):
                operator = next
            else:
                result = operations[operator](result, next)
        else: 
            result = operations[operator](result, solve(next))
    return result

# calculate result

results = list()

for calc in reordered_calcs:
    results.append(solve(calc))
    
print(results)

print("The sum of the resulting values is:", sum(results))

