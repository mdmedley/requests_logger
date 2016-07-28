import os
import logging
from nose.tools import raises

from requests_logger import LoggingRequests, LoggerError


class TestLoggingRequests():

    @raises(LoggerError)
    def test_no_logger_exception(self):
        LoggingRequests()

    def test_requests_logging(self):
        self.req.request('GET', 'http://www.google.com')
        expected = [
            'method  : GET',
            'url     : http://www.google.com/',
            'params  : None',
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
        """ Checks that the specified file contains all strings in the
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
