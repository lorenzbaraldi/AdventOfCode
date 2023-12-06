with open('./day_1/day_1_input') as f:
    input = f.read().splitlines()

sum = 0



for element in input:
    first_index = ''
    number = ''
    for character in element:
        if character.isdigit():
            if first_index == '':
                first_index = int(character)
            else:
                number = int(character)
    if number == '':
        number = first_index
    sum += first_index*10 + number

print(sum)