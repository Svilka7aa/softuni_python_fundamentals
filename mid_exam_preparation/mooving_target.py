target = input().split(" ")
target = list(map(int, target))

line = input()

while line != "End":
    command1 = line.split(" ")
    command = command1[0]
    index = int(command1[1])
    value = int(command1[2])

    if command == "Shoot" and index >= 0 and index < len(target):
        current_target = target[index]
        current_target -= value
        if current_target <= 0:
            target.pop(index)
        else:
            target[index] = current_target

    elif command == "Add":
        if index >= 0 and index < len(target):
            target.insert(index, value)

        else:
            print("Invalid placement!")

    elif command == "Strike":
        if index - value >= 0 and index + value < len(target):
            target = target[:index - value] + target[index + value + 1:]
        else:
            print("Strike missed!")

    line = input()

target = list(map(str, target))
output = "|".join(target)
print(output)
