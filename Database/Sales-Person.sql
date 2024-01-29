select
    SalesPerson.name
from
    Orders
    inner join Company
    on Company.com_id = Orders.com_id 
    and Company.name = 'RED'
    right join SalesPerson
    on SalesPerson.sales_id = Orders.sales_id
where 
    Orders.sales_id is null