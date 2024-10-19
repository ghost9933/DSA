-- # Write your MySQL query statement below
with main as (select query_name , round(sum(rating/position)/count(query_name),2) as quality, count(query_name) as c from Queries group by query_name),
rating as (
    select query_name , count(query_name) rc  from queries  where rating <3
    group by query_name
)
select main.query_name,main.quality,COALESCE(round(rating.rc/main.c*100,2),0) as poor_query_percentage from main
left  join rating
on main.query_name=rating.query_name
WHERE main.query_name IS NOT NULL

-- select query_name , round(sum(rating/position)/count(query_name),2) as quality, count(query_name) as c from Queries group by query_name


-- select query_name , count(query_name) rc from queries where rating <3
--     group by query_name