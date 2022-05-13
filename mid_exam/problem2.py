def add_func(data, value):
    data.append(value)
    return data


def remove_func(data, value):
    if value in data:
        data.remove(value)
        return data


def replace_func(data, value):
    replacements = value.split(" ")
    num1 = replacements[0]
    num2 = replacements[1]
    for i in data:
        if i == value:
            data.remove(i)
            data.insert([num1], num2)

    return data


def collapse_func(data, value):
    new_data = [num for num in data if num >= value]
    return new_data


def numbers(data):

    while True:
        command = input().split(" ")
        if command[0] == "Finish":
            print(" ".join(data))
            break

        current_command = command[0]
        value = command[1]
        replacement = command[2]

        if current_command == "Add":
            data = add_func(data, value)

        elif current_command == "Remove":
            data = remove_func(data, value)

        elif current_command == "Replace":
            data = replace_func(data, value)

        elif current_command == "Collapse":
            data = collapse_func(data, value)


info = input().split(" ")
numbers(info)
