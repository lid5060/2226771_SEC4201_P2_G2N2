#!/bin/bash
echo "Enter the username of the user you would like to add:"  | xargs -I{} ./User Management {}
read -r username
export username
echo "Enter the password of the user you would like to add:"
read -r password
export password
sudo useradd -m -s /bin/bash "$username"
# -m creates a home directory for the user
# -s specifies the shell for the user
echo "$username:$password" | sudo chpasswd
echo "User $username has been added."