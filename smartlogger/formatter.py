

from datetime import datetime
from .levels import LEVEL_NAMES

class Formatter:

    def __init__(self, template="[{time}] [{level}] {message}"):
        self.template = template

    def format(self, level, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        level_name = LEVEL_NAMES[level]

        log = self.template.format(
            time=timestamp,
            level=level_name,
            message=message
        )

        return log

import json

class JSONFormatter:
    def format(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        level_name = LEVEL_NAMES.get(level, "UNKNOWN")
        return json.dumps({
            "time": timestamp,
            "level": level_name,
            "message": message
        })