number = int(input())
word = input()
strings = []
filtered = []

for i in range(number):
    current_string = input()
    strings.append(current_string)
    if word in current_string:
        filtered.append(current_string)
print(strings)
print(filtered)
