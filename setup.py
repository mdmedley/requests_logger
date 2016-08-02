from setuptools import setup


license = open('LICENSE', 'r').read()
long_description = (
    'This package is a wrapper around Requests to log http requests '
    'in a human readable format.'
)


setup(
    name='requests_logger',
    version='0.2.0',
    description='Wrapper around Requests to add logging',
    long_description=long_description,
    author='Marcus Medley',
    author_email='mdmeds@gmail.com',
    license=license,
    packages=['requests_logger'],
    tests_require=['tox', 'mock'],
    keywords=['requests', 'logging', 'request', 'log', 'logger'],
    url='https://github.com/mdmedley/requests_logger',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'
    )
)
