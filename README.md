# Folder-Monitoring-Script

# Objective

The objective of the script is to monitor a specific folder and detect files with the string **‘content-banned’** in their name. It watches for the following events:

**Created**: When a new file with 'content-banned' in the name is added to the folder.
**Renamed**: When an existing file with 'content-banned' in the name is renamed within the folder.
**Removed**: When a file with 'content-banned' in the name is deleted from the folder.

For each of these events (created, renamed, or removed), the script prints a corresponding message to the screen.

# Key Features:

- The script continuously monitors the folder for any changes.
- It tracks created, renamed, and removed files.
- The script uses a polling mechanism (checks periodically) to detect changes.
- It is designed to be portable and should work in a basic Linux/Unix environment.

# Minimal Requirements

**Event Detection**: The script checks for the three specified events (created, renamed, removed) and prints corresponding messages to the screen when they occur.

**Portability**: 

- The script is written in Python, which is commonly available on Linux/Unix systems.
- It uses basic Python modules (os, sys, time), making it portable without any external dependencies.
- The script runs on a vanilla Linux/Unix environment and doesn't require network connectivity, ensuring it works in offline scenarios.

**Execution and Compilation**:

Python is a widely supported language and does not require compilation. The script is executed directly with the python interpreter.
It assumes Python 3.x, which is available on most modern Linux/Unix distributions.

# How It Works

- **Startup**: The script checks the folder on startup and identifies any existing files with content-banned in their names.
- **Polling**: It continuously polls the folder at a configurable interval (default is 1 second) to check for changes (file creation, renaming, or removal).
- **Event Handling**: For each event (created, renamed, removed), the script prints a message to the screen indicating which file was affected.
- **User Input**: The script prompts the user to input a valid folder path, ensuring that the path exists before starting the monitoring process.

# How to Run the Script

- Ensure Python 3.x is Installed:

The script is written in Python 3.x, so ensure that Python 3 is installed on your system.
You can check if Python 3 is installed by running the following command:

**python3 --version**

- Make the Script Executable (Optional):

**chmod +x script-v8.py**

- Run the Script:

To run the script, use the following command:

**python3 folder-monitoring-script.py**

Upon running the script, you will be prompted to enter the full path of the folder you want to monitor.

- Enter the full path of the folder to monitor: /path/to/your/folder

The script will print messages to the screen when a file with content-banned in its name is created, renamed, or removed.
Example output:

Monitoring folder: /path/to/your/folder
Polling interval: 1 second(s)

Found during startup: content-banned-file1.txt  
Created: content-banned-file2.txt  
Renamed: content-banned-file1.txt -> content-banned-file1-renamed.txt  
Removed: content-banned-file3.txt  

- Stop the Script:    

To stop the script, press Ctrl + C. This will halt the monitoring process.

# Evaluation Criteria

The following criteria were considered while developing this script:

- **Algorithm**: The script efficiently monitors the folder by tracking files based on their inode numbers, which ensures accurate detection of renamed files. It uses a polling mechanism to detect changes and minimize resource usage.

- **Portability**: The script is designed to run on any vanilla Linux/Unix system without requiring additional dependencies. It uses Python 3, which is commonly available on most systems, and the code avoids relying on external network connectivity.

- **User Friendliness**: The script prompts the user for input (folder path), provides clear error messages for invalid input, and offers helpful information, such as the polling interval and events detected. It also provides an easy way to stop monitoring (via Ctrl+C).

- **Maintainability**: The code is modular, with functions like monitor_folder that encapsulate the monitoring logic. It is designed to be easily extensible, with variables like POLLING_INTERVAL exposed for reconfiguration.

- **Readability**: The script is well-organized, with clear function names and comments explaining the core logic, making it easy to read and understand.

- **Scalability**: The script can easily be extended to handle additional file operations or support multiple folders. The polling interval can also be adjusted to balance performance and responsiveness.

- **Usability**: The script is designed to be simple and intuitive to use. The user only needs to provide a folder path, and the script takes care of monitoring the directory and detecting relevant file events (created, renamed, removed).

# Future Improvements

Here’s a summary of future improvements:

- **Logging**: The script could log events to a file, allowing for persistent records with timestamps.

- **Email/Notification Alerts**: The script could send email or system notifications when file events occur.

- **Multiple Directory Support**: The script could monitor multiple directories, either by accepting a list of directories or monitoring a parent directory and its subdirectories.

- **File Type Filtering**: Users could filter files based on type or extension, in addition to the "content-banned" or a different string.

- **Daemon Mode**: The script could run as a background service, restarting automatically after system reboots using tools like systemd.

- **More Detailed Output**: Detailed information such as file sizes, timestamps, and error messages could be added to the output.

- **Cross-Platform Support**: The script could be improved for better cross-platform compatibility, including Windows.

- **Graceful Shutdown**: A mechanism could be implemented for users to gracefully stop the script without manually interrupting it.
