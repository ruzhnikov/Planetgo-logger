
# -*- coding: utf-8 -*-


import pytest
import os
import shutil
from pgo import logger as pgo_logger


TMP_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_FOLDER = TMP_DIR + "/log"


def clean_file_before_test():
    """Delete all files from log directory"""

    if os.path.exists(LOG_FOLDER):
        for file in os.listdir(LOG_FOLDER):
            os.remove(LOG_FOLDER + "/" + file)


class TestLoggerWithoutFile():
    """Testing the logger without passing fname or needed env variables"""

    def test_default_values(self):
        """Simple test with default values"""

        logger = pgo_logger.get_logger()
        assert logger is not None
        assert logger.hasHandlers() is True
        assert logger.name == pgo_logger.DEFAULT_LOGGER_NAME
        assert logger.level == 20 # INFO level

    def test_passing_parameters(self):
        """Testing with passing several parameters"""

        logger_name = "test_logger_name"
        logger = pgo_logger.get_logger(logger_name, log_level="WARNING")

        assert logger is not None
        assert logger.hasHandlers() is True
        assert logger.name == logger_name
        assert logger.level == 30

class TestLoggerWithFile():
    """"Testing with creating and passing log file and log directory"""

    @classmethod
    def setup_class(cls):
        if not os.path.exists(LOG_FOLDER):
            os.makedirs(LOG_FOLDER)
    
    @classmethod
    def teardown_class(cls):
        if os.path.exists(LOG_FOLDER):
            shutil.rmtree(LOG_FOLDER)

    def test_passing_env(self):
        """Test with passing parameters via env"""

        pass