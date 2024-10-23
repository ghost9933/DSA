# Write your MySQL query statement below
select round(COUNT(CASE WHEN order_date = customer_pref_delivery_date THEN 1 END)/count(order_date)*100,2) as immediate_percentage 
from (
    select *,row_number() over (partition by customer_id order by order_date asc) as rn from Delivery 
) main where rn=1

