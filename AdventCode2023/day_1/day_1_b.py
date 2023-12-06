with open('day_1_input') as f:
    input = f.read().splitlines()

sum = 0
numbers = {0:'zero',1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7: 'seven', 8:'eight', 9:'nine' }
local_sums = []
for row in input:
    row_list = []
    first_number = -1
    last_number = -1
    first_position = -1
    last_position = -1

    for index in range(10):
        first_occurrence = row.find(str(index))
        first_occurrence_word = row.find(numbers[index])
        last_occurrence = row.rfind(str(index))
        last_occurrence_word = row.rfind(numbers[index])
        if (first_occurrence < first_position or first_position == -1) and first_occurrence != -1:
            first_position = first_occurrence
            first_number = index
        if last_occurrence > last_position:
            last_position = last_occurrence
            last_number = index
        if (first_occurrence_word < first_position or first_position == -1) and first_occurrence_word != -1:
            first_position = first_occurrence_word
            first_number = index
        if last_occurrence_word > last_position:
            last_position = last_occurrence_word
            last_number = index
    local_sum = first_number * 10 + last_number
    sum += local_sum
    local_sums.append(local_sum)

with open('day_1_b_output', 'w') as f:
    for element in local_sums:
        f.write(str(element) + '\n')
print(sum)

