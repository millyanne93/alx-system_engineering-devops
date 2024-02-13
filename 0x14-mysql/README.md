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
