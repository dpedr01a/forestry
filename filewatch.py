#!/usr/bin/env python
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.merge_done = False

    def on_modified(self, event):
        if event.src_path.endswith('Density.csv') or event.src_path.endswith('Age.csv'):
            print("{} modified".format(event.src_path))
            time.sleep(15)
            self.execute_merge4unity()

    def execute_merge4unity(self):
        if not self.merge_done:
            print("Executing merge4unity.py...")
            subprocess.run(['python', 'merge4unity.py'], cwd="C:/Users/chiba/OneDrive/kimitsu/Model/scripts")
            self.merge_done = True
            self.execute_unityexe()

    def execute_unityexe(self):
        print("Executing unityexe.py...")
        subprocess.run(['python', 'unityexe.py'], cwd="C:/Users/chiba/OneDrive/kimitsu/Model/scripts")

if __name__ == "__main__":
    path = 'C:/Users/chiba/OneDrive/kimitsu/Model'  # Target directory
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
