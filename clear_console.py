# MODULES IMPORT
#Platform import to detect os
import platform
# Importing clearing commands from system
import sys, os

# VARIABLES 
#system = name of os
system = platform.system()
#Command variable for one-line clear exec(cls)
cls = "Not set yet."
######################################
#  SETTING CLS COMMAND

#OS detection
if system == "Windows":
    cls = "os.system('cls')"

elif system == "Linux":
    cls = "os.system('clear')"

else:
    print("No operating system detected, cannot be cls command cannot be set...")

######################################
# EXECUTING CLS
# USE THIS CODE FOR CLEARING CONSOLE:
exec(cls)
