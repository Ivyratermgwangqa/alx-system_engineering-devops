# MySQL Configuration and Backup Project

This project involves setting up MySQL servers, configuring replication between them, and creating a backup script for MySQL databases.

## Table of Contents

- [Introduction](#introduction)
- [Tasks](#tasks)
  - [Task 0: Install MySQL](#task-0-install-mysql)
  - [Task 1: Create MySQL User](#task-1-create-mysql-user)
  - [Task 2: Create Database and Table](#task-2-create-database-and-table)
  - [Task 3: Create Replica User](#task-3-create-replica-user)
  - [Task 4: Setup Primary-Replica Infrastructure](#task-4-setup-primary-replica-infrastructure)
  - [Task 5: MySQL Backup](#task-5-mysql-backup)

## Introduction

This project involves configuring MySQL servers for replication and setting up a backup solution for MySQL databases. The tasks cover installation, user management, database setup, replication configuration, and backup script creation.

## Tasks

### Task 0: Install MySQL

First, MySQL 5.7.x must be installed on both web-01 and web-02 servers. This task ensures that MySQL is correctly installed and verified.

### Task 1: Create MySQL User

A MySQL user named holberton_user must be created on both web-01 and web-02 servers with specific permissions for replication status checking.

### Task 2: Create Database and Table

This task involves creating a database named tyrell_corp on the web-01 server and setting up a table named nexus6 with at least one entry. Permissions are granted to holberton_user for table access.

### Task 3: Create Replica User

A new MySQL user named replica_user must be created on the web-01 server with appropriate permissions for replication.

### Task 4: Setup Primary-Replica Infrastructure

Configuration of primary and replica MySQL servers is performed in this task. Replication between the servers is established, and its functionality is verified.

### Task 5: MySQL Backup

A Bash script is created to generate a MySQL dump containing all databases, compressing it into a tar.gz archive with a specific naming format. This backup solution ensures data redundancy and disaster recovery.

Each task directory contains scripts and configuration files necessary to complete the respective task.
