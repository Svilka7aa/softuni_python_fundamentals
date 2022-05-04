money_list = input().split(", ")
beggars_number = int(input())

offers_counter = 0
beggars_list = []

for i in range(beggars_number):
    beggars_list.append(0)

while offers_counter < len(money_list):
    for j in range(len(beggars_list)):
        if offers_counter >= len(money_list):
            break
        beggars_list[j] += int(money_list[offers_counter])
        offers_counter += 1

print(beggars_list)


