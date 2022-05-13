import math
budget = float(input())
students = int(input())
price_package_floor = float(input())
price_of_one_egg = float(input())
price_of_single_apron = float(input())

free_packages = 0
for i in range(1, students + 1):
    if i % 5 == 0:
        free_packages += 1


twenty_percent_aprons = math.ceil(students * 0.2)
aprons_needed = price_of_single_apron * (students + twenty_percent_aprons)
eggs_needed = students * 10 * price_of_one_egg
floor_needed = price_package_floor * students - free_packages * price_package_floor
total = aprons_needed + eggs_needed + floor_needed

if budget >= total:
    print(f"Items purchased for {total:.2f}$.")
else:
    print(f"{total - budget:.2f}$ more needed.")