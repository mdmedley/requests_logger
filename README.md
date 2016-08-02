[![PyPI](https://img.shields.io/pypi/v/requests_logger.svg?style=flat-square)](https://pypi.python.org/pypi/requests_logger) [![Travis](https://img.shields.io/travis/mdmedley/requests_logger.svg?style=flat-square)](https://travis-ci.org/mdmedley/requests_logger)

# Requests Logging

This package is a wrapper around Requests to log http requests in a human readable format.

### Version
v0.2.0


### Installation
```sh
pip install requests_logger
```


### Quickstart
```python
import logging
from requests_logger import LoggingRequests

# Setup logger
logger = logging.getLogger('requests_logger') #  Gets base logger for LoggingRequests
handler = logging.FileHandler('logs.log', mode='w')
formater = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
handler.setFormatter(formater)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

response = LoggingRequests.request('GET', 'http://google.com')
```


### Development
Want to contribute? Great! Fork and submit a pull request!


### Todos

    - Format json and xml request/response bodies
    - Rename package (maybe)
    - Rename Class (maybe)
    - Write more tests
