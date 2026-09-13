# Xom Data · Letter grade from score
# Problem: https://xomdata.com/practice/py-grade-letter
# Solved: 2026-09-13

def grade_letter(score):
    if score in range(0, 101):
        if score >= 90:
            grade_letter = "A"
        elif score in range(80, 90):
            grade_letter = "B"
        elif score in range(70, 80):
            grade_letter = "C"
        elif score in range(60, 70):
            grade_letter = "D"
        else:
            grade_letter = "F"
    return grade_letter
