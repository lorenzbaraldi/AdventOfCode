import re
from collections import defaultdict
with open("day_3_input") as f:
    input = f.read().splitlines()

coordinates = defaultdict(int)

for row, element in enumerate(input):
    for columns, character in enumerate(element):
        if character != '.' and not character.isdigit():
            coordinates[(row, columns)] = 1
number_sum = 0
for row, element in enumerate(input):
    splitted = re.split('[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', element)
    splitted = [element for element in splitted if element != '']
    for number in splitted:
        number_correct = False
        position = element.find(number)
        if position != -1:
            for search_row in range(row-1, row+2):
                for i in range(position-1, position + len(number)+1):
                    if coordinates[(search_row, i)] == 1:
                        number_correct = True
        if number_correct:
            number_sum += int(number)
        element = element.replace(number, ''.join(['.' for i in range(len(number))]), 1)
        #print(element)

print(number_sum)




