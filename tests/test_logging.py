import os
import mock
import logging

from requests_logger import LoggingRequests


class Request(object):
    pass


def mocked_request(*args, **kwargs):
    class MockResponse(object):
        def __init__(
                self, status_code, method, url, params=None, content=None,
                headers=None, body=None, history=[]):
            self.params = params
            self.status_code = status_code
            self.content = content
            self.headers = headers
            self.history = history
            self.request = Request()
            self.request.headers = headers
            self.request.method = method
            self.request.url = url
            self.request.body = body

    if args[1] == 'http://website.com':
        return MockResponse(
            status_code=200, method='GET',
            url='http://website.com/?foo=bar&bar=foo')

    if args[1] == 'http://redirect.com':
        redirect = MockResponse(
            status_code=301, method='GET', url='http://redirect.com/')
        return MockResponse(
            status_code=200, method='GET',
            url='https://redirect.com/', history=[redirect])


class TestLoggingRequests(object):
    @mock.patch('requests.request', side_effect=mocked_request)
    def test_requests_logging(self, mock_request):
        self.req.request(
            'GET', 'http://website.com', params={'foo': 'bar', 'bar': 'foo'})
        expected = [
            'method  : GET',
            'url     : http://website.com/?foo=bar&bar=foo',
            "'foo': 'bar'",
            "'bar': 'foo'",
            'body    : None'
        ]

        assert os.path.exists('/tmp/logs.log')
        assert self._file_contains('/tmp/logs.log', expected)[0]

    @mock.patch('requests.request', side_effect=mocked_request)
    def test_requests_logging_redirect(self, mock_request):
        self.req.request(
            'GET', 'http://redirect.com')
        expected = [
            'method  : GET',
            'url     : http://redirect.com/',
            'params  : None',
            'body    : None',
            'url     : https://redirect.com/'
        ]

        assert os.path.exists('/tmp/logs.log')
        assert self._file_contains('/tmp/logs.log', expected)[0]

    @classmethod
    def setUpClass(cls):
        logger = logging.getLogger('requests_logger')
        handler = logging.FileHandler('/tmp/logs.log', mode='w')
        formater = logging.Formatter(
            '%(asctime)s: %(levelname)s: %(name)s: %(message)s')
        handler.setFormatter(formater)
        logger.addHandler(handler)

        cls.req = LoggingRequests

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
