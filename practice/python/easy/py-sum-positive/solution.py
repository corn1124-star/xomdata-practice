# Xom Data · Total receipts
# Problem: https://xomdata.com/practice/py-sum-positive
# Solved: 2026-09-14

def sum_positive(numbers):
    if not numbers:
        return 0
    sum_positive = 0
    for i in numbers:
        if i > 0:
            sum_positive += i
    
    return sum_positive
