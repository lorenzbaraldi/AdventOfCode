with open("day_6_input") as f:
    input = f.read().splitlines()

times = [time for time in input[0].split(":")[1].split(" ") if time != ""]
distance = [time for time in input[1].split(":")[1].split(" ") if time != ""]
ways_to_beat = 0

times = [int("".join(times))]
distance = [int("".join(distance))]


for idx, time in enumerate(times):
    distance_to_beat = distance[idx]
    for hold in range(1, time):
        distance_run = hold * (time-hold)
        if distance_run > distance_to_beat:
            ways_to_beat += 1

print(ways_to_beat)
# product = 1
# for ways in ways_to_beat:
#     product *= ways
# print(product)

