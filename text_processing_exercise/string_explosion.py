text = input()
new_text = list()
strength = 0
for ch in text:
    if ch.isdigit():
        strength += int(ch)
        strength -= 1
        continue
    else:
        if strength < 1:
            new_text.append(ch)
        else:
            if ch == ">":
                new_text.append(ch)
            else:
                strength -= 1
                continue
print("".join(new_text))

