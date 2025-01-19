# Write your MySQL query statement below
select product_id,year first_year , quantity , price from Sales
where (product_id,year) in(select product_id,min(year) as year from sales group by product_id)
-- group by product_id