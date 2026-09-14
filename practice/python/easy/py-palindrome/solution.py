# Xom Data · Check palindrome
# Problem: https://xomdata.com/practice/py-palindrome
# Solved: 2026-09-14

def is_palindrome(text):
    s = text.lower()
    return s == s[::-1]
