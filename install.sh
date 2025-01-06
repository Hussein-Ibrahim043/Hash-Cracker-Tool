### **Disclaimer**
This tool is intended for educational purposes and ethical security testing only. Unauthorized use of this tool is prohibited.
---

### **install.sh**

Here’s the `install.sh` script for creating an alias:

```bash
#!/bin/bash

# Installation Script for Hash Cracker Tool

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root."
    exit
fi

# Define installation path
INSTALL_DIR="/usr/local/bin/hashcracker"

# Move the main script to the installation path
echo "Installing Hash Cracker Tool..."
cp hash_cracker.py "$INSTALL_DIR"

# Make the script executable
chmod +x "$INSTALL_DIR"

# Create an alias
echo "alias hashcracker='python3 /usr/local/bin/hashcracker'" >> ~/.bashrc

# Reload shell configuration
source ~/.bashrc

echo "Installation complete! Use 'hashcracker' to run the tool."
