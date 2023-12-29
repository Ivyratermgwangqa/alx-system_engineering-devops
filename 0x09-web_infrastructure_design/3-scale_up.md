# Task 3: Scale Up

## Overview

This task involves scaling up the web infrastructure by introducing a dedicated server for each component - web server, application server, and database. Additionally, a load balancer (HAproxy) is configured as a cluster to efficiently distribute incoming traffic.

## Design on Whiteboard

![Whiteboard Design](<insert_image_url_here>)

## Explanation

### Components:
1. **Server (1):**
   - Dedicated server for hosting a specific component.

2. **Load Balancer (HAproxy):**
   - Configured as a cluster to distribute incoming traffic efficiently.

3. **Web Server:**
   - Serves static content and handles HTTP requests.

4. **Application Server:**
   - Executes application logic and processes dynamic content requests.

5. **Database Server:**
   - Stores and manages data for the web application.

### Specifics:
- **Additional Elements:**
  - Each component (web server, application server, database) now has its dedicated server, allowing for better resource utilization and scalability.
  - The load balancer is configured as a cluster to enhance reliability and handle increased traffic.

- **Purpose of Each Added Component:**
  - Dedicated servers for each component ensure efficient resource usage and easier scalability.
  - A load balancer cluster improves redundancy and ensures continuous operation even if one load balancer fails.

## Repository

- [Repo](<https://github.com/Ivyratermgwangqa/alx-system_engineering-devops.git>)
