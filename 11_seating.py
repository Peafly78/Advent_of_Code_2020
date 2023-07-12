#***** ADVENT OF CODE 2020 *****
#************ DAY 11 ************
#****************** Part 1 *****



# get input data

input_data = None

with open("11_seating_input.txt") as input:
    input_data = [input.strip("\n") for input in input.readlines()]

# create seat class

class Seat: 
    def __init__(self, occupied=False):
        self.occupied = occupied
        self.neighbors = list()
    
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def is_occupied(self):
        return self.occupied
    
    def has_neighbors(self):
        for neighbor in self.neighbors:
            if neighbor.is_occupied():
                return True
        return False
                
    def has_four_neighbors(self):
        count_occupied = 0
        for neighbor in self.neighbors:
            if neighbor.is_occupied():
                count_occupied += 1
        return count_occupied >= 4
    
    def change_occupation(self):
        if self.is_occupied():
            self.occupied = False
        else:
            self.occupied = True
    
    def display(self):
        if self.is_occupied():
            print("#", end=" ")
        else:
            print("L", end=" ")

# create seats according to grid

seating_matrix = [[Seat() if spot == "L" else 0 for spot in row] for row in input_data]

# add neighbors where appropriate

for i in range(len(seating_matrix)):
    for j in range(len(seating_matrix[0])):
        if seating_matrix[i][j] == 0:
            continue
        possible_neighbors = list()
        if i > 0:
            possible_neighbors.append(seating_matrix[i-1][j])
            if j > 0:
                possible_neighbors.extend([seating_matrix[i-1][j-1], seating_matrix[i][j-1]])
            if j < len(seating_matrix[0])-1:
                possible_neighbors.append(seating_matrix[i-1][j+1])
        if i < len(seating_matrix)-1:
            possible_neighbors.append(seating_matrix[i+1][j])
            if j < len(seating_matrix[0])-1:
                possible_neighbors.extend([seating_matrix[i+1][j+1], seating_matrix[i][j+1]])
            if j > 0:
                possible_neighbors.append(seating_matrix[i+1][j-1])
        if i == 0 and j > 0:
            possible_neighbors.append(seating_matrix[i][j-1])
        if i == len(seating_matrix)-1 and  j < len(seating_matrix[0])-1:
            possible_neighbors.append(seating_matrix[i][j+1])
        
        for spot in possible_neighbors:
            if spot == 0:
                continue
            seating_matrix[i][j].add_neighbor(spot)

# print()
# for row in seating_matrix:
#     for seat in row:
#         if seat == 0:
#             print(".", end=" ")
#         else:
#             print(len(seat.neighbors), end=" ")
#     print()
# print()

# create function for changing seat status -- fix this

def change_seats(matrix):
    marked_for_change = list()

    for row in matrix:
        for seat in row:
            if seat == 0:
                continue
            if seat.is_occupied() and seat.has_four_neighbors():
                marked_for_change.append(seat)
            elif not seat.is_occupied() and not seat.has_neighbors():
                marked_for_change.append(seat)
    
    for seat in marked_for_change:
        seat.change_occupation()
    
    return len(marked_for_change) > 0

# create function to print matrix

def print_matrix(matrix):
    print()
    for row in matrix:
        for seat in row:
            if seat == 0:
                print(".", end=" ")
            else:
                seat.display()
        print()
    print()

# create function to count occupied seats

def count_occupied_seats(matrix):
    count = 0
    for row in matrix:
        for seat in row:
            if seat == 0:
                continue
            if seat.is_occupied():
                count += 1
    return count

# calculate occupied seats

# while change_seats(seating_matrix):
#     continue

# print("\nThe count of occupied seats is:", count_occupied_seats(seating_matrix))




#****************** Part 2 *****



# create function to look around in matrix 

def look_up_and_down(matrix, pos):
    visible_occupied_seats = 0
    row = pos[0]
    col = pos[1]

    for i in range(1, row+1):
        next_cell = matrix[row-i][col]
        if next_cell == 0:
            continue
        if next_cell.is_occupied():
            visible_occupied_seats += 1
        break
        
    for i in range(1, len(matrix)-row+1):
        next_cell = matrix[row+i][col]
        if next_cell == 0:
            continue
        if next_cell.is_occupied():
            visible_occupied_seats += 1
        break

    return visible_occupied_seats

def look_left_and_right(matrix, pos):
    visible_occupied_seats = 0
    row = pos[0]
    col = pos[1]

    for i in range(1, col+1):
        next_cell = matrix[row][col-i]
        if next_cell == 0:
            continue
        if next_cell.is_occupied():
            visible_occupied_seats += 1
        break

    for i in range(1, len(matrix[0])-col+1):
        next_cell = matrix[row][col+i]
        if next_cell == 0:
            continue
        if next_cell.is_occupied():
            visible_occupied_seats += 1
        break

    return visible_occupied_seats

def look_diagonal(matrix, pos):
    visible_occupied_seats = 0
    row = pos[0]
    col = pos[1]

    for i in range(1, min(row, col)+1):
        next_cell = matrix[row-i][col-i]
        if next_cell == 0:
            continue
        if next_cell.is_occupied():
            visible_occupied_seats += 1
        break

    for i in range(1, min(row, len(matrix[0])-col)+1):
        next_cell = matrix[row-i][col+i]
        if next_cell == 0:
            continue
        if next_cell.is_occupied():
            visible_occupied_seats += 1
        break

    for i in range(1, min(len(matrix)-row, col)+1):
        next_cell = matrix[row+i][col-i]
        if next_cell == 0:
            continue
        if next_cell.is_occupied():
            visible_occupied_seats += 1
        break

    for i in range(1, min(len(matrix)-row, len(matrix[0])-col)+1):
        next_cell = matrix[row+i][col+i]
        if next_cell == 0:
            continue
        if next_cell.is_occupied():
            visible_occupied_seats += 1
        break

    return visible_occupied_seats

# combine all three functions above into one:

def look_around(matrix, pos):
    return sum([look_up_and_down(matrix, pos), look_left_and_right(matrix, pos), look_diagonal(matrix, pos)])

# create function for changing seat status according to new rules

def change_seats_visibility(matrix): # fix this -- index error
    marked_for_change = list()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            seat = matrix[row][col]
            if seat == 0:
                continue
            if seat.is_occupied() and look_around(matrix, (row, col)) <= 5:
                marked_for_change.append(seat)
            elif not seat.is_occupied() and look_around(matrix, (row, col)) == 0:
                marked_for_change.append(seat)
    
    for seat in marked_for_change:
        seat.change_occupation()
    
    return len(marked_for_change) > 0

# count occupied seats according to new rules

while change_seats_visibility(seating_matrix):
    continue

print("\nThe count of occupied seats is:", count_occupied_seats(seating_matrix))

# Testing

position = (5, 2)
print()
print(position)
print_matrix(seating_matrix)

print()
print("Up and down:", look_up_and_down(seating_matrix, position))
print()
print("Left and right:", look_left_and_right(seating_matrix, position))
print()
print("Diagonal:", look_diagonal(seating_matrix, position))

print("All together:", look_around(seating_matrix, position))