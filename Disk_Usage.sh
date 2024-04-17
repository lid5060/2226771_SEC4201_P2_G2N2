#!/bin/bash
# Description: This script will display the disk usage of the system.
disk_usage=$(df -h)
echo "$disk_usage"
