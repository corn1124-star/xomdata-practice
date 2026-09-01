-- Xom Data · Customer spending per order
-- Problem: https://xomdata.com/practice/medium-join-001
-- Solved: 2026-09-01

SELECT
    c.full_name,
    COUNT(*) AS order_count,
    COALESCE(SUM(o.total_amount), 0) AS total_spending,
    COALESCE(AVG(o.total_amount), 0) AS avg_order_value,
    DENSE_RANK() OVER(ORDER BY COALESCE(SUM(o.total_amount), 0) DESC, c.full_name ASC ) AS spending_rank
FROM customers c
INNER JOIN orders o
ON c.id = o.customer_id
GROUP BY c.id, c.full_name
