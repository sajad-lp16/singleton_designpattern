# Author Sajad

# This class Will create instance once only
# In next initiation it will return
# The same object


class Singleton(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance

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
