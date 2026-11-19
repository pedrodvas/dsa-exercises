/*
Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+


SELECT DISTINCT p1.email AS Email
FROM Person p1
left JOIN Person p2 ON p1.email = p2.email AND p1.id != p2.id
WHERE p2.id is NOT NULL;*/

SELECT p1.email AS Email
FROM Person p1
GROUP BY p1.email
HAVING COUNT(p1.email)> 1;