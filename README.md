# Automated Network Configuration Backup

Automated Network Configuration Backup is a Python-based tool designed to connect to Cisco network devices and automatically extract their running configurations. The system dynamically retrieves the device's hostname prompt, executes configuration commands via SSH, and securely saves the output to local text files. It features error handling and is built to easily scale from a single router to a large list of network devices.

## TECH STACK
- Python
- Netmiko

## SETUP
- Clone this repository to your local machine.
- Install the required python dependencies
- Open backup.py and update the devices list with your target router credentials

## HOW TO USE
- Run the script.
- The terminal will display the connection progress and catch any connection errors without crashing.
- Upon successful connection, the extracted running configuration will be printed in the terminal.
- A new .txt file will be automatically generated in the project's root directory containing the backup data.
