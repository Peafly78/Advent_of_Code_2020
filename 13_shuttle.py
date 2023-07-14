#***** ADVENT OF CODE 2020 *****
#************ DAY 13 ************
#****************** Part 1 *****


from functools import reduce

# get input data

estimate = None
input_data = None

with open("13_shuttle_input.txt") as input:
    estimate = int(input.readline())
    input_data = [int(bus) if bus != "x" else bus for bus in input.readline().split(",")] 

# calculate earliest bus leaving at estimate

waiting_times = dict()
shortest_waiting_time = None

for bus in input_data:
    if bus != "x":
        waiting_times[bus] = bus - (estimate % bus)

for key, value in waiting_times.items():
    if value == min(waiting_times.values()):
        shortest_waiting_time = (key, value)

print(f"""\nThe shortest waiting time is {shortest_waiting_time[1]} minutes for traveling with bus {shortest_waiting_time[0]}.
These two numbers multiplied are:""", shortest_waiting_time[0] * shortest_waiting_time[1])



#****************** Part 2 *****


# create function to tell whether a list's values are cascading or not 

def is_cascade(timestamps): 
    for i in range(1, len(timestamps)):
        if timestamps[i]-1 != timestamps[i-1]:
            return False
    return True

# create function to return timestamp of first cascading value and cascading intervallist with timestamps for each bus and x for empty bus slots

def find_cascade(buses, interval=1, start=None, step=1):
    if not start:
        start = buses[0]
    while (start + step) % buses[1] != 0:
        start += interval * buses[0]
    return start + step, start // buses[0]

# create dictionary with timestamp and interval values

bus_dict = {}
step = 1

for i in range(len(input_data)-1):
    bus_1 = input_data[i]
    if bus_1 == "x":
        continue
    idx_bus_2 = i+1
    bus_2 = input_data[idx_bus_2]
    while bus_2 == "x":
        step += 1
        idx_bus_2 +=1
        bus_2 = input_data[idx_bus_2]
    bus_dict[(bus_1, bus_2)] = find_cascade((bus_1, bus_2), step=step)
    step = 1

print(bus_dict)

# usint dict values calculate end result
        
# Testing

print()
print(find_cascade((7, 13))[1])
print(find_cascade((7, 13))[0])

# print(find_cascade([13, 59], interval=find_interval((7, 13)), start=78, step=3))
# print(find_cascade((59, 31), interval=find_interval((13,59)), start=2655, step=2))
# print(find_cascade((31, 19)), interval=find_interval(59, 31))

# bus_7 = [7*i for i in range(33)]
# bus_13 = [13*i for i in range(33)]

# bus_7_test = [77]
# bus_7_test.extend([7*13*i + 7*11 for i in range(1, 33)])

# print(bus_7)
# print(bus_13)
# print()
# print(bus_7_test)

# test_list = [5, 9, 10]

# print(is_cascade(test_list))