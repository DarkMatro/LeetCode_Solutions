select
    Products.product_name,
    sum(unit) as unit
from
    Orders
    inner join Products
    on Orders.product_id = Products.product_id
where
    year(order_date) = 2020
    and month(order_date) = 2
group by
    Orders.product_id
having
    sum(unit) >= 100
