import requests
import logging
from .common import (request_message, response_message, classproperty)

logging.getLogger("requests").setLevel(logging.WARNING)


class LoggingRequests(object):
    """
        Wrapper class for Requests to add logging
    """

    @classproperty
    def logger(cls):
        return logging.getLogger('requests_logger.{0}'.format(cls.__name__))

    @classmethod
    def request(cls, method, url, **kwargs):
        # Make the actual request
        response = requests.request(method, url, **kwargs)
        for resp in response.history:
            cls.log_request(resp)
        else:
            return cls.log_request(response)

    @classmethod
    def log_request(cls, response):

        # Get params. Defaults to None
        if '?' in response.request.url:
            url, params_str = response.request.url.split('?', 1)

            params = {
                param.split('=')[0]: param.split('=')[1] for param in
                params_str.split('&')
            }
        else:
            params = None

        # Log request
        cls.logger.debug(
            request_message.format(
                method=response.request.method,
                url=response.request.url,
                params=params,
                headers=response.request.headers,
                body=response.request.body))

        # Log response
        cls.logger.debug(
            response_message.format(
                status=response.status_code,
                headers=response.headers,
                body=response.content,
                divider='-' * 79))

        return response
