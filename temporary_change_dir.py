import os
from contextlib import contextmanager
from functools import wraps

# 定义一个上下文管理器，用于临时改变当前工作目录
@contextmanager
def temporary_change_dir(path):
    current_dir = os.getcwd()  # 获取当前工作目录
    os.chdir(path)  # 改变当前工作目录到指定路径
    try:
        yield
    finally:
        os.chdir(current_dir)  # 恢复原工作目录

def class_temporary_change_dir(path):
    def class_decorator(cls):
        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value):
                setattr(cls, attr_name, method_decorator(attr_value, path))
        return cls

    def method_decorator(method, path):
        @wraps(method)
        def wrapper(*args, **kwargs):
            old_dir = os.getcwd()
            os.chdir(path)
            try:
                result = method(*args, **kwargs)
            finally:
                os.chdir(old_dir)
            return result
        return wrapper

    return class_decorator