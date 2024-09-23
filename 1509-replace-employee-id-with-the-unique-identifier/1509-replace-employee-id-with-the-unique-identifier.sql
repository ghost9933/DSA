# Write your MySQL query statement below
select u.unique_id  unique_id, e.name name from Employees E left join EmployeeUNI U
on e.id=u.id