-- Xom Data · Revenue from delivered orders
-- Problem: https://xomdata.com/practice/easy-sum-001
-- Solved: 2026-09-01

SELECT SUM(total_amount) AS total_revenue
FROM orders
WHERE status LIKE 'Delivered'
