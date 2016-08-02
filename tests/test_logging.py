import os
import mock
import logging
from nose.tools import raises

from requests_logger import (LoggingRequests, LoggerError)


def mocked_request(*args, **kwargs):
    class MockResponse(object):
        class request(object):
            pass

        def __init__(
                self, status_code, method, url, params=None, content=None,
                headers=None, body=None):
            self.params = params
            self.status_code = status_code
            self.content = content
            self.headers = headers
            self.request.headers = headers
            self.request.method = method
            self.request.url = url
            self.request.body = body

        def json(self):
            return self.json_data

    return MockResponse(
        status_code=200, method='GET',
        url='http://website.com/?foo=bar&bar=foo')


class TestLoggingRequests():

    @raises(LoggerError)
    def test_no_logger_exception(self):
        LoggingRequests()

    @mock.patch('requests.request', side_effect=mocked_request)
    def test_requests_logging(self, mock_request):
        self.req.request(
            'GET', 'http://website.com', params={'foo': 'bar', 'bar': 'foo'})
        expected = [
            'method  : GET',
            'url     : http://website.com/?foo=bar&bar=foo',
            "params  : {'foo': 'bar', 'bar': 'foo'}",
            'body    : None'
        ]

        assert os.path.exists('/tmp/logs.log')
        assert self._file_contains('/tmp/logs.log', expected)[0]

    @classmethod
    def setUpClass(cls):
        logger = logging.getLogger(__name__)
        handler = logging.FileHandler('/tmp/logs.log', mode='w')
        formater = logging.Formatter(
            '%(asctime)s: %(levelname)s: %(name)s: %(message)s')
        handler.setFormatter(formater)
        logger.addHandler(handler)

        cls.req = LoggingRequests(logger=logger)

    @classmethod
    def tearDownClass(cls):
        os.remove('/tmp/logs.log')

    def _file_contains(self, file_path, target_strings):
        """
            Checks that the specified file contains all strings in the
            target_strings list.
        """
        not_found = []
        with open(file_path) as in_file:
            contents = in_file.read()
        for target_string in target_strings:
            if target_string not in contents:
                not_found.append(target_string)
        if len(not_found) > 0:
            return (False, not_found)
        return (True, not_found)
