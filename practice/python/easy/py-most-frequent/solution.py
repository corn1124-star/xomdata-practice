# Xom Data · Most frequent character
# Problem: https://xomdata.com/practice/py-most-frequent
# Solved: 2026-09-14

def most_frequent(text):
    return max(text, key=text.count)
