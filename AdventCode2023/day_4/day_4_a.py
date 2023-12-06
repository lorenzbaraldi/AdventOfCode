import math
with open("day_4_input") as f:
    input = f.read().splitlines()

total_points = 0
for row in input:
    winning_numbers = [element for element in row.split(":")[1].split("|")[0].split(" ") if element != '']
    my_numbers = [element for element in row.split(":")[1].split("|")[1].split(" ") if element != '']
    local_points = 0
    for number in my_numbers:
        if number in winning_numbers:
            local_points += 1
    if local_points != 0:
        local_points = math.pow(2,local_points-1)
    total_points += local_points
print(total_points)