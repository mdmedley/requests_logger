[![PyPI](https://img.shields.io/pypi/v/requests_logger.svg?style=flat-square)](https://pypi.python.org/pypi/requests_logger) [![Travis](https://img.shields.io/travis/mdmedley/requests_logger.svg?style=flat-square)](https://travis-ci.org/mdmedley/requests_logger)

# Requests Logging

This package is a wrapper around the requests.request object to log http request in a human readable format.

### Version
v0.0.1


### Installation
```sh
pip install git+ssh://git@github.com/mdmedley/requests_logger.git
```


### Quickstart
```python
import logging
from requests_logger import LoggingRequests

logger = logging.getLogger('my_logger')
# Setup logger how you see fit

req = LoggingRequests(logger)
req.request('GET', 'http://google.com')
```


### Development
Want to contribute? Great! Fork and submit a pull request!


### Todos

    - Format json and xml request/response bodies
    - Rename package
    - Rename Class
    - Write more tests
