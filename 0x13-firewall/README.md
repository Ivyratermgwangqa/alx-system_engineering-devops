# 0x13. Firewall

## Table of Contents
* [Tasks](#tasks)
  * [Task 0: Block all incoming traffic but](#task-0-block-all-incoming-traffic-but)
  * [Task 1: Port forwarding](#task-1-port-forwarding)
* [Additional Notes](#additional-notes)

---

## Tasks

### Task 0: Block all incoming traffic but

#### Description
In this task, we configure the `ufw` firewall on `web-01` to block all incoming traffic except for ports 22 (SSH), 80 (HTTP), and 443 (HTTPS SSL).

#### Solution
```bash
# Install ufw if not already installed
sudo apt-get update
sudo apt-get install ufw

# Set default incoming policy to deny
sudo ufw default deny incoming

# Allow incoming SSH, HTTP, and HTTPS
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Enable ufw
sudo ufw enable
```

### Task 1: Port forwarding

#### Description
In this task, we configure `web-01`'s firewall to redirect port 8080/TCP to port 80/TCP.

#### Solution
```bash
# Edit the ufw configuration file
sudo nano /etc/ufw/before.rules
```

Add the following lines at the beginning of the file:
```
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
```

Save the file and exit the editor. Then reload `ufw`:
```bash
sudo ufw reload
```

Now, port forwarding from 8080/TCP to 80/TCP should be configured on `web-01`.

---

## Additional Notes

Make sure to verify the changes by testing the connectivity and ensuring that the configurations are applied correctly.
