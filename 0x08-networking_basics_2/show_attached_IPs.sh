#!/bin/bash

# Get the active IPv4 IPs using 'ifconfig' and filter the output using 'grep' and awk
ifconfig | grep -oE 'inet (addr:)?([0-9]*\.){3}[0-9)*' | awk '{print $2}'
