from smartlogger import Logger
from smartlogger.handlers import ConsoleHandler, FileHandler, TimeRotatingFileHandler
from smartlogger.formatter import Formatter, JSONFormatter
from smartlogger.levels import DEBUG

print("--- Testing Colorized Console ---")
# 1. Colorized Console Test
console_log = Logger(level=DEBUG, formatter=Formatter("[{time}] [{level}] {message}"))
console_log.add_handler(ConsoleHandler(color=True))

console_log.debug("Checking system configurations...")
console_log.info("System successfully initialized.")
console_log.warning("Memory usage is getting high.")
console_log.error("Failed to connect to the database!")

print("\n--- Testing JSON Format & Time Rotation ---")
# 2. JSON & Daily File Rotation Test
json_log = Logger(level=DEBUG, formatter=JSONFormatter())
json_log.add_handler(TimeRotatingFileHandler("test_logger/daily-log"))

json_log.info("This message is saved as JSON.")
json_log.error("Another JSON error logged.")
print("Check the 'test_logger' folder for the new daily-log file!")

print("\n--- Testing Size-based File Rotation ---")
# 3. Size-Based File Rotation Test (max_size=50 bytes for quick testing)
size_log = Logger(level=DEBUG, formatter=Formatter("[{level}] {message}"))
size_log.add_handler(FileHandler("test_logger/size-log.log", max_size=50))

size_log.info("Filling up the log file...")
size_log.info("This should trigger a backup rotation!")
print("Check the 'test_logger' folder for size-log.log and size-log.log.1")