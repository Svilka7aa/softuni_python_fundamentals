budget = float(input())
price_for_kg_flour = float(input())

price_for_pack_eggs = price_for_kg_flour * 0.75
price_for_liter_milk = price_for_kg_flour + (price_for_kg_flour * 0.25)

price_for_one_bread = price_for_kg_flour + price_for_pack_eggs + price_for_liter_milk * 0.25

eggs_counter = 0
easter_bread = 0

while budget >= price_for_one_bread:
    budget -= price_for_one_bread
    easter_bread += 1
    eggs_counter += 3
    if easter_bread % 3 == 0:
        eggs_counter -= (easter_bread - 2)


print(f"You made {easter_bread} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")
