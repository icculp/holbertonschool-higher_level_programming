-- mysql project
-- task 18/101
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (6, 7) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
