# Web Stack Debugging #2

This project is focused on debugging and configuring a web stack. The tasks involve running software as another user, ensuring Nginx runs as the nginx user, and providing a concise fix for the configuration.

## Tasks

### Task 0: Run software as another user

In this task, we created a Bash script (`0-iamsomeoneelse`) that accepts a username as an argument and runs the `whoami` command under that user.

### Task 1: Run Nginx as Nginx

For this task, a Bash script (`1-run_nginx_as_nginx`) was created to configure Nginx to run as the `nginx` user. The script modifies the Nginx configuration file to specify the user as `nginx` and then starts Nginx.

### Task 2: 7 lines or less

This task required providing a more concise version of the script from Task 1. The Bash script (`100-fix_in_7_lines_or_less`) accomplishes the same goal of configuring Nginx to run as `nginx`, but in 7 lines or less.

## Directory Structure

```
0x12-web_stack_debugging_2/
│
├── 0-iamsomeoneelse
├── 1-run_nginx_as_nginx
└── 100-fix_in_7_lines_or_less
│
└── README.md
```

## Usage

Ensure that the Bash scripts are executable before running:

```bash
chmod +x 0-iamsomeoneelse 1-run_nginx_as_nginx 100-fix_in_7_lines_or_less
```

Execute the scripts with appropriate permissions:

```bash
./0-iamsomeoneelse <username>
./1-run_nginx_as_nginx
./100-fix_in_7_lines_or_less
```

## Author
Lerato Mgwangqa.
