-- mysql project
-- task 18/101
SELECT STATE, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
