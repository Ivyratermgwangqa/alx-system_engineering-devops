# Task 0: Simple Web Stack

## Overview

This task involves designing a one-server web infrastructure that hosts a website reachable via www.foobar.com. The infrastructure includes a server, web server (Nginx), application server, application files, and a MySQL database. Additionally, the domain name foobar.com must be configured with a www record pointing to the server IP 8.8.8.8.

## Design on Whiteboard

![Whiteboard Design](<insert_image_url_here>)

## Explanation

### Components:
1. **Server:**
   - A physical or virtual machine responsible for hosting the web infrastructure.

2. **Web Server (Nginx):**
   - Serves as the entry point for incoming HTTP requests.
   - Handles static content and forwards dynamic content requests to the application server.

3. **Application Server:**
   - Executes application logic and processes dynamic content requests.
   - Communicates with the database to fetch or store data.

4. **Application Files:**
   - Your codebase, containing the web application's source code and necessary files.

5. **Database (MySQL):**
   - Stores and manages data for the web application.

6. **Domain Name (foobar.com):**
   - A human-readable identifier for the website.

### Specifics:
- **What is a server?**
  - A physical or virtual machine responsible for hosting and serving web applications.

- **Role of the Domain Name:**
  - Acts as a human-readable identifier for the website.

- **Type of DNS Record for www.foobar.com:**
  - The www record is a CNAME (Canonical Name) record pointing to the server's IP (8.8.8.8).

- **Role of the Web Server (Nginx):**
  - Serves as the entry point for incoming HTTP requests, handling static content and forwarding dynamic content requests.

- **Role of the Application Server:**
  - Executes application logic, processes dynamic content requests, and communicates with the database.

- **Role of the Database (MySQL):**
  - Stores and manages data for the web application.

- **Server Communication:**
  - The server communicates with the user's computer over the HTTP protocol.

### Issues with the Infrastructure:
1. **Single Point of Failure (SPOF):**
   - The entire infrastructure is dependent on a single server, leading to a potential failure if the server goes down.

2. **Downtime During Maintenance:**
   - Performing maintenance, such as deploying new code, requires restarting the web server, leading to downtime.

3. **Scalability Limitations:**
   - The infrastructure cannot easily scale to handle a large volume of incoming traffic.

## Repository

- [GitHub Repository Link](<insert_repository_url_here>)
