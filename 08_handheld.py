#***** ADVENT OF CODE 2020 *****
#************ DAY 8 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("08_handheld_input.txt") as input:
    input_data = [tuple(input.strip().split()) for input in input.readlines()]

# process instructions



# change to function so it is reusable -- continue here

def process_instructions(list_of_instructions):
    accumulator = 0
    idx = 0
    indices_visited = []
    while idx < len(list_of_instructions):
        if idx in indices_visited:
            break
        indices_visited.append(idx)

        command = list_of_instructions[idx][0]
        move = list_of_instructions[idx][1]

        if command == "nop":
            idx += 1
            continue

        elif command == "acc":
            if move[0] == "+":
                accumulator += int(move[1:])
            elif move[0] == "-":
                accumulator -= int(move[1:])

        elif command == "jmp":
            if move[0] == "+":
                idx += int(move[1:])
                continue
            elif move[0] == "-":
                idx -= int(move[1:])
                continue
        
        idx += 1

    return accumulator

print("\nThe value of the accumulator before entering an infinite loop is:", process_instructions(input_data))



