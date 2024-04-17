#!/bin/bash
# The script will display the disk usage of the system.
disk_usage=$(df -h)
# df command is used to display the disk usage of the system and -h flag is used to display the output in human readable format.
echo "$disk_usage"
# The output of the df command is stored in the variable disk_usage and then displayed on the terminal.
# End of script