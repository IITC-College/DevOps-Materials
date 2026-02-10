#!/bin/bash
# Template showing case statement syntax

read -p "Enter your choice: " CHOICE

case "$CHOICE" in
    option1)
        echo "You chose option 1"
        # Add commands here
        ;;
    option2)
        echo "You chose option 2"
        # Add commands here
        ;;
    *)
        echo "Invalid option"
        exit 1
        ;;
esac
