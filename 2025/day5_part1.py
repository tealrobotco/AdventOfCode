# ingest the input file
with open("data/input_dayfive.txt", "r") as file:
    input = [line.strip() for line in file.readlines()]

# Test Input
# input = [
#     "3-5",
#     "10-14",
#     "16-20",
#     "12-18",
#     "",
#     "1",
#     "5",
#     "8",
#     "11",
#     "17",
#     "32",
# ]

# Read the input until you reach a blank line
good_food_ranges = []
while True:
    line = input.pop(0)
    if line == "":
        break
    good_food_ranges.append([int(x) for x in line.split("-")])

# The remaining input is the available food
available_food = [int(x) for x in input]

# part 1
fresh_food = []
for food in available_food:
    for food_range in good_food_ranges:
        if int(food) >= food_range[0] and int(food) <= food_range[1]:
            fresh_food.append(food)
            break


print("good_food_ranges: ", good_food_ranges)
print("available_food: ", available_food)
print("fresh_food: ", fresh_food)

print("Answer: ", len(fresh_food))
