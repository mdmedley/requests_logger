request_message = (
    '\n=======\n'
    'REQUEST\n'
    '=======\n'
    'method  : {method}\n'
    'url     : {url}\n'
    'params  : {params}\n'
    'headers : {headers}\n'
    'body    : {body}\n'
)

response_message = (
    '\n========\n'
    'RESPONSE\n'
    '========\n'
    'status  : {status}\n'
    'headers : {headers}\n'
    'body    : {body}\n'
    '{divider}'
)


class ClassPropertyDescriptor(object):

    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        return self.fget.__get__(obj, klass)()


def classproperty(func):
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)
    return ClassPropertyDescriptor(func)
