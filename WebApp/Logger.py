import logging

# todo log levels, trace flags, etc


def init_logger(file):
    logging.basicConfig(filename=file, level=logging.DEBUG)
