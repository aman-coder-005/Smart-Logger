import os

class ConsoleHandler:
    def __init__(self, color=True):
        self.color = color

    def emit(self, message, level=None):
        if self.color and level is not None:
            from .levels import DEBUG, INFO, WARNING, ERROR
            colors = {
                DEBUG: "\033[36m",    # Cyan
                INFO: "\033[32m",     # Green
                WARNING: "\033[33m",  # Yellow
                ERROR: "\033[31m",    # Red
            }
            reset = "\033[0m"
            color_code = colors.get(level, "")
            print(f"{color_code}{message}{reset}")
        else:
            print(message)
            
class FileHandler:


        def __init__(self, filename, max_size=5000):
            self.filename = filename
            self.max_size = max_size
            dir_name = os.path.dirname(self.filename)
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)
            with open(self.filename, "a", encoding="utf-8"):
                pass

        def emit(self, message, level=None):
            dir_name = os.path.dirname(self.filename)
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)
                
            if os.path.exists(self.filename):
                if os.path.getsize(self.filename) > self.max_size:
                    backup = self.filename + ".1"
                    if os.path.exists(backup):
                        os.remove(backup)
                    os.rename(self.filename, backup)

            with open(self.filename, "a", encoding="utf-8") as f:
                f.write(message + "\n")

import time
from datetime import datetime

class TimeRotatingFileHandler:
    def __init__(self, filename_prefix="app"):
        self.filename_prefix = filename_prefix

    def _get_filename(self):
        date_str = datetime.now().strftime("%Y-%m-%d")
        return f"{self.filename_prefix}-{date_str}.log"

    def emit(self, message, level=None):
        filename = self._get_filename()
        dir_name = os.path.dirname(filename)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
            
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")