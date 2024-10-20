-- # Write your MySQL query statement below
-- with main as (
--     select *,DATE_FORMAT(trans_date, '%Y-%m') as month  FROM Transactions
--     ),
-- global as (
-- select month, country, count(id) as trans_count ,sum(amount) trans_total_amount from main
-- group by month,country ),
-- filtered as (
--    select month m, country c
--    , count(id) as approved_count  ,sum(amount) approved_total_amount  
--    from main
--    where state='approved '
-- group by month,country 
-- )
-- select  month    ,country,trans_count , IFNULL(approved_count,0) approved_count, trans_total_amount ,ifnull(approved_total_amount,0) approved_total_amount from global left join filtered
-- on global.month=filtered.m and global.country=filtered.c


-- WITH main AS (
--     SELECT 
--         id,
--         DATE_FORMAT(trans_date, '%Y-%m') AS month,
--         country,
--         amount,
--         state
--     FROM Transactions
-- ),
-- global AS (
--     SELECT 
--         month, 
--         ifnull(country,'NULL') country, 
--         COUNT(id) AS trans_count,
--         SUM(amount) AS trans_total_amount 
--     FROM main
--     GROUP BY month, country
-- ),
-- filtered AS (
--     SELECT 
--         month AS m, 
--         ifnull(country,'NULL') c,
--         COUNT(id) AS approved_count,
--         SUM(amount) AS approved_total_amount  
--     FROM main
--     WHERE state = 'approved'  -- Removed the trailing space
--     GROUP BY month, country 
-- )
-- SELECT  
--     global.month,
--     if(global.country='NULL',NULL,global.country) as country,
--     global.trans_count,
--     IFNULL(filtered.approved_count, 0) AS approved_count,
--     global.trans_total_amount,
--     IFNULL(filtered.approved_total_amount, 0) AS approved_total_amount 
-- FROM global 
-- LEFT JOIN filtered
-- ON global.month = filtered.m AND global.country = filtered.c;


SELECT 
    LEFT(trans_date, 7) AS month,
    country, 
    COUNT(id) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM((state = 'approved') * amount) AS approved_total_amount
FROM 
    Transactions
GROUP BY 
    month, country;