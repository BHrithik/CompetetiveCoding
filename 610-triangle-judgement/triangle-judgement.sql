# Write your MySQL query statement below
SELECT X,Y,Z, IF(X+Y>Z AND Y+Z > X AND Z+X> Y,"Yes","No") as triangle from Triangle