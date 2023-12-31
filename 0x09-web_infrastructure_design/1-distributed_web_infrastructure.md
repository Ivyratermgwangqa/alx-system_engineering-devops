# Task 1: Distributed Web Infrastructure

## Overview

This task involves designing a three-server web infrastructure that hosts the website www.foobar.com. The infrastructure includes two servers, a load balancer (HAproxy), a web server (Nginx), an application server, a MySQL database, and a set of application files.

## Design on Whiteboard

![Whiteboard Design](<https://raw.githubusercontent.com/Ivyratermgwangqa/alx-system_engineering-devops/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png>)

## Explanation

### Components:
1. **Servers (2):**
   - Two physical or virtual machines to distribute the load and improve redundancy.

2. **Load Balancer (HAproxy):**
   - Balances incoming web traffic across multiple servers for improved performance and reliability.

3. **Web Server (Nginx):**
   - Serves as the entry point for incoming HTTP requests.
   - Handles static content and forwards dynamic content requests to the application server.

4. **Application Server:**
   - Executes application logic and processes dynamic content requests.
   - Communicates with the database to fetch or store data.

5. **MySQL Database:**
   - Stores and manages data for the web application.

6. **Application Files:**
   - Your codebase containing the application logic.

### Specifics:
- **Additional Elements:**
  - Two servers are added for load distribution and improved redundancy.
  - The load balancer (HAproxy) is introduced to evenly distribute web traffic among the servers.

- **Purpose of Each Added Component:**
  - The additional servers enhance performance, and the load balancer distributes incoming requests for improved reliability.
  - Application files contain the logic for the web application.

- **Load Balancer Configuration:**
  - The load balancer is configured with a round-robin algorithm to distribute traffic evenly.

- **Active-Active or Active-Passive Setup:**
  - The load balancer enables an Active-Active setup, where both servers actively handle incoming requests.

- **Database Primary-Replica (Master-Slave) Cluster:**
  - The MySQL database is configured as a Primary-Replica (Master-Slave) cluster for data redundancy.

- **Difference Between Primary and Replica Nodes:**
  - The Primary node handles write operations, while the Replica nodes replicate the data for read operations.

### Issues with the Infrastructure:
1. **Single Point of Failure (SPOF):**
   - While redundancy is improved, the load balancer remains a potential single point of failure.

2. **Security Issues:**
   - The infrastructure lacks firewall configurations, exposing it to potential security threats.

3. **No Monitoring:**
   - Monitoring tools are not implemented, making it challenging to identify and address issues promptly.

## Repository

- [Repo](<https://github.com/Ivyratermgwangqa/alx-system_engineering-devops.git>)
