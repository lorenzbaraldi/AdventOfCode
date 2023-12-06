from collections import defaultdict
with open("day_5_input") as f:
    input = f.read().splitlines()


dict_conversion = defaultdict(list)
list_sum = []
seeds = [int(seed) for seed in input[0].split(":")[1].split(" ") if seed != ""]
current_conversion = ""
for row in input[1:]:
    if ":" in row:
        current_conversion = row.split(":")[0]
    elif row != "":
        dict_conversion[current_conversion].append([int(conversion) for conversion in row.split(" ")])

print(dict_conversion)
local_element = 0
for idx,element in enumerate(seeds):
    local_element = 0
    list_sum.append(element)

    for conversion in dict_conversion:
        found = False
        for converted in dict_conversion[conversion]:
            destination = converted[0]
            source = converted[1]
            offset = converted[2]
            if list_sum[idx]>= source and list_sum[idx]< source + offset:
                list_sum[idx] = destination + (list_sum[idx] - source)
                found = True
                break
        # if not found:
        #     list_sum[idx] = element
print(min(list_sum))
