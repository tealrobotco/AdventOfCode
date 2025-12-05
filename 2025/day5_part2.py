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


# Sort the good food ranges by the start of the range
good_food_ranges.sort(key=lambda x: x[0])

# Merge the good food ranges if they overlap
merged_good_food_ranges = []
for food_range in good_food_ranges:
    if merged_good_food_ranges and merged_good_food_ranges[-1][1] >= food_range[0]:
        merged_good_food_ranges[-1][1] = max(merged_good_food_ranges[-1][1], food_range[1])
    else:
        merged_good_food_ranges.append(food_range)

# Count each of the ranges in the merged good food ranges
range_counts = []
for food_range in merged_good_food_ranges:
    range_counts.append(food_range[1] - food_range[0] + 1)

# Sum the range counts
total_range_count = sum(range_counts)

print("range_counts: ", range_counts)
print("total_range_count: ", total_range_count)
print("Answer: ", total_range_count)
