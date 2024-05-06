# Write your MySQL query statement below
with running_weight as(
            select *,
                SUM(weight) OVER(order by turn) as running_wt
            from Queue
) select person_name
  from running_weight
  where running_wt <= 1000
  order by turn desc
  limit 1;