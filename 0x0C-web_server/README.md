# 0x0C-web_server

This repository contains scripts and configurations related to web server setup tasks.

## Table of Contents

- [Tasks](#tasks)
  - [Task 0: Transfer a File](#0-transfer-a-file)
  - [Task 1: Install Nginx Web Server](#1-install-nginx-web-server)
  - [Task 2: Setup a Domain Name](#2-setup-a-domain-name)
  - [Task 3: Redirection](#3-redirection)
  - [Task 4: Not Found Page 404](#4-not-found-page-404)
  - [Task 5: Install Nginx Web Server (w/ Puppet)](#5-install-nginx-web-server-w-puppet)

## Tasks

### 0. Transfer a File

Write a Bash script that transfers a file from a client to a server using SCP.

#### Requirements:

- Accepts 4 parameters:
  - The path to the file to be transferred
  - The IP of the server
  - The username for SCP
  - The path to the SSH private key for SCP
- Display Usage if less than 3 parameters are passed
- SCP must transfer the file to the user's home directory
- Strict host key checking must be disabled
- Example:

```bash
./0-transfer_file some_file.txt 8.8.8.8 username /path/to/private_key
```

### 1. Install Nginx Web Server

Write a Bash script that installs Nginx on a server and configures it to listen on port 80. When querying Nginx at its root with a GET request, it must return a page containing the string "Hello World!"

#### Requirements:

- Install Nginx on the server
- Nginx should be listening on port 80
- When querying Nginx at its root with a GET request, it must return a page containing "Hello World!"
- The script should be run on the server itself
- Cannot use systemctl for restarting Nginx
- Example:

```bash
./1-install_nginx_web_server
```

### 2. Setup a Domain Name

Register a free .tech domain and configure DNS records to point the root domain to the web server's IP address.

#### Requirements:

- Provide the domain name (e.g., myschool.tech)
- Configure DNS records with an A entry to point the root domain to the web server's IP address
- Propagate DNS records (may take 1-2 hours)
- Example:

```bash
./2-setup_a_domain_name
```

### 3. Redirection

Configure the Nginx server to redirect requests to "/redirect_me" to another page using a 301 Moved Permanently redirect.

#### Requirements:

- Use `sed` to replace a line with multiple lines
- Configure Nginx to redirect "/redirect_me" to another page with a 301 redirect
- Script should automatically configure a new Ubuntu machine
- Example:

```bash
curl -sI 34.198.248.145/redirect_me/
```

### 4. Not Found Page 404

Configure Nginx to have a custom 404 page that returns an HTTP 404 error code and contains the string "Ceci n'est pas une page."

#### Requirements:

- Configure Nginx to return HTTP 404 error for non-existent pages
- Custom 404 page should contain the string "Ceci n'est pas une page"
- Script should automatically configure a new Ubuntu machine
- Example:

```bash
curl 34.198.248.145/xyz
```

### 5. Install Nginx Web Server (w/ Puppet)

Use Puppet to install and configure Nginx on a server. Also, include resources in the manifest to perform a 301 redirect for "/redirect_me".

#### Requirements:

- Nginx should be listening on port 80
- When querying Nginx at its root with a GET request, it must return a page containing "Hello World!"
- The redirection must be a 301 Moved Permanently
- Puppet manifest should automatically configure an Ubuntu machine
- Example:

```bash
puppet apply 7-puppet_install_nginx_web_server.pp
```

Feel free to adjust and expand the README.md based on your specific project requirements and additional details you want to provide.
