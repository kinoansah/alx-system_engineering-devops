#!/bin/bash

# Backup the original /etc/hosts file
sudo cp /etc/hosts /etc/hosts.bak

# Add the new host entries to /etc/hosts
echo "127.0.0.2 localhost" | sudo tee -a /etc/hosts
echo "8.8.8.8   facebook.com" | sudo tee -a /etc/hosts

echo "Configuration completed successfully."
