import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import ctf
AUTO_FILTER = True

class ctfHandler(FileSystemEventHandler):
    def on_modified(self, event):
        time.sleep(10)
        ctf.ctf()

event_handler = ctfHandler()
observer = Observer()
observer.schedule(event_handler, ctf.DOWNLOADS_DIR, recursive=True)
observer.start()
try:
    while AUTO_FILTER:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()