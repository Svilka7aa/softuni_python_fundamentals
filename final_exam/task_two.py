import re

number = int(input())
pattern = r"(.+)>(?P<digits>\d{3,})\|(?P<small>[a-z]{3,})\|(?P<big>[A-Z]{3,})" \
          r"\|(?P<spec>[0-9 A-Za-z$&+,:;=_{?@#|}'.-^*()%!]{3,})<\1+"

for _ in range(number):
    password = input()
    valid_password = re.findall(pattern, password)
    if len(valid_password) > 0:
        matches = re.finditer(pattern, password)
        for match in matches:
            digits = match.group("digits")
            small = match.group("small")
            big = match.group("big")
            spec = match.group("spec")
        print(f"Password: {digits}{small}{big}{spec}")

    else:
        print("Try another password!")
