/*
Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
*/

SELECT e1.name AS Employee
FROM Employee e1 INNER JOIN Employee e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;