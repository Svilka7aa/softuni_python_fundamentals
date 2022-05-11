def electron_distribution(number):
    field_shields = []
    counter = 1
    while True:
        element = 2 * (counter ** 2)

        if element < number:
            number -= element
            field_shields.append(element)
        else:
            field_shields.append(number)
            break

        counter += 1

    print(field_shields)


data = int(input())
electron_distribution(data)