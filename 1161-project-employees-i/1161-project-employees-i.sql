# Write your MySQL query statement below
select project_id,round(sum(experience_years)/count(e.employee_id),2) average_years 
from project p inner join employee e
where p.employee_id=e.employee_id
group by project_id