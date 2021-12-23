from json import dumps

from configs import FILE_APPENDER

def log_output(func):
    """ log_output 为了日志输出 """
    def wrapper(*args, **kwargs):
        go_on, log = func(*args, **kwargs)
        with open(FILE_APPENDER, "a+") as f:
            f.write(dumps(log) + "\n")
        return go_on, log
    return wrapper


def for_listener(func):
    """ for_listener
        为了添加其他功能，所以 Hook 函数还增添了其他的返回，
        这对于 Listener 来说是无法识别的。
        因此使用这个装饰器返回一个 bool 类型表示 “是否终止监听”。
    """
    def wrapper(*args, **kwargs):
        go_on = func(*args, **kwargs)[0]
        return go_on
    return wrapper
