# Write your MySQL query statement below
with root as (
select class,count(student) c from Courses 

group  by  class)
select class from root where c>=5