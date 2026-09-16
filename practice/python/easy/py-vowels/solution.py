# Xom Data · Count vowels in a name
# Problem: https://xomdata.com/practice/py-vowels
# Solved: 2026-09-16

def count_vowels(name):
    if not name: return 0
    num = 0
    for i in name.lower():
        if i in ["a", "e", "i", "o", "u"]:
            num += 1
    
    return num
