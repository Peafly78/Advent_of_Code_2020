#***** ADVENT OF CODE 2020 *****
#************ DAY 18 ************
#****************** Part 1 *****



# get input data

input_data = None

with open("18_maths_input.txt") as input:
    input_data = [operation.strip("\n") for operation in input.readlines()]          

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

# find subcalculations

def find_subcalc(calc): # test with input
    start = 0
    end = len(calc)
    nesting_level = 0
    for i in range(len(calc)):
        if calc[i] == "(":
            start = i+1
            nesting_level += 1
            for j in range(start, len(calc)):
                if calc[j] == ")":
                    nesting_level -= 1
                    if nesting_level == 0:
                        end = j                        
                        subcalc = calc[start:end]
                        if len(subcalc) == len(calc):
                            return None
                        return calc[start:end]
                elif calc[j] == "(":
                    nesting_level += 1
                else:
                    continue       

def count_elements(nested_list):
    count = 0
    for item in nested_list:
        if isinstance(item, list):
            count += count_elements(item) + 2
        else:
            count += 1
    return count         

# reorder calculations

def reorder(calc):
    new_order = list()
    skip = 0
    while skip < len(calc):
        for i in range(skip, len(calc)):
            item = calc[i]
            if item == "(":
                item = find_subcalc(calc[i:])
                if "(" in item:
                    sub = reorder(item)
                    skip += count_elements(sub)+2
                    new_order.append(sub)
                else:
                    skip += len(item)+2
                    new_order.append(item)
                break
            elif item == ")":
                skip += 1
            else:
                new_order.append(item)
                skip += 1
    return new_order
         
reordered_calcs = [reorder(calc) for calc in calculations]

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

for calc in reordered_calcs[:]:
    results.append(solve(calc))
    
print(results)

print("The sum of the resulting values is:", sum(results))

#****************** Part 2 *****


# define function for solving calculations according to new rules

def solve_add_first(calc):
    step_one_result = list()
    temp_result = 0
    operator = "+"
    while calc:
        next = calc.pop(0)
        if not isinstance(next, list):
            if not isinstance(next, int):
                operator = next
                if operator == "*":
                    step_one_result.append(temp_result)
                    temp_result = 0
                    step_one_result.append(operator)
            else:
                if operator == "+":
                    temp_result = operations[operator](temp_result, next)
                else:
                    temp_result = next
        else: 
            if operator == "+":
                temp_result = operations[operator](temp_result, solve_add_first(next))
            else:
                temp_result = solve_add_first(next)
    if temp_result:
        step_one_result.append(temp_result)
    return solve(step_one_result)   

# calculate results

results_add_first = list()

for calc in [reorder(calc) for calc in calculations]:
    results_add_first.append(solve_add_first(calc))

print("The sum of the resulting values is:", sum(results_add_first))