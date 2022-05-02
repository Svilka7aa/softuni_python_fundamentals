lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total = 0
shield_counter = 0

for lost in range(1, lost_fights_count + 1):
    if lost % 2 == 0:
        total += helmet_price
    if lost % 3 == 0:
        total += sword_price
        if lost % 2 == 0:
            total += shield_price
            shield_counter += 1
    if shield_counter == 2:
        total += armor_price
        shield_counter = 0
print(f"Gladiator expenses: {total:.2f} aureus")


