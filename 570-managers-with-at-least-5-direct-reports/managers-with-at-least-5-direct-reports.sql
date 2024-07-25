-- SELECT e1.name AS name 
-- FROM Employee AS e1 
-- LEFT JOIN Employee AS e2 ON e1.id = e2.managerId 
-- GROUP BY e1.id, e1.name
-- HAVING COUNT(e2.managerId) >= 5;

SELECT m.name as name from
Employee as m LEFT JOIN Employee as e
on m.id = e.managerId
group by m.id, m.name
having COUNT(e.id) >= 5