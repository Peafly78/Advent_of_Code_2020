#***** ADVENT OF CODE 2020 *****
#************ DAY 16 ************
#****************** Part 1 *****



# get input data

input_data = None

with open("16_tickets_input.txt") as input:
    input_data = input.read().split("\n\n")

# format input data

specifications = [entry.split(": ") for entry in input_data[0].split("\n")]
spec_dict = {entry[0] : [tuple([int(num) for num in item.split("-")]) for item in entry[1].split(" or ")] for entry in specifications}

your_ticket = tuple([int(num) for num in input_data[1][13:].split(",")])

nearby_tickets = [tuple([int(num) for num in ticket.split(",")]) for ticket in input_data[2][16:].split("\n")]

# exclude invalid tickets

all_nums = list()

for val in spec_dict.values():
    for nums in val:
        all_nums.extend(i for i in range(nums[0], nums[1]+1))

valid_nums = set(all_nums)

ticket_scanning_error_rate = 0

for ticket in nearby_tickets:
    for num in ticket:
        if num not in valid_nums:
            ticket_scanning_error_rate += num

print("\nThe ticket scanning error rate is:", ticket_scanning_error_rate)




#****************** Part 2 *****



# exclude invalid tickets

valid_tickets = list()

for ticket in nearby_tickets:
    valid = True
    for num in ticket:
        if num not in valid_nums:
            valid = False
    if valid:
        valid_tickets.append(ticket)

# determine the meaning of the various fields

valid_nums_dict = {}

for key, val in spec_dict.items():
    new_val = list()
    for nums in val:
        new_val.extend(i for i in range(nums[0], nums[1]+1))
    valid_nums_dict[key] = new_val

field_position_dict = {}
possible_fields = list(valid_nums_dict.keys())

while len(list(field_position_dict)) < len(valid_tickets[0]):
    for i in range(len(valid_tickets[0])):
        if i in field_position_dict:
            continue
        next_please = False
        remaining_fields = [item for item in possible_fields if item not in field_position_dict.values()]
        if len(remaining_fields) == 1:
            field_position_dict[i] = remaining_fields[0]
            break
        for ticket in valid_tickets:
            if next_please:
                break
            for key, value in valid_nums_dict.items():
                if ticket[i] not in valid_nums_dict[key]:
                    if key in remaining_fields:
                        remaining_fields.remove(key)
                        if len(remaining_fields) == 1:
                            field_position_dict[i] = remaining_fields[0]
                            next_please = True
                            break

# calculate result from your ticket

result = 1

for key, value in field_position_dict.items():
    if value.startswith("departure"):
        result *= your_ticket[key]

print("\nThe final multiplication result of your ticket is:", result)

