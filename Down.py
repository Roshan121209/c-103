import os
import shutil
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/rosha/Downloads"
to_dir = "C:/Users/rosha/OneDrive/Desktop/roshan/to"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)
        for key, value in dir_tree.items():
            if (extension in value):
                file_name = os.path.basename(event.src_path)
                path1 = from_dir + "/" + file_name
                path2 = to_dir + "/" + key
                path3 = to_dir + "/" + key + "/" + file_name

                if os.path.exists(to_dir + "/" + key):
                    if os.path.exists(path2):
                        print("moving")
                        shutil.move(path1, path3)

                    else:
                        os.makedirs(path2)
                        print("moving")
                        shutil.move(path1, path3)
                        time.sleep(1)
                            



event_handler = FileMovementHandler()

observer = Observer()
observer.schedule(event_handler, from_dir, recursive = True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running")

except KeyboardInterrupt : 
    print("stop")
    observer.stop()        