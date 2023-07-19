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

for key, val in spec_dict.items():
    print(key, " >> ", val)

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

