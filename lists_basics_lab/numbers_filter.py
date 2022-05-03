n = int(input())
numbers = []


for i in range(n):
    current_num = int(input())
    numbers.append(current_num)

filtered = []
command = input()

if command == "positive":
    for number in numbers:
        if number >= 0:
            filtered.append(number)

if command == "negative":
    for number in numbers:
        if number < 0:
            filtered.append(number)

if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)

if command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)

print(filtered)
