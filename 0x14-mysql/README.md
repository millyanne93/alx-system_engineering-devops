# **0x14. MySQL**
The MySQL server provides a database management system with querying and connectivity capabilities, as well as the ability to have excellent data structure and integration with many different platforms.
# MySQL Database Management and Setup Guide

## What to Understand
- What is a primary-replica cluster?
- MySQL primary replica setup
- Building a robust database backup strategy

## Learning Objectives
- Understand the main role of a database
- Define a database replica and its purpose
- Explain the importance of storing database backups in different physical locations
- Identify regular operations to ensure the effectiveness of a database backup strategy

## Installation Guide for MySQL 5.7
1. Obtain PGP Public Key
   - Go to dev.mysql.com and copy the PGP PUBLIC KEY.
   - Create a new file with a .key extension and paste the PGP PUBLIC KEY.
2. Add Key to Apt
   - `sudo apt-key add signature.key`
   - `sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C`
3. Add MySQL Repository
   - `sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'`
4. Update Apt Packages
   - `sudo apt-get update`
5. Install MySQL 5.7
   - `sudo apt-cache policy mysql-server`
   - `sudo apt install -f -y mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*`


# MySQL Setup and Replication Configuration

## Project Task: Setting Up MySQL Database and Replication

### Creating a User and Granting Privileges in MySQL

```bash
$ mysql -u root -p
Password: /* Type root password */

mysql> CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

mysql> GRANT GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

mysql> FLUSH PRIVILEGES;

## Creating Database, Tables, and Adding Data

$ mysql -uroot -p

mysql> CREATE DATABASE db_name_;

mysql> USE db_name;

mysql> CREATE TABLE table_name (
    -> col_1 data_type,
    -> col_2 data_type);
    
mysql> INSERT INTO table_name VALUES (val_1, val_2);

## Setting Up MySQL Replication
bash
$ mysql -uroot -p

mysql> CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_user_pwd';

mysql> GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

mysql> FLUSH PRIVILEGES;

-- Edit mysqld.cnf and restart MySQL

$ sudo service mysql restart

-- Lock the database and prepare for replication

mysql> FLUSH TABLES WITH READ LOCK;

mysql> SHOW MASTER STATUS;

-- Export and import the database

$ mysqldump -uroot -p db_name > export_db_name.sql

$ scp -i _identity_file_ export_db_name.sql user@machine_ip:location

$ mysql -uroot -p db_name < export_db_name.sql

-- Configure replication on replica server

$ mysql -uroot -p

mysql> CREATE DATABASE db_name;

mysql> CHANGE MASTER TO
    -> MASTER_HOST='source_host_name',
    -> MASTER_USER='replication_user_name',
    -> MASTER_PASSWORD='replication_password',
    -> MASTER_LOG_FILE='recorded_log_file_name',
    -> MASTER_LOG_POS=recorded_log_position;

mysql> START SLAVE;
