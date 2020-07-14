-- SQL continues
-- Task 8
SELECT state_id AS id, name FROM hbtn_0d_usa.cities WHERE id IN (SELECT id FROM hbtn_0d_usa.states WHERE name = 'California') ORDER BY id ASC;
