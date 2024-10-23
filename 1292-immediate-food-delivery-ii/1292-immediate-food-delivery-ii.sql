# Write your MySQL query statement below
with main as(select *,row_number() over (partition by customer_id order by order_date asc) as rn from Delivery )
select round(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 else 0 END)/count(order_date)*100,2) as immediate_percentage 
from  main where rn=1

