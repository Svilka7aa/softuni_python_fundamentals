text = input()
print("".join([text[i] for i in range(len(text)) if text[i] != text[i - 1] or i == 0]))