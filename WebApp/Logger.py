import logging

# todo log levels, trace flags, etc

logger = None


def init_logger(file, console):
    global logger
    logger = AppLogger()
    logging.basicConfig()

    if file is not None:
        logger.file = logging.getLogger("WebAppLog")
        fh = logging.FileHandler(file)
        logger.file.addHandler(fh)
        logger.file.setLevel(logging.DEBUG)

    if console:
        logger.console = logging.getLogger("WebAppConsole")
        logger.file.setLevel(logging.INFO)


def log_info(msg):
    if logger.file:
        logger.file.info(msg)

    if logger.console:
        logger.console.info(msg)


def log_debug(msg):
    if logger.file:
        logger.file.debug(msg)

    if logger.console:
        logger.console.debug(msg)


class AppLogger:
    def __init__(self):
        self.console = None
        self.file = None
