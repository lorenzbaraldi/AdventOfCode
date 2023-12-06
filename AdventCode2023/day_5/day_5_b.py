from collections import defaultdict

with open("day_5_input") as f:
    input = f.read().splitlines()

dict_conversion = defaultdict(list)
list_sum = []
seeds = [int(seed) for seed in input[0].split(":")[1].split(" ") if seed != ""]
#
seeds_range = []
for idx in range(0, len(seeds), 2):
    seeds_range.append((seeds[idx], seeds[idx] + seeds[idx+1]))

current_conversion = ""
for row in input[1:]:
    if ":" in row:
        current_conversion = row.split(":")[0]
    elif row != "":
        dict_conversion[current_conversion].append([int(conversion) for conversion in row.split(" ")])

print(dict_conversion)

for conversion in dict_conversion:
    target = []
    while len(seeds_range) != 0:
        seed_range = seeds_range.pop()
        found_range = False
        for converted in dict_conversion[conversion]:
            destination = converted[0]
            source = converted[1]
            offset = converted[2]
            if seed_range[0] >= source and seed_range[1] < (source + offset):
                target.append([destination + (seed_range[0] - source), destination + (seed_range[1] - source)])
                found_range = True
                break
            if source <= seed_range[0] and (source + offset) <= seed_range[1] and (source + offset) > seed_range[0]:
                target.append([destination + (seed_range[0] - source), destination + offset])
                seeds_range.append([source+offset, seed_range[1]])
                found_range = True
                break
            if source >= seed_range[0] and (source + offset) <= seed_range[1]:
                target.append([destination, destination + offset])
                seeds_range.append([seed_range[0], source])
                seeds_range.append([source + offset, seed_range[1]])
                found_range = True
                break

        if not found_range and seed_range[0] != seed_range[1]:
            target.append(seed_range)
    seeds_range = target

print(target)
min_list = [element[0] for element in target]
print(min(min_list))