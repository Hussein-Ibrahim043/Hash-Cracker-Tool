#!/bin/bash

# Installation Script for Hash Cracker Tool
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root."
    exit
fi

INSTALL_DIR="/usr/local/bin/hashcracker"

echo "Installing Hash Cracker Tool..."
cp hash_cracker.py "$INSTALL_DIR"

chmod +x "$INSTALL_DIR"
echo "alias hashcracker='python3 /usr/local/bin/hashcracker \"\$@\"'" >> ~/.bashrc

# Reload shell configuration
source ~/.bashrc

echo "Installation complete! Use 'hashcracker' followed by arguments to run the tool."
