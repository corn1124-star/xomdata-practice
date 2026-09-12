# Xom Data · Row totals and column totals of a table
# Problem: https://xomdata.com/practice/py-row-col-sums
# Solved: 2026-09-12

def row_col_sums(table):
    if not table or not table[0]:
        return ([], [])

    row_sums = []
    col_sums = [0] * len(table[0])

    for row in table:
        r_sum = 0
        for j, val in enumerate(row):
            r_sum += val
            col_sums[j] += val
        row_sums.append(r_sum)

    return (row_sums, col_sums)
