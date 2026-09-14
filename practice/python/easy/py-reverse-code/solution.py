# Xom Data · Reverse the order code
# Problem: https://xomdata.com/practice/py-reverse-code
# Solved: 2026-09-14

def reverse_code(code):
    if not code:
        return ""
    code = list(code)
    return "".join(code[::-1])
