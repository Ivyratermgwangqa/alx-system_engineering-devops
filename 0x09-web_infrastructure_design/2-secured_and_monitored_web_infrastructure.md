# Task 2: Secured and Monitored Web Infrastructure

## Overview

This task involves designing a three-server web infrastructure that hosts the website www.foobar.com. The infrastructure must be secured, serve encrypted traffic over HTTPS, and be actively monitored.

## Design on Whiteboard

![Whiteboard Design](<https://raw.githubusercontent.com/Ivyratermgwangqa/alx-system_engineering-devops/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png>)

## Explanation

### Components:
1. **Firewalls (3):**
   - Deployed to enhance security by controlling and monitoring incoming and outgoing network traffic.

2. **SSL Certificate:**
   - Implemented to enable HTTPS and secure the communication between the user and the website.

3. **Monitoring Clients (3):**
   - Utilized for active monitoring of the infrastructure to identify issues and ensure optimal performance.

### Specifics:
- **Additional Elements:**
  - Firewalls are added for enhanced security.
  - An SSL certificate is introduced for secure, encrypted communication.
  - Monitoring clients are deployed for real-time infrastructure monitoring.

- **Purpose of Each Added Component:**
  - Firewalls control and monitor network traffic, preventing unauthorized access.
  - SSL certificates secure the data exchanged between the user and the website.
  - Monitoring clients actively collect data to identify and address potential issues promptly.

- **Issues with the Infrastructure:**
  1. **SSL Termination at Load Balancer:**
      - Terminating SSL at the load balancer can expose decrypted traffic between the load balancer and the web servers, posing a security risk.

  2. **Single MySQL Server for Writes:**
      - Having only one MySQL server capable of accepting writes poses a single point of failure for write operations.

  3. **Identical Server Components:**
      - Deploying servers with identical components may lead to uniform vulnerabilities and a lack of diversity, potentially causing widespread issues.

## Repository

- [Repo](<https://github.com/Ivyratermgwangqa/alx-system_engineering-devops.git>)
