# Xom Data · Average score by subject
# Problem: https://xomdata.com/practice/py-average
# Solved: 2026-09-13

def average_score(scores):
    if not scores:
        average_score = 0
    else:
        average_score = round(sum(scores)/len(scores), 1)
    
    return average_score
