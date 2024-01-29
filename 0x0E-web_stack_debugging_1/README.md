# 0x0E-web_stack_debugging_1

This repository contains Bash scripts for debugging and configuring Nginx on Ubuntu 20.04 LTS.

## Task 0: Nginx likes port 80

### Description
Using debugging skills, the task is to find out what's preventing the Nginx installation from listening on port 80 and create a Bash script to automate the fix.

### Requirements
- Nginx must be running and listening on port 80 of all the server's active IPv4 IPs.
- The Bash script should pass Shellcheck without any error.
- The script should run without errors.

### Script
[0-nginx_likes_port_80](0x0E-web_stack_debugging_1/0-nginx_likes_port_80)

## Task 1: Make it sweet and short

### Description
Build a concise Bash script to fix and configure Nginx within 5 lines or less.

### Requirements
- The Bash script must be 5 lines long or less.
- The service (init) must indicate that Nginx is not running.

### Script
[1-debugging_made_short](0x0E-web_stack_debugging_1/1-debugging_made_short)

## General Requirements
- Allowed editors: vi, vim, emacs.
- Files interpreted on Ubuntu 20.04 LTS.
- All files end with a new line.
- README.md file at the root is mandatory.
- Bash script files must be executable.
- Bash scripts must pass Shellcheck without errors.
- First line of Bash scripts: `#!/usr/bin/env bash`.
- Second line of Bash scripts: A comment explaining the script.
