# Write your MySQL query statement below
SELECT query_name, ROUND(AVG(rating/position),2) AS quality, ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) as poor_query_percentage
FROM Queries where query_name is NOT NULL
group by query_name 