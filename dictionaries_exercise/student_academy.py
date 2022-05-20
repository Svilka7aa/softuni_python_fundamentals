def student_grades():
    students_dict = {}
    number = int(input())
    for i in range(number):
        student = input()
        grade = float(input())
        if student not in students_dict:
            students_dict[student] = []
        students_dict[student].append(grade)

    for key, value in students_dict.items():
        average = sum(value)/len(value)
        if average >= 4.5:
            print(f"{key} -> {average:.2f}")


student_grades()
