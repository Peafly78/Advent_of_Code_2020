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


# find way to calculate timestamp after which busses cascade 

def is_cascade(timestamps): 
    for i in range(1, len(timestamps)):
        if timestamps[i]-1 != timestamps[i-1]:
            return False
    return True

# create function to return list with timestamps for each bus and x for empty bus slots

def find_cascade(buses, interval=1, start=None, step=1):
    if not start:
        start = buses[0]
    timestamp_bus_1 = buses[1]
    while (start + step) % buses[1] != 0:
        start += interval * buses[0]
    return start

def find_interval(): # continue here
    pass

# create function to fill empty bus slots (==x) with numbers that fit cascade
        
# Testing

print(find_cascade([13, 59], interval=11, start=78, step=3))

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