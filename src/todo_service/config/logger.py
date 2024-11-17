import logging
from sys import stdout



logger = logging.getLogger("Logger")
logger.setLevel(logging.DEBUG)
logformater = logging.Formatter("%(name)-12s %(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")
console_handle = logging.StreamHandler(stdout)
console_handle.setFormatter(logformater)
logger.addHandler(console_handle)