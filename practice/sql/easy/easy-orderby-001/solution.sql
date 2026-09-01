-- Xom Data · Active menu sorted by price
-- Problem: https://xomdata.com/practice/easy-orderby-001
-- Solved: 2026-09-01

SELECT
    dish_name,
    price
FROM menu
WHERE status LIKE 'Active'
ORDER BY price ASC, dish_name ASC
