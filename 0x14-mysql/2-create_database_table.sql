mysql -e "CREATE DATABASE tyrell_corp;"
mysql -e "USE tyrell_corp; CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));"
mysql -e "USE tyrell_corp; INSERT INTO nexus6 (name) VALUES ('Leon');"
mysql -e "GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';"
