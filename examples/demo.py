
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# create logger object
from smartlogger import Logger
from smartlogger.handlers import ConsoleHandler, FileHandler
from smartlogger.formatter import Formatter
formatter = Formatter(" [{level}] {message}")
log = Logger(formatter=formatter)
log.add_handler(ConsoleHandler())
# log.add_handler(FileHandler("app.log"))

log.info("Custom format working")
log.warning("Low memory warning")
log.warning("Low memory warning")
# try:
#     x=10/0
# except Exception as e:
#     log.exception(e)
