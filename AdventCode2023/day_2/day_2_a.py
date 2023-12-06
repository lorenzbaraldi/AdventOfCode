import re
with open('day_2_input') as f:
    input = f.read().splitlines()

configuration = {'red': 12, 'green': 13, 'blue': 14}
sum_idx = 0
for record in input:
    game_number = int(record.split(':')[0].split(' ')[1])
    elements = re.split(',|;| ', record.split(':')[1])
    considered = True
    for idx,element in enumerate(elements):
        if element.isdigit():
            value = int(element)
            colour = elements[idx+1]
            if value > configuration[colour]:
                considered = False
    if considered:
        print(game_number)
        sum_idx += game_number

print(sum_idx)