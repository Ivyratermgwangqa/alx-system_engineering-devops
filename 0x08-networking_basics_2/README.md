```markdown
# Networking Basics 2

This repository contains Bash scripts that demonstrate networking basics on an Ubuntu 20.04 LTS system.

## Table of Contents

1. [Change Your Home IP](#change-your-home-ip)
2. [Show Attached IPs](#show-attached-ips)
3. [Port Listening on Localhost](#port-listening-on-localhost)

## Change Your Home IP

This script configures an Ubuntu server with specific IP configurations.

### Requirements

- `localhost` should resolve to `127.0.0.2`
- `facebook.com` should resolve to `8.8.8.8`

### Usage

```bash
sudo ./0-change_your_home_IP
```

### Example

Before running the script:

```bash
ping localhost
```

After running the script:

```bash
ping localhost
```

## Show Attached IPs

This script displays all active IPv4 IPs on the machine it's executed on.

### Usage

```bash
./1-show_attached_IPs
```

### Example

```bash
./1-show_attached_IPs | cat -e
```

## Port Listening on Localhost

This advanced script listens on port 98 on localhost, providing a useful tool for debugging network connections.

### Usage

```bash
sudo ./100-port_listening_on_localhost
```

### Example

In one terminal window:

```bash
sudo ./100-port_listening_on_localhost
```

In another terminal window:

```bash
telnet localhost 98
```

Useful for debugging socket connection issues, checking firewall rules, and more.

Feel free to explore, experiment, and have fun with these networking basics scripts!

```
