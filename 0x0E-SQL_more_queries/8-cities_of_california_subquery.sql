-- SQL continues
-- Task 8
SELECT id, name FROM hbtn_0d_usa.cities WHERE state_id = '1' ORDER BY id ASC;
-- FUCK YOU THIS SHOULD WORK ASSHOLES SELECT id, name FROM hbtn_0d_usa.cities WHERE state_id IN (SELECT id FROM hbtn_0d_usa.states WHERE name = 'California') ORDER BY id ASC;
