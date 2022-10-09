# mysql-selfmanaged
HHA504 / Assignment 5 / Flask and DBs - MySQL

## This repo aims to:
- Deploy a VM using GCP
- Install MySQL onto a GCP VM
- Configure the VM to allow inbound connections
- Upload public dataset via python to a dummy database within MySQL to allow someone to remotely connect and query this database 

<br>

------
# HOW TO SETUP VM AND MYSQL: 
------

# MySQL REQUIREMENTS AND DEPENDENCIES FOR THE INSTANCE 
1. 2 vCPU | 4 GB GAM | 10 GB | Ubuntu 18.04 LTS
2. Allow traffic for: HTTP. HTTPS. SSH, MySQL
3. Create a new firewall rule to enable MySQL traffic (Open port 3306)   
    - Name: mysql-allow
    - Target Tags: All instances in the network
    - Source IP ranges: 0.0.0.0/0
    - Protocols and ports: Check [TCP]: 3306

<br>

# EDITING THE CONFIG FILE TO CHANGE BIND ADDRESSES
1. Go to config file:
    - sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
2. Change **bind address** and **mysqlx-bind-address** from 127.0.0.1 to 0.0.0.0/0
3. Restart mysql server to activate changes:
    - **sudo /etc/init.d/mysql restart**
4. [For Azure VM, add: Inbound security rule
Service: MySQL, which auto-adds port 3306,
Name it: mysql-custom-allow]

<br>

# .SSH TERMINAL SETUP ON GCP
1. sudo apt-get update 
2. sudo apt install mysql-client mysql-server # provides many dbs
3. sudo mysql # connecting to server 
4. Show what databases exist within the server
    - show databases; or show databases \G; # will show what databases are within the server
5. \q to leave the mysql server

<br>

# CREATE A NEW DBA USER (database administrator)
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

<br>

# CREATE A NEW DB IN MYSQL SERVER
1. Log back into mysql server
2. CREATE DATABASE db1;
3. Verify db was created by show all databases using:
    - show databases \G;
4. Change into new db directory to create a table:
    - Use db1

<br>

# CREATE A TABLE WITHIN THE NEW DB
5. Create a new table within the new db1
    -Create table table_name(column1 datatype, column2 datatype, column3 datatype, ...));
     -Create table salarytable(title varchar(255), salary int, year int);
6. Confirm table was created
    - show tables;
7. print(engine.table_names())

<br>

# CONNECTING DB TO MYSQL
- Refer to connectDB.py script

<br> 

# IMPORTING DATA
 1. Refer to **connectDB.py Data section** to push .csv data into a new table (ds_salary_table) within db1
 2. To review data, enter a query into mysql server on GCP:
    - select * from db1.ds_salary_table limit 5;
    - select * from ds_salary_table where employee_residence = 'US';

 - **Data Analyst Salaries Dataset Retreived from Kaggle: https://www.kaggle.com/code/ericktilieri/data-analyst-salaries-eda/data**