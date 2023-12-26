# Web Infrastructure Design Project

## Overview

This project is part of the DevOps and SysAdmin track at [AlxSE](https://www.alxafrica.com/). It aims to enhance understanding and practical application of web infrastructure concepts, including DNS, monitoring, web servers, network basics, load balancers, and servers.

## Learning Objectives

- Gain proficiency in designing web infrastructures for various scenarios.
- Develop the ability to explain the role of each component.
- Understand system redundancy and potential issues in web infrastructures.
- Acquire knowledge of acronyms such as LAMP, SPOF, QPS.

## Concepts

### 1. DNS (Domain Name System)

DNS is a fundamental technology translating human-readable domain names to machine-adapted IP addresses. Ensure familiarity with main DNS record types (A, CNAME, MX, TXT), NS Records, SOA Records, and the differences between root domains and subdomains.

### 2. Monitoring

Monitoring is crucial for ensuring software systems' health. Web stack monitoring includes application monitoring (tracking software behavior) and server monitoring (monitoring server resources like CPU, memory, disk, and network). Familiarize yourself with popular monitoring tools like NewRelic, DataDog, Uptime Robot, Nagios, and WaveFront.

### 3. Web Server

Distinguish between a web server and a server. A web server is software delivering web pages, while a server is the actual computer. Understand the role of web servers in serving web pages to clients and explore resources like Nginx and Apache.

### 4. Network Basics

Networking is foundational for communication between machines. Understand key concepts like protocols, IP addresses, TCP/IP, and Internet Protocol (IP) ports.

### 5. Load Balancer

Explore the role of load balancers in distributing web traffic across multiple servers. Learn about load-balancing algorithms and how they contribute to handling large amounts of traffic efficiently.

### 6. Server

Servers, whether physical or virtual, host applications and services. Servers run operating systems and are essential components in web infrastructures. Differentiate between a server and a web server.

## Tasks

### Task 0: Simple Web Stack

#### Design on Whiteboard
1. Sketch a single-server web infrastructure on a whiteboard.
2. Include components such as the server, web server (Nginx), application server, and database.
3. Connect these components to represent the flow of data.

#### Explanations
1. Explain the role of each component.
2. Discuss the issues: SPOF, downtime during maintenance, scalability limitations.

#### Screenshot
- Take a picture/screenshot of your whiteboard design.

#### Repository
- [GitHub Repository Link](<insert_repository_url_here>)

### Task 1: Distributed Web Infrastructure

#### Design on Whiteboard
1. Sketch a three-server web infrastructure with load balancing.
2. Add components such as servers, load balancer (HAproxy), web server, application server, and database.
3. Connect these components to represent the flow of data.

#### Explanations
1. Explain the purpose of each added component.
2. Discuss the issues: SPOF, security issues, no monitoring.

#### Screenshot
- Take a picture/screenshot of your whiteboard design.

#### Repository
- [GitHub Repository Link](<insert_repository_url_here>)

### Task 2: Secured and Monitored Web Infrastructure

#### Design on Whiteboard
1. Sketch a three-server web infrastructure with added security measures and monitoring.
2. Add components such as firewalls, SSL certificate, and monitoring clients.
3. Connect these components to represent the flow of data.

#### Explanations
1. Explain the purpose of each additional element.
2. Discuss the issues: SSL termination, single MySQL server for writes, uniform server components.

#### Screenshot
- Take a picture/screenshot of your whiteboard design.

#### Repository
- [GitHub Repository Link](<insert_repository_url_here>)

### Task 3: Scale Up

#### Design on Whiteboard
1. Sketch an infrastructure for scaling up.
2. Add 1 server and 1 load balancer (HAproxy) configured as a cluster with the other one.
3. Split components (web server, application server, database) with their own server.
4. Connect these components to represent the flow of data.

#### Explanations
1. Explain why each additional element is added to scale up the infrastructure.

#### Screenshot
- Take a picture/screenshot of your whiteboard design.

#### Repository
- [GitHub Repository Link](<>)

## General Requirements

- A README.md file is mandatory at the root of the project folder.
- For each task, whiteboard the design and take a picture/screenshot.
- Upload screenshots to any image hosting service and insert the links in the README.md.
- Push the project to GitHub and provide the repository link.

## Final Steps

1. Review your GitHub repository to ensure completion.
2. Push the final version of your project to GitHub.
3. Request a manual QA review.
4. Prepare for the whiteboarding session with mentors, staff, or students.

## Acknowledgments

This project is part of the curriculum at [alxse](https://www.alxafrica.com/) and is designed to strengthen practical skills in web infrastructure design.
