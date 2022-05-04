gifts = input().split(" ")
command = input()
current_gift_list = list(gifts)

while command != "No Money":
    command = command.split(" ")
    current_command = command[0]
    gift = command[1]

    if current_command == "OutOfStock":
        if gift in current_gift_list:
            current_gift_list = list(map(lambda x: x.replace(gift, "None"), current_gift_list))

    elif current_command == "Required":
        index = int(command[2])
        if index < len(current_gift_list):
            current_gift_list[index] = gift

    elif current_command == "JustInCase":
        current_gift_list[-1] = gift

    command = input()

for j in current_gift_list:
    if j == "None":
        current_gift_list.remove(j)

print(" ".join(current_gift_list))
