import re
with open('day_2_input') as f:
    input = f.read().splitlines()


power = 0
for record in input:
    game_number = int(record.split(':')[0].split(' ')[1])
    elements = re.split(',|;| ', record.split(':')[1])
    minimum_configuration = {'red': 1, 'green': 1, 'blue': 1}
    for idx,element in enumerate(elements):
        if element.isdigit():
            value = int(element)
            colour = elements[idx+1]
            if value > minimum_configuration[colour]:
                minimum_configuration[colour] = value
    power += minimum_configuration['red'] * minimum_configuration['green'] * minimum_configuration['blue']

print(power)