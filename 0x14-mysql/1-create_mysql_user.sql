mysql -e "CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';"
mysql -e "GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';"
