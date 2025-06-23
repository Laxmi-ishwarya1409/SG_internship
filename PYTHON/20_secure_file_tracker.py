# project: secure file tracker with logs (build a toot that lets the users log file creation, access, deletion, storong logs securely using python logging module) 


import argparse
import os
import sys
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

LOG_FILE = "file_events.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_event(action, file_path):
    message = f"{action} - {file_path}"
    logging.info(message)


class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"[EVENT] File created: {event.src_path}")
            log_event("CREATED", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[EVENT] File deleted: {event.src_path}")
            log_event("DELETED", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            print(f"[EVENT] File modified: {event.src_path}")
            log_event("MODIFIED", event.src_path)

def start(path):
    if not os.path.isdir(path):
        print(f"ERROR: The path '{path}' does not exist or is not a directory.")
        sys.exit(1)
    else:
        print(f"INFO Started monitoring: {path}")
        log_event("MONITORING_STARTED", path)

        event_handler = FileEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()  # starts a new thread to monitor file events

        print("[INFO] Press Ctrl+C to stop monitoring.")

        try:
            while True:
                time.sleep(1)  # keep running
        except KeyboardInterrupt:
            observer.stop()  # Stops watching the folder
            print("\n[INFO] Stopped monitoring.")
        observer.join()   # Waits for the observer thread to end

def show_logs():
    log_file = "file_events.log"
    if not os.path.exists(log_file):
        print("INFO: No logs found yet.")
    else:
        print("INFO: Displaying log contents:\n")
        with open(log_file, "r") as f:
            print(f.read())

def main():
    # creating an object for argparse
    parser = argparse.ArgumentParser(description="Secure File Tracker CLI Tool")
    # Add subparsers for commands
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    # Define the start subcommand
    start_parser = subparsers.add_parser("start", help="Start monitoring a folder")
    start_parser.add_argument("path", help="Path to folder to monitor")
    # Define the show-logs subcommand
    log_parser = subparsers.add_parser("show-logs", help="Display the event logs")
    # Parse the command-line arguments
    args = parser.parse_args()
    # Conditional logic to handle commands
    if args.command == "start":
        start(args.path)
    elif args.command == "show-logs":
        show_logs()
    else:
        parser.print_help()


main()