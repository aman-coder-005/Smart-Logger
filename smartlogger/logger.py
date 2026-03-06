import traceback
from .formatter import Formatter
from .handlers import ConsoleHandler, FileHandler
from .levels import INFO, ERROR
class Logger:
    def __init__(self,level=INFO,formatter=None):
        self.level = level
        self.formatter =formatter or Formatter()
        self.handlers = []
    def add_handler(self, handler):
        self.handlers.append(handler)
    def log(self, level, message):
        if level < self.level:
            return
        formatted_message = self.formatter.format(level, message)
        for handler in self.handlers:
            handler.emit(formatted_message)
    def info(self, message):
        self.log(INFO, message)
    def error(self, message):
        self.log(ERROR, message)
    def exception(self, error):
        error.message=str(error)
        trace=traceback.format_exc()
        full_message=f"{error.message}\n{trace}"
        self.log(ERROR, full_message)
        