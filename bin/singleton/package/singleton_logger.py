import os
from .package.singleton_object import SingletonObject

log_path = os.path.expanduser('~/code/python/singleton/bin/data/data.log')

logger_object = SingletonObject(log_path)

logger_object.critical("CRITICAL")

logger_object.error("ERROR")

logger_object.warn("WARN")

logger_object.info("INFO")

logger_object.debug("DEBUG")
