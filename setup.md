## Setting Up GCP Instance
# MySQL Requirements 
1. 2 vCPU | 4 GB GAM | 10 GB | Ubuntu 18.04 LTS
2. Allow traffic for: HTTP. HTTPS. SSH, MySSQL
3. MySQL Traffic: add new firewall rule (opne port 3306)
    - Name: mysql
    - Target Tags: mysql
    - Source IP ranges: 0.0.0.0/0
    - Protocols and ports: Check [TCP]: 3306



## .SSH Terminal Setup on GCP
1. sudo apt-get update 
2. sudo apt install mysql-client mysql-server # provides many dbs
3. sudo mysql # connecting to server 
4. Show what databases exist within the server
    - show databases; or show databases \G; # will show what databases are within the server
5. \q to leave the mysql server

## Create new DBA (database administrator)
1. Create user 'username'@'%' identified by 'ahi2022';
    - @ = wildcard
    - % desginates where the DBA connected from
2. To get a list of users: 
    - select * from mysql.user;
    - what db do we want to execute this query within
3. To get NEAT list of users:
    - select * from mysql.user \G;
4. Query to get a list of usernames only: 
    - select user, host, password_expired, authentication_string, password_last_changed from mysql.user \G; 
5. Exit mysql server: \q
6. LOGGING INTO MYSQL SERVER
    - mysql -u alice -p 
7. enter [password] 
8. select * from mysql.users;
9. Fix user permissions error: 
    - grant all privileges on *.* TO 'alice'@'%' with grant option;
10. Confirm privileges are opened to your user:
    - show grants for alice \G;

## CREATE A NEW DB IN MYSQL SERVER
1. Log back into mysql server
2. CREATE DATABASE db1;
3. Verify db was created by show all databases using:
    - show databases \G;
4. Change into new db directory to create a table:
    - Use db1
5. Create a new table within the new db1
     - CREATE TABLE table_name (job_title str, year int, salary varchar(255))
