# SmartLogger
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
A lightweight modular logging framework built in Python.

## Features
- Modular logging architecture
- Multiple log levels (DEBUG, INFO, WARNING, ERROR)
- Console and file logging
- Custom log format templates
- Log rotation support
- Exception logging

## Installation
Clone the repository and install:
pip install -e .

## Usage

```python
'''
from smartlogger import Logger
from smartlogger.handlers import ConsoleHandler
from smartlogger.formatter import Formatter
formatter = Formatter("[{time}] [{level}] {message}")
log = Logger(formatter=formatter)
log.add_handler(ConsoleHandler())
log.info("Application started")
'''

## Example Output
[2026-03-07 12:00:01] [INFO] Application started 

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