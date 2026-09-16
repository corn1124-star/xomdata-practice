# Xom Data · Mask phone number
# Problem: https://xomdata.com/practice/py-mask-phone
# Solved: 2026-09-16

def mask_phone(phone):
    if not phone or len(phone) < 3:
        return phone
    if len(phone) > 3:
        return "*" * (len(phone)-3) + phone[-3:]
    else:
        return phone
