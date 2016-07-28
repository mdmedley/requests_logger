from setuptools import setup, find_packages


license = open('LICENSE', 'r').readlines()


setup(
    name='requests_logger',
    version='0.0.3',
    description='Wrapper around Requests to add logging',
    author='Marcus Medley',
    author_email='mdmeds@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests*')),
    tests_require=['tox'],
    keywords=['requests', 'logging', 'request'],
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
    ),
)
