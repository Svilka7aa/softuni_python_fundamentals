text = input()
cards = text.split(' ')
count = int(input())

for num in range(count):
    half_text_length = int(len(cards)/2)
    first_cards = cards[:half_text_length]
    second_cards = cards[-half_text_length:]
    cards = []
    for line in range(half_text_length):
        cards.append(first_cards[line])
        cards.append(second_cards[line])
print(cards)
