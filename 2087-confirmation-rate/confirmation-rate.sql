# Write your MySQL query statement below

SELECT e1.user_id as user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate from Signups as e1 
left join Confirmations as c on e1.user_id = c.user_id group by e1.user_id