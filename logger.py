
# -*- coding: utf-8 -*-

"""Logger module"""

import logging
import os

__version__ = "0.0.1.dev"

ENV_WORK_DIR = "PGO_WORK_DIR"
ENV_LOG_LEVEL = "PGO_LOG_LEVEL"
DEFAULT_LOG_LEVEL = "DEBUG"
DEFAULT_LOGGER_NAME = "logger"
LOG_DIR = "/log"


def get_logger(logger_name=DEFAULT_LOGGER_NAME, log_file_name=None):
    """Returns a logger object"""

    # log_format = "%(asctime)s | %(levelname)s | %(process)d | " \
    #     "%(name)s | %(filename)s:%(lineno)s | %(message)s"
    pass


def _get_whole_log_file(log_file_name):
    """Returns a full path to the log file
        or None if needing env variables were not set or
        log directory does not exist
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
