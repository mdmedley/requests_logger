from setuptools import setup, find_packages


license = open('LICENSE', 'r').read()
long_description = (
    'This package is a wrapper around Requests to log http request '
    'in a human readable format.'
)


setup(
    name='requests_logger',
    version='0.1.0',
    description='Wrapper around Requests to add logging',
    long_description=long_description,
    author='Marcus Medley',
    author_email='mdmeds@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests*')),
    tests_require=['tox'],
    keywords=['requests', 'logging', 'request', 'log', 'logger'],
    url='https://github.com/mdmedley/requests_logger',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'
    )
)
