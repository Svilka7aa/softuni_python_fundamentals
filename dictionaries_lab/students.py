text = input()
courses = dict()

while ":" in text:

    (name, id, course) = text.split(":")

    if course not in courses.keys():
        courses[course] = dict()

    courses[course][id] = name

    text = input()

text = text.replace("_", " ")

for id in courses[text]:
    print(f"{courses[text][id]} - {id}")
