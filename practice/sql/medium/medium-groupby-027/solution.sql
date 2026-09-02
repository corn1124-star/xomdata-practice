-- Xom Data · Average score per subject
-- Problem: https://xomdata.com/practice/medium-groupby-027
-- Solved: 2026-09-02

SELECT
    s.subject_name,
    s.credits,
    COUNT(g.id) AS student_count,
    ROUND(AVG(g.final_score), 2) AS avg_score,
    ROUND(
        100.0 * COUNT(CASE WHEN g.final_score >= 5 THEN 1 END) 
        / NULLIF(COUNT(g.final_score), 0), 
        2
    ) AS pass_rate,
    RANK() OVER(
        ORDER BY AVG(g.final_score) DESC
    ) AS rank_by_avg,
    NTILE(4) OVER(
        ORDER BY AVG(g.final_score) DESC, s.subject_name ASC
    ) AS difficulty_quartile
FROM subjects s
LEFT JOIN grades g
    ON s.id = g.subject_id
GROUP BY 
    s.id, 
    s.subject_name, 
    s.credits;
