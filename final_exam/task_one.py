text = input()

command = input()
while command != "Done":
    command = command.split(" ")

    if command[0] == "Change":
        char = command[1]
        replacement = command[2]
        text = text.replace(char, replacement)
        print(text)

    elif command[0] == "Includes":
        substring = command[1]
        if substring in text:
            print("True")
        else:
            print("False")

    elif command[0] == "End":
        substring = command[1]
        if text.endswith(substring):
            print("True")
        else:
            print("False")

    elif command[0] == "Uppercase":
        new_text = ""
        for char in text:
            if char.islower():
                char = char.upper()
                new_text += char
            else:
                new_text += char
            text = new_text
        print(text)

    elif command[0] == "FindIndex":
        char = command[1]
        print(text.index(char))

    elif command[0] == "Cut":
        start_index = int(command[1])
        count = int(command[2])
        text = text[start_index:count+3]
        print(text)

    command = input()
