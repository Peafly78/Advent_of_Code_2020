#***** ADVENT OF CODE 2020 *****
#************ DAY 11 ************
#****************** Part 1 *****



# get input data

input_data = None

with open("11_seating_input.txt") as input:
    input_data = [input.strip("\n") for input in input.readlines()]

print(input_data)

# create seat class

class Seat: 
    def __init__(self, occupied=False):
        self.occupied = occupied
        self.neighbors = list()
    
    def __repr__(self):
        return "S"
    
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def is_occupied(self):
        return self.occupied
    
    def has_neighbors(self):
        for neighbor in self.neighbors:
            if neighbor.is_occupied:
                return True
        return False
                
    def has_four_neighbors(self):
        count_occupied = 0
        for neighbor in self.neighbors:
            if neighbor.is_occupied:
                count_occupied += 1
        return count_occupied >= 4
    
    def change_occupation(self):
        if self.is_occupied:
            self.occupied = False
        else:
            self.occupied = True
    
    def display(self):
        if self.is_occupied:
            return "#"
        return "L"

# create seats according to grid

seating_matrix = [[Seat() if spot == "L" else 0 for spot in row] for row in input_data]

for row in seating_matrix:
    print(row)

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

print()
for row in seating_matrix:
    for seat in row:
        if seat == 0:
            print(".", end=" ")
        else:
            print(len(seat.neighbors), end=" ")
    print()
print()

# create function for changing seat status -- fix this

def change_seats(matrix):
    for row in matrix:
        for seat in row:
            if seat == 0:
                continue
            if seat.is_occupied() and seat.has_four_neighbors():
                print("Changing to empty")
                seat.change_occupation()
            elif not seat.is_occupied() and not seat.has_neighbors():
                print("Changing to occupied")
                seat.change_occupation()
    return matrix

# create function to print matrix



# Testing

print()
for row in seating_matrix:
    for seat in row:
        if seat == 0:
            print(".", end=" ")
        else:
            print(seat.display(), end=" ")
    print()
print()

change_seats(seating_matrix)

print()
for row in seating_matrix:
    for seat in row:
        if seat == 0:
            print(".", end=" ")
        else:
            print(seat.display(), end=" ")
    print()
print()