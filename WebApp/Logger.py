from enum import Enum

from logging import INFO, DEBUG
from logging import FileHandler, StreamHandler
from logging import basicConfig, getLogger


class TraceFlag(Enum):
    APP = "webapp"
    DB = "database"
    WIDGET = "widget"


app_name = "WebApp"


def init_logger(file, console):
    """init loggers for console and files

    :param file: path to log file or None to skip
    :type file: string or None
    :param console: flag to enable console output
    :type console: bool"""
    global trace_flags
    # the linters will fight over doing this inline
    trace_flags = {}
    trace_flags[TraceFlag.APP] = True
    trace_flags[TraceFlag.DB] = True
    trace_flags[TraceFlag.WIDGET] = True

    handlers = []
    fmt_str = "%(name)s:%(levelname)s: %(message)s"

    # todo parameterize
    console_level = INFO
    file_level = DEBUG

    if file is not None:
        fh = FileHandler(file)
        fh.setLevel(file_level)
        handlers.append(fh)
    if console:
        sh = StreamHandler()
        sh.setLevel(console_level)
        handlers.append(sh)

    # if len(handles) > 0?
    basicConfig(level=DEBUG, handlers=handlers, format=fmt_str)


def set_tf(tf, value):
    """sets trace flag to value"""
    if not isinstance(tf, TraceFlag):
        raise f"{tf} is not a TraceFlag"
    trace_flags[tf] = value


def debug(tf, msg):
    """wrapper around logging.debug"""
    if not isinstance(tf, TraceFlag):
        raise f"{tf} is not a TraceFlag"
    if trace_flags[tf]:
        logger = f"{app_name}.{tf.value}"
        getLogger(logger).debug(msg)


def info(tf, msg):
    """wrapper for logging.info"""
    if not isinstance(tf, TraceFlag):
        raise f"{tf} is not a TraceFlag"
    if trace_flags[tf]:
        logger = f"{app_name}.{tf.value}"
        getLogger(logger).info(msg)


def warning(tf, msg):
    """wrapper around logging.warning"""
    if not isinstance(tf, TraceFlag):
        raise f"{tf} is not a TraceFlag"
    if trace_flags[tf]:
        logger = f"{app_name}.{tf.value}"
        getLogger(logger).warning(msg)


def error(tf, msg):
    """wrapper around logging.error"""
    if not isinstance(tf, TraceFlag):
        raise f"{tf} is not a TraceFlag"
    if trace_flags[tf]:
        logger = f"{app_name}.{tf.value}"
        getLogger(logger).error(msg)


def critical(tf, msg):
    """wrapper around logging.critical"""
    if not isinstance(tf, TraceFlag):
        raise f"{tf} is not a TraceFlag"
    if trace_flags[tf]:
        logger = f"{app_name}.{tf.value}"
        getLogger(logger).critical(msg)
