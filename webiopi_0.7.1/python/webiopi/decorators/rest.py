from webiopi.utils.types import M_PLAIN

def request(method="GET", path="", data=None):
    def wrapper(func):
        func.routed = True
        func.method = method
        func.path = path
        func.data = data
        return func
    return wrapper

def response(fmt="%s", contentType=M_PLAIN):
    def wrapper(func):
        func.format = fmt
        func.contentType = contentType
        return func
    return wrapper

def macro(method="POST", action ="", contentType=M_PLAIN):
    def wrapper(func):
        func.macro = True
        func.method = method
        func.action = action or func.__name__
        func.contentType = contentType
        return func
    return wrapper
