def grade_text():
    grade = float(input())
    
    if grade < 3:
        return "Fail"
    elif grade < 3.5:
        return "Poor"
    elif grade < 4.50:
        return "Good"
    elif grade < 5.50:
        return "Very Good"
    else:
        return "Excellent"


print(grade_text())
