# SmartLogger
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
A lightweight modular logging framework built in Python.

## Features
- Modular logging architecture
- **Colorized console output** (automatic based on log level)
- Multiple log levels (DEBUG, INFO, WARNING, ERROR)
- **JSON Formatter** for structured logging
- Log rotation by size (`FileHandler`) and **daily time rotation** (`TimeRotatingFileHandler`)
- Custom log format templates
- Exception logging

## Installation
Clone the repository and install:
pip install -e .

## Usage

```python
from smartlogger import Logger
from smartlogger.handlers import ConsoleHandler, TimeRotatingFileHandler
from smartlogger.formatter import Formatter, JSONFormatter
from smartlogger.levels import DEBUG

# Basic Colorized Console Logging
formatter = Formatter("[{time}] [{level}] {message}")
log = Logger(level=DEBUG, formatter=formatter)
log.add_handler(ConsoleHandler(color=True))
log.debug("Tracing execution...")
log.info("Application started")

# Advanced: JSON Logging to a Daily Rotating File
json_log = Logger(level=DEBUG, formatter=JSONFormatter())
json_log.add_handler(TimeRotatingFileHandler("logs/app"))
json_log.error("Database connection failed")
```

## Example Outputs

### Console (Colorized automatically)
```
[2026-05-14 12:00:01] [DEBUG] Tracing execution...
[2026-05-14 12:00:01] [INFO] Application started 
```

### JSON Log File (`logs/app-2026-05-14.log`)
```json
{"time": "2026-05-14 12:00:02", "level": "ERROR", "message": "Database connection failed"}
```

## Architecture
'''
User Code  
↓  
Logger  
↓  
Formatter  
↓  
Handlers  
↓  
Console / File Output
'''

## Project Structure
'''
smartlogger/
│
├── logger.py
├── formatter.py
├── handlers.py
├── levels.py
└── __init__.py
'''
## Author
Aman Gupta  
GitHub: https://github.com/aman-coder-005

## Future Improvements
- Additional log handlers (database, network)
- Configurable log levels
- Asynchronous logging