from smartlogger import Logger
from smartlogger.handlers import ConsoleHandler

log = Logger()

log.add_handler(ConsoleHandler())

log.info("Testing installed library")