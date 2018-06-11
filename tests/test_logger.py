
# -*- coding: utf-8 -*-


import pytest
import os
import shutil
from pgo import logger as pgo_logger
from pgo.logger import ENV_WORK_DIR, ENV_LOG_LEVEL, ENV_LOG_FNAME


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
        assert logger.level == 30 # WARNING level

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

        log_file = "test.log"
        whole_log_file = os.path.join(LOG_FOLDER, log_file)
        if os.path.exists(whole_log_file):
            os.remove(whole_log_file)

        os.environ[ENV_WORK_DIR] = TMP_DIR
        os.environ[ENV_LOG_FNAME] = log_file

        logger = pgo_logger.get_logger()

        assert logger is not None

        logger.info("test")
        assert os.path.exists(whole_log_file) is True
        assert os.path.isfile(whole_log_file) is True

    def test_passing_log_fname(self):
        """Test with passing log fname to function"""

        log_env_file = "test.log"
        log_file = "test_2.log"
        whole_env_log_file = os.path.join(LOG_FOLDER, log_env_file)
        whole_log_file = os.path.join(LOG_FOLDER, log_file)

        # remove both files if they exist
        for file in (whole_env_log_file, whole_log_file):
            if os.path.exists(file):
                os.remove(file)

        os.environ[ENV_WORK_DIR] = TMP_DIR
        os.environ[ENV_LOG_FNAME] = log_env_file

        logger = pgo_logger.get_logger(log_file_name=log_file)
        assert logger is not None

        logger.info("test")

        assert os.path.exists(whole_log_file) is True
        assert os.path.isfile(whole_log_file) is True
        assert os.path.exists(whole_env_log_file) is False

