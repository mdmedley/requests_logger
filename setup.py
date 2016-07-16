from setuptools import setup, find_packages


setup(
    name='requests_logger',
    version='0.0.1',
    description='Wrapper around Requests to add logging',
    author='Marcus Medley',
    author_email='mdmeds@gmail.com',
    packages=find_packages(),
    tests_require=['tox']
)
