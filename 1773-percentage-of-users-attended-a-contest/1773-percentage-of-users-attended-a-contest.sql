# Write your MySQL query statement below
WITH uc AS (
    SELECT COUNT(user_id) AS c FROM Users
)
SELECT contest_id, round(count(user_id)/uc.c*100,2) as percentage FROM register,uc
group by contest_id
order by percentage desc,contest_id asc;