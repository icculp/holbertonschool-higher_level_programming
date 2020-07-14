-- SQL continues
-- Task 1
CREATE USER IF NOT EXISTS user_0d_1@localhost;
UPDATE mysql.user SET authentication_string = PASSWORD('user_0d_1_pwd') WHERE user = 'user_0d_1' AND host = 'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
