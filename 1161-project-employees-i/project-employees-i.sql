# Write your MySQL query statement below
SELECT p.project_id as project_id, ROUND(SUM(e.experience_years)/COUNT(p.employee_id),2) as average_years
FROM Project as P CROSS JOIN Employee as e on p.employee_id = e.employee_id
GROUP BY p.project_id