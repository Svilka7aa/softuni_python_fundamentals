def courses():
    courses_dict = {}
    while True:
        command = input()
        if command == "end":
            break

        command = command.split(" : ")
        if command[0] not in courses_dict.keys():
            courses_dict[command[0]] = []
        courses_dict[command[0]].append(command[1])

    for key, value in courses_dict.items():
        print(f"{key}: {len(value)}")
        for student in value:
            print(f"-- {student}")


courses()
