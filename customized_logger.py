# Author Sajad

# This class Will create instance once only
# In next initiation it will return
# The same object


class SingletonPattern(object):
    class __SingletonPattern:
        def __init__(self, filename='log'):
            self.val = filename

        def _write_report(self, level, msg):
            with open(self.val + '.log', 'a') as file:
                file.write("[{level}]: {msg}".format(level=level, msg=msg))

        def warning(self, msg):
            return self._write_report("WARNING", msg)

        def critical(self, msg):
            return self._write_report("CRITICAL", msg)

        def info(self, msg):
            return self._write_report("WARNING", msg)

        def debug(self, msg):
            return self._write_report("DEBUG", msg)

    instance = None

    def __new__(cls, *args, **kwargs):
        if not SingletonPattern.instance:
            name = input('>>> ')
            SingletonPattern.instance = SingletonPattern.__SingletonPattern(name)
        return SingletonPattern.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)
