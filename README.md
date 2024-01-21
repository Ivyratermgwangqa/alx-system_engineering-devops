# SSH Configuration Project
# 0x0B. SSH

This project includes Bash scripts and configurations to manage SSH keys and client configurations. The tasks aim to enhance security and automate SSH connections.

## Task 0: Use a Private Key

Script: [0-use_a_private_key](0x0B-ssh/0-use_a_private_key)

This script uses SSH to connect to a server using the private key `~/.ssh/school` with the user `ubuntu`. It adheres to specific requirements regarding single-character flags and handling private key passphrase.

## Task 1: Create an SSH Key Pair

Script: [1-create_ssh_key_pair](0x0B-ssh/1-create_ssh_key_pair)

This script generates an RSA key pair with the private key named `school` and a passphrase set to `betty`. The key pair is saved in the `~/.ssh/` directory.

## Task 2: Client Configuration File

Script: [2-ssh_config](0x0B-ssh/2-ssh_config)

This script configures the local SSH client using the `~/.ssh/config` file. It sets the private key to `~/.ssh/school` and refuses authentication using a password.

## Task 3: Let me in!

No script is needed for this task. It involves adding a provided SSH public key to the server's authorized keys, allowing connection with the `ubuntu` user.

## Task 4: Client Configuration File (w/ Puppet)

Script: [100-puppet_ssh_config.pp](0x0B-ssh/100-puppet_ssh_config.pp)

This Puppet script automates the configuration of the SSH client. It modifies the SSH configuration file to use the private key `~/.ssh/school` and refuse password authentication.

---

### Instructions for Use:

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/alx-system_engineering-devops.git
    ```

2. Navigate to the project directory:

    ```bash
    cd alx-system_engineering-devops/0x0B-ssh
    ```

3. Execute the scripts or follow the instructions provided for each task.

---

Feel free to reach out if you have any questions or concerns!

