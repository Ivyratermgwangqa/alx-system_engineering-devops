# Project Title: HTTPS SSL Configuration

## Overview

This project focuses on configuring HTTPS SSL for a website, ensuring secure communication and proper handling of SSL termination using HAProxy. The tasks include configuring subdomains, setting up SSL termination, and enforcing HTTPS traffic.

## Tasks

### Task 0: World Wide Web

- **Description:**
  - Configure domain zone for subdomains www, lb-01, web-01, and web-02.
  - Bash script that accepts a domain name and subdomain (optional).
  - Output information about specified subdomain or default subdomains.

- **Script:**
  - `0x10-https_ssl/0-world_wide_web`

### Task 1: HAProxy SSL Termination

- **Description:**
  - Create a certificate using certbot.
  - Configure HAProxy to handle encrypted traffic on port TCP 443.
  - HAProxy must serve encrypted traffic returning the root of your web server with Holberton School.

- **Script:**
  - `0x10-https_ssl/1-haproxy_ssl_termination`

### Task 2: No Loophole in Your Website Traffic

- **Description:**
  - Enforce HTTPS traffic by configuring HAProxy to automatically redirect HTTP traffic to HTTPS.
  - HAProxy should return a 301 for HTTP requests.

- **Script:**
  - `0x10-https_ssl/100-redirect_http_to_https`

## Usage

1. Clone the repository.
2. Execute the scripts using appropriate permissions.

```bash
chmod +x script_name.sh
./script_name.sh
```

## Resources

- [Link to Certbot documentation]
- [Link to HAProxy SSL termination guide]
- [Additional resources as needed]

## Author

[Your Name]

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.
```
