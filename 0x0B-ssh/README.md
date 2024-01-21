# SSH Configuration Project
# 0x0B. SSH

This project contains Bash scripts and configurations aimed at managing SSH keys and client settings, providing enhanced security and automation for SSH connections.

## Task 0: Use a Private Key

**Script:** [0-use_a_private_key](0x0B-ssh/0-use_a_private_key)

This script facilitates an SSH connection to a server using the private key `~/.ssh/school` with the user `ubuntu`. It strictly adheres to specific requirements, utilizing single-character flags and handling private key passphrases.

## Task 1: Create an SSH Key Pair

**Script:** [1-create_ssh_key_pair](0x0B-ssh/1-create_ssh_key_pair)

This script generates a robust RSA key pair with the private key named `school` and protects it with a passphrase set to `betty`. Both the private and public keys are saved in the `~/.ssh/` directory.

## Task 2: Client Configuration File

**Script:** [2-ssh_config](0x0B-ssh/2-ssh_config)

This script configures the local SSH client by modifying the `~/.ssh/config` file. It ensures that the private key `~/.ssh/school` is used for authentication and strictly refuses any attempts for password-based authentication.

## Task 3: Let me in!

This task doesn't require a script. Instead, it involves adding a provided SSH public key to the server's authorized keys, allowing secure connections using the `ubuntu` user.

## Task 4: Client Configuration File (w/ Puppet)

**Script:** [100-puppet_ssh_config.pp](0x0B-ssh/100-puppet_ssh_config.pp)

This Puppet script automates the configuration of the SSH client. It makes modifications to the SSH configuration file, ensuring the use of the private key `~/.ssh/school` and explicitly refusing authentication via password.

---

### Instructions for Use:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your_username/alx-system_engineering-devops.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd alx-system_engineering-devops/0x0B-ssh
    ```

3. **Execute the scripts or follow the instructions provided for each task.**

---

Feel free to reach out if you have any questions or concerns! Contributions and feedback are always welcome.
