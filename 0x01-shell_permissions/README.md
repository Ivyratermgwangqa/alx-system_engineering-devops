# Shell Permissions Project

This project focuses on shell scripting in a Linux environment, specifically dealing with file permissions. The tasks involve creating scripts to perform various operations related to user, group, and other file permissions.

## Project Structure

The project directory (`0x01-shell_permissions`) contains the following scripts:

1. **0-iam_betty**
   - Description: Switches the current user to the user `betty`.
   - Usage: `./0-iam_betty`

2. **1-who_am_i**
   - Description: Prints the effective username of the current user.
   - Usage: `./1-who_am_i`

3. **2-groups**
   - Description: Prints all the groups the current user is part of.
   - Usage: `./2-groups`

4. **3-new_owner**
   - Description: Changes the owner of the file `hello` to the user `betty`.
   - Usage: `sudo ./3-new_owner`

5. **4-empty**
   - Description: Creates an empty file called `hello`.
   - Usage: `./4-empty`

6. **5-execute**
   - Description: Adds execute permission to the owner of the file `hello`.
   - Usage: `./5-execute`

7. **6-multiple_permissions**
   - Description: Adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.
   - Usage: `./6-multiple_permissions`

8. **7-everybody**
   - Description: Adds execution permission to the owner, the group owner, and other users, to the file `hello`.
   - Usage: `./7-everybody`

9. **8-James_Bond**
   - Description: Sets specific permissions to the file `hello`.
   - Usage: `./8-James_Bond`

10. **9-John_Doe**
    - Description: Sets the mode of the file `hello` to a specific permission set.
    - Usage: `./9-John_Doe`

11. **10-mirror_permissions**
    - Description: Sets the mode of the file `hello` the same as `olleh`'s mode.
    - Usage: `./10-mirror_permissions`

12. **11-directories_permissions**
    - Description: Adds execute permission to all subdirectories of the current directory for the owner, the group owner, and all other users. Regular files are not changed.
    - Usage: `./11-directories_permissions`

13. **12-directory_permissions**
    - Description: Creates a directory called `my_dir` with permissions `751` in the working directory.
    - Usage: `./12-directory_permissions`

14. **13-change_group**
    - Description: Changes the group owner to `school` for the file `hello`.
    - Usage: `sudo ./13-change_group`

15. **100-change_owner_and_group**
    - Description: Changes the owner to `vincent` and the group owner to `staff` for all files and directories in the working directory.
    - Usage: `sudo ./100-change_owner_and_group`

16. **101-symbolic_link_permissions**
    - Description: Changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively (assuming `_hello` is a symbolic link to `hello`).
    - Usage: `sudo ./101-symbolic_link_permissions`

17. **102-if_only**
    - Description: Changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.
    - Usage: `sudo ./102-if_only`

## Requirements and Restrictions

- **Editors:** vi, vim, emacs
- **Tested on:** Ubuntu 20.04 LTS
- **Script Length:** All scripts should be exactly two lines long (`wc -l file` should print 2)
- **File Ending:** All files should end with a new line.
- **Shebang:** The first line of all files should be `#!/bin/bash`
- **Execution:** All files must be executable
- **Plagiarism:** Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Learning Objectives

By completing this project, you are expected to gain knowledge and practical experience in the following areas:

- Linux file permissions
- Commands: `chmod`, `sudo`, `su`, `chown`, `chgrp`, `id`, `groups`, `whoami`, `adduser`, `useradd`, `addgroup`
- Representation of file permissions as a single digit for owner, group, and other
- Changing permissions, owner, and group of a file
- Running commands with root privileges
- Changing user ID or becoming superuser
