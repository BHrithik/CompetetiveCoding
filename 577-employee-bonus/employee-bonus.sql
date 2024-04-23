SELECT E.name AS name, B.bonus AS Bonus 
FROM Employee AS E
LEFT JOIN Bonus AS B ON E.empId = B.empId 
WHERE B.bonus < 1000 OR B.bonus IS NULL;
