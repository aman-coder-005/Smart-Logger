import unittest
import json
import os
import shutil
from smartlogger import Logger
from smartlogger.formatter import Formatter, JSONFormatter
from smartlogger.levels import INFO, DEBUG

class TestSmartLogger(unittest.TestCase):
    def test_formatter_text(self):
        formatter = Formatter("[{level}] {message}")
        result = formatter.format(INFO, "Test message")
        self.assertEqual(result, "[INFO] Test message")

    def test_formatter_json(self):
        formatter = JSONFormatter()
        result = formatter.format(DEBUG, "JSON Test")
        data = json.loads(result)
        self.assertEqual(data["level"], "DEBUG")
        self.assertEqual(data["message"], "JSON Test")
        self.assertIn("time", data)

    def test_logger_level_filtering(self):
        # We can test if messages below the set level are ignored.
        class DummyHandler:
            def __init__(self):
                self.messages = []
            def emit(self, message, level=None):
                self.messages.append(message)

        log = Logger(level=INFO)
        handler = DummyHandler()
        log.add_handler(handler)
        
        log.debug("This should be ignored")
        log.info("This should be logged")
        
        self.assertEqual(len(handler.messages), 1)
        self.assertIn("This should be logged", handler.messages[0])

if __name__ == "__main__":
    unittest.main()
