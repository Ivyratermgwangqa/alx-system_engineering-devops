### 0-current_working_directory
```bash
#!/bin/bash
pwd
```

### 1-listit
```bash
#!/bin/bash
ls
```

### 2-bring_me_home
```bash
#!/bin/bash
cd
```

### 3-listfiles
```bash
#!/bin/bash
ls -l
```

### 4-listmorefiles
```bash
#!/bin/bash
ls -la
```

### 5-listfilesdigitonly
```bash
#!/bin/bash
ls -lan
```

### 6-firstdirectory
```bash
#!/bin/bash
mkdir /tmp/my_first_directory
```

### 7-movethatfile
```bash
#!/bin/bash
mv /tmp/betty /tmp/my_first_directory
```

### 8-firstdelete
```bash
#!/bin/bash
rm /tmp/my_first_directory/betty
```

### 9-firstdirdeletion
```bash
#!/bin/bash
rmdir /tmp/my_first_directory
```

### 10-back
```bash
#!/bin/bash
cd -
```

### 11-lists
```bash
#!/bin/bash
ls -la . .. /boot
```

### 12-file_type
```bash
#!/bin/bash
file /tmp/iamafile
```

### 13-symbolic_link
```bash
#!/bin/bash
ln -s /bin/ls __ls__
```

### 14-copy_html
```bash
#!/bin/bash
cp *.html ..
```

### 100-lets_move
```bash
#!/bin/bash
mv [A-Z]* /tmp/u
```

### 101-clean_emacs
```bash
#!/bin/bash
rm *~
```

### 102-tree
```bash
#!/bin/bash
mkdir welcome welcome/to welcome/to/school
```

### 103-commas
```bash
#!/bin/bash
ls -m -p -a | sed ':a;N;$!ba;s/\n/, /g'
```

### school.mgc
```
0	string	SCHOOL	School data
```

#### Sample README.md
```markdown
# Shell Basics Project

This repository contains shell scripts written to fulfill specific tasks and objectives related to understanding shell commands and navigation.

## Scripts Overview

1. **0-current_working_directory**
   - Prints the absolute path name of the current working directory.

2. **1-listit**
   - Displays the contents list of the current directory.

3. **2-bring_me_home**
   - Changes the working directory to the user's home directory.

4. **3-listfiles**
   - Displays current directory contents in a long format.

5. **4-listmorefiles**
   - Displays current directory contents, including hidden files, in long format.

...

## How to Use

1. Clone the repository.
2. Navigate to the desired script.
3. Run the script using `./script_name`.

Feel free to explore and learn from these scripts!
```
