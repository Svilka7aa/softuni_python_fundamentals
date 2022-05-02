number = int(input())
total = 0

for _ in range(number):
    char = input()
    total += ord(char)
print(f"The sum equals: {total}")