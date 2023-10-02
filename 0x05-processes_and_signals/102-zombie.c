#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/sched.h>
#include <linux/unistd.h>

MODULE_LICENSE("GPL");

/**
 * infinite_while - Infinite loop to keep the program running
 * Return: Always 0
 */
int infinite_while(void)
{
    while (1) {
        schedule();
    }
    return 0;
}

static int __init zombie_init(void)
{
    pid_t child_pid;
    int i;

    for (i = 0; i < 5; i++) {
        child_pid = fork();
        if (child_pid < 0) {
            pr_err("Failed to fork\n");
            return -1;
        }
        if (child_pid == 0) {
            pr_info("Zombie process created, PID: %d\n", getpid());
            exit(0);
        }
    }
    return 0;
}

static void __exit zombie_exit(void)
{
    pr_info("Module unloaded\n");
}

module_init(zombie_init);
module_exit(zombie_exit);
