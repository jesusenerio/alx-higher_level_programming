-- creates database and table with their own values
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- create a table
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE AUTO_INCREMENT NOT NULL,name VARCHAR(256) NOT NULL,PRIMARY KEY(id));
