number_of_Snowballs = int(input())
best_snowball_quality = 0
best_snowball_Data = ""

for _ in range(number_of_Snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    result = (weight / time) ** quality

    if result > best_snowball_quality:
        best_snowball_quality = result
        best_snowball_Data = f"{weight} : {time} = {int(result)} ({quality})"

print(best_snowball_Data)

