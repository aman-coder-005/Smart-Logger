'''
from datetime import datetime
from .levels import LEVEL_NAMES
class Formatter:

    def format(self, level, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        level_name = LEVEL_NAMES[level]
        return f"[{timestamp}] [{level_name}] {message}"
'''

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