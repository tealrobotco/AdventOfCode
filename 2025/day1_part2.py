# Read in the input file from data/input_dayone.txt
with open("data/input_dayone.txt", "r") as file:
    sequence = file.readlines()
    sequence = [line.strip() for line in sequence]

start = 50
dial_size = 100 # 0 to 99

# Test Sequences
# sequence = [
#     "L68",
#     "L30",
#     "R48",
#     "L5",
#     "R60",
#     "L55",
#     "L1",
#     "L99",
#     "R14",
#     "L82",
# ]

# sequence = [
#     "R1000",
# ]

current_position = start
answer = 0
for command in sequence:
    direction = -1 if command[0] == "L" else 1
    old_position = current_position
    new_position = old_position + direction * int(command[1:])
    current_position = new_position % dial_size
    
    # Count how many times we click on 0
    answer += new_position // dial_size - old_position // dial_size if direction == 1 else (old_position - 1) // dial_size - (new_position - 1) // dial_size
    
    print(f"{command}: {old_position} -> {new_position} (mod {current_position}), total={answer}")

print("Answer: ", answer)