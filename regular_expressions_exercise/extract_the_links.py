import re
links = []

while True:
    text = input()
    if len(text) != 0:
        pattern = r"www.\w+([\-\.][a-z]+)*"

        result = re.findall(pattern, text)
        if len(result) > 0:
            links.append(result[0])

    else:
        break

for link in links:
    print(link)




