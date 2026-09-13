# Xom Data · Generate initials
# Problem: https://xomdata.com/practice/py-initials
# Solved: 2026-09-13

def get_initials(full_name):
    if not full_name or not full_name.replace(" ", "").isalpha():
        return ""

    return "".join(word[0].upper() for word in full_name.split())
