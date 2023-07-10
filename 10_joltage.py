#***** ADVENT OF CODE 2020 *****
#************ DAY 10 ************
#****************** Part 1 *****

from functools import reduce

# get input data

input_data = None

with open("10_joltage_input.txt") as input:
    input_data = [int(input.strip("\n")) for input in input.readlines()]

input_data.sort()

# find built-in joltage adapter rating

joltage_diff_1 = 0
joltage_diff_3 = 1

if input_data[0] == 1:
    joltage_diff_1 += 1
if input_data[0] == 3:
    joltage_diff_3 += 1

for i in range(len(input_data)-1):
    if input_data[i+1] - input_data[i] == 1:
        joltage_diff_1 += 1
    elif input_data[i+1] - input_data[i] == 3:
        joltage_diff_3 += 1

print("\nThe number of 1-jolt differences multiplied by the number of 3-jolt differences is:", joltage_diff_1 * joltage_diff_3)




#****************** Part 2 *****

print(input_data)
# create graph

class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def __repr__(self):
        return "Value - " + str(self.value)

    def add_edge(self, vertex, weight = 0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())

class Graph:
    def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight = 0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def count_paths(self): # find way to count cluster and reduce each cluster by 1
        path_count = 1
        multi_vals = list()
        for vertex in self.graph_dict.values():
            if len(vertex.edges) > 1:
                multi_vals.append(len(vertex.edges))
        print(multi_vals)
        for i in range(len(multi_vals)):
            if multi_vals[i] > 1:
                multi_vals[i] -= 1
                break
        print(multi_vals)
        return reduce(lambda x, y: x*y, multi_vals)


    def count_all_paths(self, start_vertex, target_vertex): # in progress -- continue here
        path_count = 0
        stack = [start_vertex]
        seen = dict()
        current_path = list()
        while len(stack) > 0:
            current_vertex = stack.pop()
            seen[current_vertex] = True
            current_path.append(current_vertex)
            print(current_vertex, "---", current_path)
            if current_vertex == target_vertex:
                path_count += 1
                current_path.pop()
            else:
                vertices_to_visit = set(vertex.value for vertex in self.graph_dict[current_vertex].edges)
                stack += [vertex for vertex in vertices_to_visit if vertex not in seen]
        while current_path:
            new_current_vertex = current_path.pop()
            path_count += len(new_current_vertex.edges)
        return path_count
    

adapter_graph = Graph(True)

for adapter in input_data:
    new_vertex = Vertex(adapter)
    adapter_graph.add_vertex(new_vertex)
   
for vertex in adapter_graph.graph_dict.values():
   for adapter in input_data:
      weight = adapter-vertex.value
      if weight > 0 and weight <= 3:
         vertex.add_edge(adapter_graph.graph_dict[adapter], weight)


for key, value in adapter_graph.graph_dict.items():
   print(key, "-->", value.edges)

# count ways adapters can be connected

all_possible_adapter_options = adapter_graph.count_paths()

print(f"\nThere are {all_possible_adapter_options} ways to connect the adapters.")