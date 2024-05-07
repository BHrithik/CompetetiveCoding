# Write your MySQL query statement below
WITH Accepters AS
    (SELECT accepter_id AS id, COUNT(accepter_id) AS num
    FROM RequestAccepted
    GROUP BY accepter_id),
Requesters AS
    (SELECT requester_id AS id, COUNT(requester_id) AS num
    FROM RequestAccepted
    GROUP BY requester_id),
Final AS
    (SELECT id, sum(num) as num FROM
        (SELECT * FROM Accepters UNION ALL SELECT * FROM Requesters) AS a
    GROUP BY id)
SELECT * FROM Final
ORDER BY num DESC LIMIT 1;
