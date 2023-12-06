import math
with open("day_4_input") as f:
    input = f.read().splitlines()

card_list = [1 for element in range(len(input))]
total_cards = 0

for current_card, row in enumerate(input):
    winning_numbers = [element for element in row.split(":")[1].split("|")[0].split(" ") if element != '']
    my_numbers = [element for element in row.split(":")[1].split("|")[1].split(" ") if element != '']
    local_points = 0
    for number in my_numbers:
        if number in winning_numbers:
            local_points += 1
    for i in range(current_card+1, local_points + current_card+1 if local_points + current_card+1 < len(card_list) else len(card_list)):
        card_list[i] += card_list[current_card]

for element in card_list:
    total_cards += element
print(total_cards)