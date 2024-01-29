SELECT TOP 1
    Q1.customer_number
FROM 
    (select
        customer_number AS customer_number,
        COUNT(order_number) AS order_number
    from 
        Orders
    group by
        customer_number) AS Q1
ORDER BY Q1.order_number DESC
