# Write your MySQL query statement below
select name from Customer where COALESCE(referee_id,0)<>2