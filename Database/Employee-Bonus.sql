SELECT
    Employee.name,
    Bonus.bonus
FROM
    Employee
        LEFT JOIN Bonus
        ON Employee.empId = Bonus.empId
where
    Bonus.bonus < 1000
    or Bonus.bonus is null

