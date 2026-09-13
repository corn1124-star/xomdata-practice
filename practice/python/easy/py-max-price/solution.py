# Xom Data · Highest price in the list
# Problem: https://xomdata.com/practice/py-max-price
# Solved: 2026-09-13

def highest_price(prices):
    if not prices:
        return 0
    for i in prices:
        if i < 0:
            break
    return max(prices)
