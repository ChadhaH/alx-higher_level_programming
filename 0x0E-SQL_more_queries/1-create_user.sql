--creates the MySQL server user user_0d_1.
CREATEIF IF NOT EXISTS USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
