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
    # Count the number of times we land on 0
    direction = -1 if command[0] == "L" else 1
    current_position = (current_position + direction * int(command[1:])) % dial_size
    
    # Count the number of times we land on 0
    answer += 1 if current_position == 0 else 0
    
    print(f"{command}: {current_position}, total={answer}")

print("Answer: ", answer)