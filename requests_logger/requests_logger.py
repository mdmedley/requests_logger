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
    def get(cls, url, **kwargs):
        return cls.request(method='GET', url=url, **kwargs)

    @classmethod
    def put(cls, url, **kwargs):
        return cls.request(method='PUT', url=url, **kwargs)

    @classmethod
    def post(cls, url, data=None, **kwargs):
        return cls.request(method='POST', url=url, data=data, **kwargs)

    @classmethod
    def delete(cls, url, **kwargs):
        return cls.request(method='DELETE', url=url, **kwargs)

    @classmethod
    def copy(cls, url, **kwargs):
        return cls.request(method='COPY', url=url, **kwargs)

    @classmethod
    def head(cls, url, **kwargs):
        return cls.request(method='HEAD', url=url, **kwargs)

    @classmethod
    def options(cls, url, **kwargs):
        return cls.request(method='OPTIONS', url=url, **kwargs)

    @classmethod
    def patch(cls, url, **kwargs):
        return cls.request(method='PATCH', url=url, **kwargs)

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
