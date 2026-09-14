# Xom Data · Alternate-merge two lists
# Problem: https://xomdata.com/practice/py-merge-alternate
# Solved: 2026-09-14

def merge_alternate(list1, list2):
    m = min(len(list1), len(list2))
    return [x for p in zip(list1, list2) for x in p] + list1[m:] + list2[m:]
