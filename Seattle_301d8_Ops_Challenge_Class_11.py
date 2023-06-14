# Ops Challenge: Psutil
# Overview
# Python is known for its versatile and diverse selection of libraries. Libraries are installable toolkits that add new functions to the language on your system. Today you will use Psutil to fetch system information.

# Objectives
# Install Psutil.

# Create a Python script that fetches this information using Psutil:

# Time spent by normal processes executing in user mode
# Time spent by processes executing in kernel mode
# Time when system was idle
# Time spent by priority processes executing in user mode
# Time spent waiting for I/O to complete.
# Time spent for servicing hardware interrupts
# Time spent for servicing software interrupts
# Time spent by other operating systems running in a virtualized environment
# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

# START CODE

#!/usr/bin/env python3

import psutil

def get_cpu_times():
    cpu_times = psutil.cpu_times()
    return {
        "user_mode": cpu_times.user,
        "kernel_mode": cpu_times.system,
        "idle_time": cpu_times.idle,
        "priority_user_mode": cpu_times.nice,
        "io_wait": cpu_times.iowait,
        "hardware_interrupts": cpu_times.irq,
        "software_interrupts": cpu_times.softirq,
        "virtual_environment": cpu_times.steal,
        "guest_os": cpu_times.guest
    }

cpu_times = get_cpu_times()

print("Time spent by normal processes executing in user mode:", cpu_times["user_mode"])
print("Time spent by processes executing in kernel mode:", cpu_times["kernel_mode"])
print("Time when system was idle:", cpu_times["idle_time"])
print("Time spent by priority processes executing in user mode:", cpu_times["priority_user_mode"])
print("Time spent waiting for I/O to complete:", cpu_times["io_wait"])
print("Time spent for servicing hardware interrupts:", cpu_times["hardware_interrupts"])
print("Time spent for servicing software interrupts:", cpu_times["software_interrupts"])
print("Time spent by other operating systems running in a virtualized environment:", cpu_times["virtual_environment"])
print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:", cpu_times["guest_os"])
