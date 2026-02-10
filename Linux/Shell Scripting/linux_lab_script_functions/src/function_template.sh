#!/bin/bash
# Template showing function syntax

# Simple function
my_function() {
    echo "This is a function"
}

# Function with parameter
greet_user() {
    echo "Hello, $1!"
}

# Function with multiple parameters
calculate() {
    local RESULT=$(($1 + $2))
    echo $RESULT
}

# Call the functions
my_function
greet_user "DevOps Engineer"
SUM=$(calculate 10 20)
echo "Sum: $SUM"
