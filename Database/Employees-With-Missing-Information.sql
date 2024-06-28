select
    Salaries.employee_id
from
    Salaries
    left join Employees
    on Salaries.employee_id = Employees.employee_id
where
    Employees.employee_id is null

union

select
    Employees.employee_id as employee_id
from
    Employees
    left join Salaries
    on Employees.employee_id = Salaries.employee_id
where
    Salaries.employee_id is null

order by
    employee_id asc
