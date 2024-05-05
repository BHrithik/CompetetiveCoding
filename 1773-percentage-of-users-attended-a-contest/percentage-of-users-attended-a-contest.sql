# Write your MySQL query statement below
SELECT contest_id, ROUND(count(distinct user_id)*100/(SELECT count(user_id) from Users),2) as percentage
FROM REGISTER
GROUP BY contest_id ORDER BY percentage DESC, contest_id 
