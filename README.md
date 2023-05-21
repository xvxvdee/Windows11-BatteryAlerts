# Windows 11 Battery Alert
This repository contains a Python script that alerts the user when their device’s battery is fully charged. The script can be automated using the task manager to run at regular intervals and check the battery status. This way, the user can be notified when their battery is fully charged without having to constantly check it themselves.
## Usage
 1. Clone this repository to your local machine.
 2. Run the script using a Python interpreter.
 3. (Optional) Set up the script to run at regular intervals using your operating system's task manager.

## Automating Alerts with Windows Task Manager
 1. Open the Windows Task Manager by searching for "Task Scheduler" in the Start menu.
 2. Click on "Create Basic Task" in the right-hand pane.
 3. Follow the prompts to set up a new task that runs the Python script at regular intervals.
 4. When prompted for the program/script, enter the location of pythonw.exe on your system (e.g., C:\Python39\pythonw.exe).
 5. In the "Add arguments" field, enter the location of the Python script (e.g., C:\path\to\battery_alert.py).
 6. When prompted for the trigger, select "On a schedule" and set it to run daily at your desired time.

With this script and the Windows Task Manager, you'll never have to worry about overcharging your device's battery again!
