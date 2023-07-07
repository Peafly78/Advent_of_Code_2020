#***** ADVENT OF CODE 2020 *****
#************ DAY 7 ************
#****************** Part 1 *****


# get input data

input_data = None

with open("07_luggage_input.txt") as input:
    input_data = input.read().split("\n")

rules = [rule.split("contain") for rule in input_data]

rules_dict = {" ".join(rule[0].strip().split()[:2]) : rule[1].strip() for rule in rules}

# find shiny gold bag carry options

already_checked = list()
check_list = ["shiny gold"]

while check_list:
    key_to_be_checked = check_list.pop(0)
    already_checked.append(key_to_be_checked)
    for key, value in rules_dict.items():
        if key_to_be_checked in value:
            check_list.append(key)

print(f"\nThere are {len(set(already_checked))-1} options to carry a shiny gold bag.")


#****************** Part 2 *****

part_2_description = """

--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

    faded blue bags contain 0 other bags.
    dotted black bags contain 0 other bags.
    vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
    dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?

"""

# find out number of bags to buy

counting_dict = {key : value.split(", ") for key, value in rules_dict.items()}

# create bag class

class Bag:
    def __init__(self, name):
        self.name = name
        self.content = list()
    
    def __repr__(self):
        return self.name
    
    def add_bag(self, bag, amount):
        self.content.append((bag, amount))
    
# create bags

dict_of_bags = dict()

for key in counting_dict.keys():
    new_bag = Bag(key)
    dict_of_bags[new_bag.name] = new_bag

# fill bags 
 
for key, value in dict_of_bags.items():
    bags_contained = [entry.split() for entry in counting_dict[key]]
    for bag in bags_contained:
        if bag[0] == "no":
            break
        amount = int(bag[0])
        bag_name = " ".join(bag[1:3])
        value.add_bag(dict_of_bags[bag_name], amount)

for key, value in dict_of_bags.items():
    print(key, "-->", value.content)


# count bags that must be in shiny gold bag 

def count_contents(bag_list):
    count = 0
    if len(bag_list) == 0:
        count -= 1
        return count
    current_item = bag_list.pop(0)
    current_bag = current_item[0]
    current_multiplier = current_item[1]
    count += current_multiplier
    for item in current_bag.content:
        bag_list.append((item[0], item[1] * current_multiplier))
    return count + count_contents(bag_list)

shiny_gold_must_contain = count_contents([(dict_of_bags["shiny gold"], 1)])

print(f"\nA single shiny gold bag must contain a total of {shiny_gold_must_contain} other bags.")

# do it with a while loop

queue = [(dict_of_bags['shiny gold'], 1)]
bag_count = -1

while len(queue) > 0:
    current_item = queue.pop(0)
    current_bag = current_item[0]
    current_multiplier = current_item[1]
    bag_count += current_multiplier
    for item in current_bag.content:
        queue.append((item[0], item[1] * current_multiplier))

print(f"\nUsing a while loop the result is:", bag_count)
