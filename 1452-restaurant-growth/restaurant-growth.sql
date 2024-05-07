SELECT 
    visited_on,
    (
        SELECT sum(amount)
        FROM customer 
        WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) and c.visited_on
    ) AS amount,
    Round(
        (
            SELECT sum(amount)/7
            FROM Customer 
            WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) and c.visited_on)
            ,
        2
    ) AS average_amount
FROM Customer c
WHERE visited_on >= (
    SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) 
    FROM customer
)
GROUP BY visited_on;