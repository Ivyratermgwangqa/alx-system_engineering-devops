# ALX System Engineering & DevOps - Load Balancer Project

## Task 0: Double the number of webservers

### Script: 0-custom_http_response_header

Description: This script configures Nginx on a new Ubuntu machine to include a custom HTTP header in its response.

Usage:
```bash
./0-custom_http_response_header
```

### Example Output:
```bash
$ curl -sI [web_server_ip] | grep X-Served-By
X-Served-By: [hostname]
```

## Task 1: Install your load balancer

### Script: 1-install_load_balancer

Description: This script installs and configures HAProxy on the lb-01 server to distribute traffic between web-01 and web-02 using a round-robin algorithm.

Usage:
```bash
./1-install_load_balancer
```

### Example Output:
```bash
$ curl -Is [load_balancer_ip]
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
...
X-Served-By: [web_server_hostname]
...

## Task 2: Add a custom HTTP header with Puppet (Advanced)

### Puppet Script: 2-puppet_custom_http_response_header.pp

Description: This Puppet script configures a brand new Ubuntu machine to add a custom HTTP header to the Nginx response.

Usage:
```bash
puppet apply 2-puppet_custom_http_response_header.pp
```

```

Feel free to customize this template based on the specifics of your project.
