quantity = int(input())
days = int(input())

christmas_spirit = 0
total_price = 0
day_five_condition = False

for day in range(1, days + 1):
    day_five_condition = False

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        christmas_spirit += 5
        total_price += 2 * quantity

    if day % 3 == 0:
        christmas_spirit += 13
        total_price += (5 * quantity) + (3 * quantity)
        day_five_condition = True

    if day % 5 == 0:
        christmas_spirit += 17
        total_price += quantity * 15

        if day_five_condition:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        total_price += 23

        if day == days:
            christmas_spirit -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {christmas_spirit}")









