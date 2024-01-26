select
    E1.name as Employee
from Employee as E1
left join Employee as E2
on E2.id = E1.managerID

where
    E1.salary > E2.salary