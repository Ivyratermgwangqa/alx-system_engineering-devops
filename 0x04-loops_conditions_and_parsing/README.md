# DevOps - System Engineering

This repository contains completed Bash scripts for various system engineering tasks and exercises, focusing on loops, conditions, and log parsing.

## Table of Contents

1. [SSH RSA Key Pair](#ssh-rsa-key-pair)
2. [Looping Bash Scripts](#looping-bash-scripts)
3. [Apache Log Parsing](#apache-log-parsing)
4. [Advanced Scripting](#advanced-scripting)

---

## SSH RSA Key Pair

### Task 0

Generate an SSH RSA key pair and share the public key.

- Run `ssh-keygen` to generate the key pair.
- Share the public key in the file `0-RSA_public_key.pub`.
- Fill the SSH public key field of your intranet profile.

[Link to Task 0 Solution](0x04-loops_conditions_and_parsing/0-RSA_public_key.pub)

---

## Looping Bash Scripts

### Task 1

Write a Bash script that displays "Best School" 10 times using a `for` loop.

- Script: [1-for_best_school](0x04-loops_conditions_and_parsing/1-for_best_school)

### Task 2

Write a Bash script that displays "Best School" 10 times using a `while` loop.

- Script: [2-while_best_school](0x04-loops_conditions_and_parsing/2-while_best_school)

### Task 3

Write a Bash script that displays "Best School" 10 times using an `until` loop.

- Script: [3-until_best_school](0x04-loops_conditions_and_parsing/3-until_best_school)

### Task 4

Write a Bash script that displays "Best School" 10 times, but on the 9th iteration, displays "Hi" on a new line.

- Script: [4-if_9_say_hi](0x04-loops_conditions_and_parsing/4-if_9_say_hi)

### Task 5

Write a Bash script that loops from 1 to 10:
- Displays "bad luck" for the 4th iteration
- Displays "good luck" for the 8th iteration
- Displays "Best School" for other iterations

- Script: [5-4_bad_luck_8_is_your_chance](0x04-loops_conditions_and_parsing/5-4_bad_luck_8_is_your_chance)

### Task 6

Write a Bash script that displays numbers from 1 to 20:
- Displays "bad luck from China" for the 4th iteration
- Displays "bad luck from Japan" for the 9th iteration
- Displays "bad luck from Italy" for the 17th iteration

- Script: [6-superstitious_numbers](0x04-loops_conditions_and_parsing/6-superstitious_numbers)

### Task 7

Write a Bash script that displays the time in a 12-hour format with a greeting message.

- Script: [7-clock](0x04-loops_conditions_and_parsing/7-clock)

### Task 8

Write a Bash script that lists files and directories in the current directory using a `for` loop and displays only the part of the name after the first dash.

- Script: [8-for_ls](0x04-loops_conditions_and_parsing/8-for_ls)

### Task 9

Write a Bash script that gives information about the "school" file.

- Script: [9-to_file_or_not_to_file](0x04-loops_conditions_and_parsing/9-to_file_or_not_to_file)

### Task 10

Write a Bash script that displays numbers from 1 to 100:
- Displays "FizzBuzz" for multiples of 3 and 5
- Displays "Fizz" for multiples of 3
- Displays "Buzz" for multiples of 5
- Otherwise, displays the number

- Script: [10-fizzbuzz](0x04-loops_conditions_and_parsing/10-fizzbuzz)

### Task 11

Write a Bash script that displays information about users from the `/etc/passwd` file.

- Script: [100-read_and_cut](0x04-loops_conditions_and_parsing/100-read_and_cut)

### Task 12

Write a Bash script that tells a story about users based on the `/etc/passwd` file.

- Script: [101-tell_the_story_of_passwd](0x04-loops_conditions_and_parsing/101-tell_the_story_of_passwd)

---

## Apache Log Parsing

### Task 13

Write a Bash script that parses Apache logs and displays the visitor IP along with the HTTP status code.

- Script: [102-lets_parse_apache_logs](0x04-loops_conditions_and_parsing/102-lets_parse_apache_logs)

### Task 14

Write a Bash script that groups visitors by IP and HTTP status code, displaying the occurrence number, IP, and HTTP code.

- Script: [103-dig_the-data](0x04-loops_conditions_and_parsing/103-dig_the-data)

---

## Advanced Scripting

Explore advanced scripting exercises within this section.

---

Feel free to explore and use these scripts for learning and reference!
