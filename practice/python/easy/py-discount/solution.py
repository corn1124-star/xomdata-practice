# Xom Data · Compute price after discount
# Problem: https://xomdata.com/practice/py-discount
# Solved: 2026-09-13

def final_price(price, percent):
    return round((price * ((100 - percent)/100)), 2) if price >= 0 and (0 <= percent <= 100) else []
