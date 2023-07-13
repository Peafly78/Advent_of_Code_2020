#***** ADVENT OF CODE 2020 *****
#************ DAY 13 ************
#****************** Part 1 *****


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


# 