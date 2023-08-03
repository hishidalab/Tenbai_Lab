CREATE USER 'user'@'localhost' IDENTIFIED BY 'hoge';
GRANT ALL PRIVILEGES ON pengin.* TO 'user'@'localhost';
ALTER USER 'user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hoge';
CREATE USER 'user'@'%' IDENTIFIED BY 'hoge';
GRANT ALL PRIVILEGES ON pengin.* TO 'user'@'%';
ALTER USER 'user'@'%' IDENTIFIED WITH mysql_native_password BY 'hoge';
