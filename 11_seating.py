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
        return "#" if self.occupied else "L"
    
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def is_occupied(self):
        return self.is_occupied
    
    def has_neighbors(self):
        return len(self.neighbors) > 0
    
    def has_four_neighbors(self):
        return len(self.neighbors) >= 4

# create seats according to grid

seating_matrix = [[Seat() if spot == "L" else 0 for spot in row] for row in input_data]

for row in seating_matrix:
    print(row)

# add neighbors where appropriate

for i in range(len(seating_matrix)-1):
    for j in range(len(seating_matrix[0])-1):
        if seating_matrix[i][j] == 0:
            continue
        possible_neighbors = [seating_matrix[i+1][j], seating_matrix[i+1][j+1], seating_matrix[i][j+1]]
        for spot in possible_neighbors:
            if spot == 0:
                continue
            seating_matrix[i][j].add_neighbor(spot)

for i in range(len(seating_matrix)-1,1,-1): # traverse backwards to add left, up, diagonal


# add remaining missing links


for row in seating_matrix:
    for seat in row:
        if seat == 0:
            print(seat)
        else:
            print(seat.neighbors)