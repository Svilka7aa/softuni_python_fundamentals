def softuni_parking():
    register_dict = {}
    command = int(input())
    for i in range(command):
        person = input().split(" ")

        if person[0] == "register" and person[1] not in register_dict:
            register_dict[person[1]] = person[2]
            print(f"{person[1]} registered {person[2]} successfully")
        elif person[0] == "register" and person [1] in register_dict:
            print(f"ERROR: already registered with plate number {person[2]}")

        elif person[0] == "unregister" and person[1] not in register_dict:
            print(f"ERROR: user {person[1]} not found")
        else:
            del register_dict[person[1]]
            print(f"{person[1]} unregistered successfully")

    for key, value in register_dict.items():
        print(f"{key} => {value}")


softuni_parking()
