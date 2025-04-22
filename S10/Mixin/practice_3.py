import logging

class LoggerMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)
        logging.basicConfig(level=logging.INFO)

    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        if callable(attr):
            def logged_method(*args, **kwargs):
                self.logger.info(f"Method {name} called with args: {args}, kwargs: {kwargs}")
                return attr(*args, **kwargs)
            return logged_method
        return attr


#test class  
class MyClass(LoggerMixin):
    def my_method(self, x, y):
        return x + y

obj = MyClass()
print(obj.my_method(3, 4))


