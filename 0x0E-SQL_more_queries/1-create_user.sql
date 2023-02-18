--This create a user and gives it priviledges
CREATE USER IF NOT EXIST user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT All PRIVILEGES ON * . * TO user_0d_1@localhost;
