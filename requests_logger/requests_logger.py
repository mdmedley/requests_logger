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
        return self.log_request(response)

    def log_request(self, response):

        # Get params. Defaults to empty string
        if '?' in response.request.url:
            url, params_str = response.request.url.split('?', 1)

            params = {
                param.split('=')[0]: param.split('=')[1] for param in
                params_str.split('&')
            }
        else:
            params = None

        # Log request
        self.logger.debug(
            request_message.format(
                method=response.request.method,
                url=response.request.url,
                params=params,
                headers=response.request.headers,
                body=response.request.body))

        # Log response
        self.logger.debug(
            response_message.format(
                status=response.status_code,
                headers=response.headers,
                body=response.content,
                divider='-' * 79))

        return response
