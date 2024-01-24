# Web Stack Debugging #0

## Overview

This project involves debugging and fixing issues within a Docker container running an Apache web server. The goal is to make Apache return a page containing "Hello Holberton" when querying the root of the server.

## Task Description

### Script: `0-give_me_a_page`

This Bash script is designed to fix the Apache configuration in a Docker container. It ensures that Apache is installed, started, and configured to return a simple HTML page with the content "Hello Holberton."

### Usage

1. Run the Docker container:

   ```bash
   docker run -p 8080:80 -d -it holbertonschool/265-0
   ```

2. Execute the script inside the Docker container:

   ```bash
   docker exec -ti <CONTAINER_ID> /path/to/0-give_me_a_page
   ```

   Replace `<CONTAINER_ID>` with the actual ID of your running Docker container.

3. Test the result by curling the port 8080:

   ```bash
   curl 0:8080
   ```

   This should return a page containing "Hello Holberton."

### Requirements

- This script is intended for Ubuntu 14.04 LTS.
- Ensure that the script is executable: `chmod +x 0-give_me_a_page`.
- The script should pass Shellcheck without any errors.

## Notes

- The script includes commands to install Apache if not already installed.
- It creates a simple HTML page with the content "Hello Holberton" in the default web directory.
- Apache is restarted to apply the changes.

## Resources

- [Docker](https://www.docker.com/)
- [Apache HTTP Server](https://httpd.apache.org/)

## Author
 
[Ivyratermgwangqa]
