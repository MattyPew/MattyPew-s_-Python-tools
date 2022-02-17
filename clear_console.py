
# MODULES IMPORT

#Platform import to detect os
import platform
# Importing clearing commands from system
import sys, os
# Sleep function
from time import sleep

# VARIABLES 

#Tested print repeat volume
x = 100
#system = name of os
system = platform.system()
#Command variable for one-line clear (exec(cls))
cls = "Not set yet."

# PRINTING TEST TEXT

#Printing os name "x" times
while x > 0:
    print(system)
    x = (x - 1)
sleep(5)

#  SETTING CLS COMMAND

#OS detection
if system == "Windows":
    cls = "os.system('cls')"

elif system == "Linux":
    cls = "os.system('clear')"

else:
    print("No operating system detected, cannot be cls command cannot be set...")

# EXECUTING CLS

#Executing cls command
exec(cls)
sleep(5)
