(SELECT U.name AS results 
FROM Users AS U 
LEFT JOIN MovieRating AS M ON U.user_id = M.user_id 
GROUP BY M.user_id 
ORDER BY COUNT(*) DESC, U.name ASC
LIMIT 1)
UNION ALL
(SELECT title AS results
FROM MovieRating JOIN Movies USING(movie_id)
WHERE YEAR(created_at) = 2020 AND MONTH(created_at) = 2
GROUP BY movie_id
ORDER BY AVG(rating) DESC, title
LIMIT 1)