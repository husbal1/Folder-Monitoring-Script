import os
import sys
import time

# Expose the polling interval as a variable
POLLING_INTERVAL = 1  # Default value in seconds

def monitor_folder(folder_path):
    """Monitors a folder for files with 'content-banned' in their names and detects creation, removal, and renaming."""
    print(f"Monitoring folder: {folder_path}\n")
    print(f"Polling interval: {POLLING_INTERVAL} second(s)\n")

    # At startup: Check for existing files with 'content-banned'
    existing_files = [f for f in os.listdir(folder_path) if 'content-banned' in f]
    for file in existing_files:
        print(f"Found during startup: {file}")

    # Map tracked files to their inode numbers
    tracked_files = {f: os.stat(os.path.join(folder_path, f)).st_ino 
                     for f in existing_files}

    while True:
        try:
            time.sleep(POLLING_INTERVAL)  # Use the configurable polling interval

            # Map current files to their inode numbers
            current_files = {f: os.stat(os.path.join(folder_path, f)).st_ino 
                             for f in os.listdir(folder_path) if 'content-banned' in f}

            # Detect renamed files first
            renamed_files = []
            for old_file, old_inode in tracked_files.items():
                for new_file, new_inode in current_files.items():
                    if old_inode == new_inode and old_file != new_file:
                        renamed_files.append((old_file, new_file))
                        print(f"Renamed: {old_file} -> {new_file}")

            # Exclude renamed files from further processing
            renamed_old_files = {old for old, _ in renamed_files}
            renamed_new_files = {new for _, new in renamed_files}

            # Detect created files (excluding renamed ones)
            created_files = {f for f in current_files if f not in tracked_files and f not in renamed_new_files}
            for created_file in created_files:
                print(f"Created: {created_file}")

            # Detect removed files (excluding renamed ones)
            removed_files = {f for f in tracked_files if f not in current_files and f not in renamed_old_files}
            for removed_file in removed_files:
                print(f"Removed: {removed_file}")

            # Update tracked files
            tracked_files = current_files

        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
            break
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    while True:
        folder_path = input("Enter the full path of the folder to monitor: ").strip()
        if not folder_path:
            print("Error: No folder path provided. Please try again.")
            continue

        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' does not exist. Please provide a valid path.")
            continue

        # Start monitoring the valid folder path
        monitor_folder(folder_path)