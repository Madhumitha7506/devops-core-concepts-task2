#!/bin/bash
echo "Date: $(date)"
echo "User: $(whoami)"
echo "Host: $(hostname)"
echo "Disk usage:"
df -h /
echo "Memory:"
free -h
