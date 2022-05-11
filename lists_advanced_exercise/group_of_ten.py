numbers = list(map(int, input().split(", ")))
group = 10
list_numbers = []

for i in numbers:
    if i < group:
        if i not in list_numbers:
                list_numbers.append(i)
print(f"Group of {group}'s: {list_numbers}")
group += 10
list_numbers.clear()
