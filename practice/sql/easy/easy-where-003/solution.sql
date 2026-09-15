-- Xom Data · Delivered orders
-- Problem: https://xomdata.com/practice/easy-where-003
-- Solved: 2026-09-15

SELECT
    order_code,
    customers,
    total_amount
FROM orders
WHERE status LIKE "Delivered"
ORDER BY id ASC
