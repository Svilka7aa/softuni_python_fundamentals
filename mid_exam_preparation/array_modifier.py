numbers = input().split()
numbers = list(map(int, numbers))

line = input()

while line != "end":
    if line == "decrease":
        numbers = list(map(lambda n: n-1, numbers))
    else:
        command = line.split(" ")
        command1 = command[0]
        index1 = int(command[1])
        index2 = int(command[2])

        if command1 == "swap":
            numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

        elif command1 == "multiply":
            numbers[index1] = numbers[index1] * numbers[index2]
    line = input()

final = list(map(str, numbers))
output = ", ".join(final)

print(output)




