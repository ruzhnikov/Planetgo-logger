
# -*- coding: utf-8 -*-

"""Planetgo logger module"""

import logging
import os

__version__ = "0.4.0"

ENV_WORK_DIR = "PGO_WORK_DIR"
ENV_LOG_LEVEL = "PGO_LOG_LEVEL"
ENV_LOG_FNAME = "PGO_LOG_FNAME"
DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_LOGGER_NAME = "logger"
LOG_DIR = "/log"
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(process)d | " \
    "%(name)s | %(filename)s:%(lineno)s | %(message)s"


def get_logger(logger_name=DEFAULT_LOGGER_NAME, log_file_name=None, log_level=None):
    """Returns a logger object

        Parameters
        ----------
        logger_name : str, optional
            A name of logger. By default will be used the default logger
        log_file_name : str, optional
            A name of log file. If it is None, logger will use STDOUT
        log_level: str, optional
            A level of logging. It can be set by enviroment variable too
    """

    # a level of logging can be set by enviroment variable.
    # Check it if this one wasn't be obtained by parameter
    if log_level is None:
        if ENV_LOG_LEVEL in os.environ:
            log_level = os.environ.get(ENV_LOG_LEVEL)
        else:
            log_level = DEFAULT_LOG_LEVEL

    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    log_handler = None

    if log_file_name is None:
        if ENV_LOG_FNAME in os.environ:
            log_file_name = os.environ.get(ENV_LOG_FNAME)

    # the whole path to the log file. Can be None
    whole_log_file = None

    if log_file_name is not None:
        whole_log_file = _get_whole_log_file(log_file_name)

    if whole_log_file is None:
        log_handler = logging.StreamHandler()
    else:
        log_handler = logging.FileHandler(whole_log_file)

    formatter = logging.Formatter(LOG_FORMAT)
    log_handler.setFormatter(formatter)

    logger.addHandler(log_handler)

    return logger


def _get_whole_log_file(log_file_name):
    """Returns a full path to the log file
        or None if needing env variables were not set or
        log directory does not exist

        Parameters
        ----------
        log_file_name : str
            A name of log file
        
        Returns
        -------
        str
            A whole path to the log file or None
    """
    if ENV_WORK_DIR not in os.environ:
        return None

    work_dir = os.environ.get(ENV_WORK_DIR)
    log_dir = work_dir + LOG_DIR

    if not os.path.exists(work_dir):
        return None

    if not os.path.exists(log_dir):
        return None

    return log_dir + "/" + log_file_name
