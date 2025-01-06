### Disclaimer
# This tool is intended for educational purposes and ethical security testing only.
# Unauthorized use of this tool is prohibited.

#!/bin/bash

# Define the alias name and command
ALIAS_NAME="hashcrack"
ALIAS_COMMAND="python3 $(pwd)/hash_cracker.py"

# File to add the alias
ZSHRC_FILE="$HOME/.zshrc"

# Path to the requirements file
REQUIREMENTS_FILE="$(pwd)/requirements.txt"

# Check if alias already exists
if grep -Fxq "alias $ALIAS_NAME=\"$ALIAS_COMMAND\"" "$ZSHRC_FILE"; then
    echo "Alias '$ALIAS_NAME' already exists in $ZSHRC_FILE."
else
    # Add alias to .zshrc
    echo "alias $ALIAS_NAME=\"$ALIAS_COMMAND\"" >> "$ZSHRC_FILE"
    echo "Alias '$ALIAS_NAME' added to $ZSHRC_FILE."
fi

# Reload .zshrc to apply changes
if [ -n "$ZSH_VERSION" ]; then
    source "$ZSHRC_FILE"
    echo "$ZSHRC_FILE reloaded. You can now use '$ALIAS_NAME' as a command."
else
    echo "Please reload your shell to apply the alias."
fi

# Check for requirements.txt and install dependencies
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Found requirements.txt. Installing dependencies..."
    pip install --quiet -r "$REQUIREMENTS_FILE"
    if [ $? -eq 0 ]; then
        echo "Dependencies installed successfully."
    else
        echo "Some dependencies might already be installed or there was an issue. Please check the requirements.txt file."
    fi
else
    echo "No requirements.txt file found. Skipping dependency installation."
fi
