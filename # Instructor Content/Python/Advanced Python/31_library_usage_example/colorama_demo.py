#!/usr/bin/env python3
# Demonstrating colorama library for colored terminal output

"""
colorama - Cross-platform colored terminal text

INSTALLATION:
  pip install colorama

USAGE:
  from colorama import Fore, Back, Style, init
  init()  # Initialize colorama
"""

try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    
    # Foreground colors
    print(Fore.RED + "This is red text")
    print(Fore.GREEN + "This is green text")
    print(Fore.YELLOW + "This is yellow text")
    print(Fore.BLUE + "This is blue text")
    print(Fore.MAGENTA + "This is magenta text")
    print(Fore.CYAN + "This is cyan text")
    print(Fore.WHITE + "This is white text")
    
    # Background colors
    print(Back.RED + "Red background")
    print(Back.GREEN + "Green background")
    print(Back.YELLOW + "Yellow background")
    
    # Styles
    print(Style.DIM + "Dim text")
    print(Style.NORMAL + "Normal text")
    print(Style.BRIGHT + "Bright text")
    
    # Combined
    print(Fore.GREEN + Back.BLACK + "Green text on black background")
    print(Fore.RED + Style.BRIGHT + "Bright red text")
    
    # Reset
    print(Style.RESET_ALL + "Back to normal")
    
    # Practical example
    print(Fore.GREEN + "[SUCCESS]" + Style.RESET_ALL + " Operation completed")
    print(Fore.RED + "[ERROR]" + Style.RESET_ALL + " Something went wrong")
    print(Fore.YELLOW + "[WARNING]" + Style.RESET_ALL + " Check your input")
    print(Fore.CYAN + "[INFO]" + Style.RESET_ALL + " Processing data")

except ImportError:
    print("colorama is not installed")
    print("Install with: pip install colorama")
