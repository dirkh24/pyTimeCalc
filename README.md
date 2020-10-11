# pyTimeCalc
A tiny little time calculation tool to calculate the time difference between a starting time and an end time.

# The user interface

![alt text](https://github.com/dirkh24/pyTimeCalc/blob/main/images/user_interface.PNG?raw=true)

Description of the user interface
* Starttime: Choose the start time with the combo boxes hour and a minute or get the current time with the button "Current Time"

* Endtime: Choose the end time with the combo boxes hour and a minute or get the current time with the button "Current Time"

* Checkbox Pause: With the checkbox "Pause" you can consider an individual pause

* Button Calc: Start the calculation of the time difference between the starting time and the end time.

# Make a standalone version with pyinstaller

With pyinstaller (https://www.pyinstaller.org/) you kann make a standalone executable for Windows, Mac or Linux. 

First you have to install pyinstaller with `pip install pyinstaller`. 
To make a Windows executable use this command `pyinstaller  -F -w pyTimeCalc.py` in the pyTimeCalc directory.

  
