-- This create a database and a user
-- creates a database
CREATE DATABASE IF NOT EXIST hbtn_0d_2;
-- creates a user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- create grant select
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
