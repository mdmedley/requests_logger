import requests

from .constants import (request_message, response_message)


class LoggerError(Exception):
    """
        Raised when initialiation of LoggingRequests object attempted without
        providing a logger.
    """


class LoggingRequests(object):
    """
        Wrapper class for requests.request to add logging
    """

    def __init__(self, logger=None, *args, **kwargs):
        super(LoggingRequests, self).__init__()

        # Set logger for object
        self.logger = logger

        # Throw error if logger not provided
        if not self.logger:
            raise LoggerError('Logger not provided')

    def request(self, method, url, **kwargs):
        # Make the actual request
        response = requests.request(method, url, **kwargs)

        # Get params dictionary. Defaults to None
        params = kwargs.get('params')

        # Log request
        self.logger.debug(
            request_message.format(
                method=response.request.method,
                url=response.request.url,
                params=params,
                headers=response.request.headers,
                body=kwargs.get('data')))

        # Log response
        self.logger.debug(
            response_message.format(
                status=response.status_code,
                headers=response.headers,
                body=response.content,
                divider='-' * 79))

        return response
