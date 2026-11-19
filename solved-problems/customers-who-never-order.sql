/*
Write a solution to find all customers who never order anything.

Return the result table in any order.

Customers
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+

Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+


SELECT c.name AS Customers
FROM Customers C
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.customerId = c.id
    )*/
SELECT name AS Customers
FROM Customers LEFT JOIN Orders ON Customers.id = Orders.customerId
WHERE Orders.id IS NULL