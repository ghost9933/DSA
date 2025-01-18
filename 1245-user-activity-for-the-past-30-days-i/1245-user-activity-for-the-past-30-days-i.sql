# Write your MySQL query statement below

select activity_date  day  ,count(distinct user_id) active_users  from Activity
WHERE 
    DATEDIFF('2019-07-27', activity_date) < 30 AND DATEDIFF('2019-07-27', activity_date)>=0

 group by activity_date