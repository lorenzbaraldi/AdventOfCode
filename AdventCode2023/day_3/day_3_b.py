import re
from collections import defaultdict
with open("day_3_input") as f:
    input = f.read().splitlines()

coordinates = defaultdict(list)

for row, element in enumerate(input):
    for columns, character in enumerate(element):
        if character != '.' and not character.isdigit():
            coordinates[(row, columns)] = [1,0]
number_sum = 0
for row, element in enumerate(input):
    splitted = re.split('[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', element)
    splitted = [element for element in splitted if element != '']
    for number in splitted:
        ajacent_gear = []
        position = element.find(number)
       # adiacente = False
        if position != -1:
            for search_row in range(row-1, row+2):
                for i in range(position-1, position + len(number)+1):
                    if len(coordinates[(search_row, i)]) >= 2:
                        ajacent_gear.append((search_row, i))
                        #adiacente = True
        for row_gear, column_gear in ajacent_gear:
            coordinates[(row_gear, column_gear)][1] += 1
            coordinates[(row_gear, column_gear)][0] *= int(number)
        element = element.replace(number, ''.join(['.' for i in range(len(number))]), 1)
        #print(element)

for key, value in coordinates.items():
    if len(value) == 2 and value[1] == 2:
        number_sum += value[0]
print(number_sum)





