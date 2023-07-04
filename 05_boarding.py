#***** ADVENT OF CODE 2020 *****
#************ DAY 5 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("05_boarding_input.txt") as input:
    input_data = input.read().split("\n")

# decipher instructions

seat_ids = [[i*8+j for j in range(8)] for i in range(128)]

def decipher_boarding_pass(seat_spec, rows=128, cols=8):
    row = [i for i in range(rows)]
    col = [j for j in range(cols)]
    for char in seat_spec[:7]:
        if char == "F":
            row = row[:len(row)//2]
        elif char == "B":
            row = row[len(row)//2:]
    for char in seat_spec[7:]:
        if char == "L":
            col = col[:len(col)//2]
        elif char == "R":
            col = col[len(col)//2:]
    return row[0], col[0]

deciphered_seat_positions = [decipher_boarding_pass(seat_spec) for seat_spec in input_data]

deciphered_seat_ids = [seat_ids[deciphered_seat_positions[i][0]][deciphered_seat_positions[i][1]] for i in range(len(deciphered_seat_positions))]

print("\nThe highest seat ID is:", max(deciphered_seat_ids))


#****************** Part 2 *****


# find missing seat

occupied_seats = [["X" if seat_id in deciphered_seat_ids else seat_id for seat_id in row] for row in seat_ids]

start_idx = None
flag = False

for i in range(len(occupied_seats)):
    if flag:
        break
    for j in range(len(occupied_seats[0])):
        if occupied_seats[i][j] == "X":
            start_idx = i
            flag = True
            break

your_seat = None
for i in range(start_idx, len(occupied_seats)):
    for j in range(len(occupied_seats[0])):
        if occupied_seats[i][j] != "X":
            if occupied_seats[i-1][j] == "X" and occupied_seats[i+1][j] == "X":
                your_seat = occupied_seats[i][j]

print("\nYour seat ID is:", your_seat)
