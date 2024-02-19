mysql -e "CREATE USER 'replica_user'@'%' IDENTIFIED BY 'password';"
mysql -e "GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';"
