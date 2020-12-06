import os

log_path = os.chdir(os.path.expanduser('singleton/bin/data/data.log'))

class Logger(object):

    def __init__(self, file_name):
        self.file_name = log_path

    def _write_log(self, level, msg):
        with open(self.file_name, "a") as log_file:
            log_file.write("[{0}] {1}\n".format(level, msg))

    def critical(self, level, msg):
        self._write_log("CRITICAL",msg)

    def error(self, level, msg):
        self._write_log("ERROR", msg)

    def warn(self, level, msg):
        self._write_log("WARN", msg)

    def info(self, level, msg):
        self._write_log("INFO", msg)

    def debug(self, level, msg):
        self._write_log("DEBUG", msg)
