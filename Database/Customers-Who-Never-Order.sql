SELECT
    Customers.name as Customers
FROM Customers
    LEFT JOIN Orders
    ON Customers.id = Orders.customerId
WHERE
    Orders.id is NULL