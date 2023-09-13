import logging
import os
from dotenv import load_dotenv

load_dotenv()

class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno == self.__level


class Logger(object):
    def __init__(self, log_path, name=""):
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(logging.DEBUG)
        self.__logger.addHandler(
            self.__get_file_handler(log_path + "info.log", logging.INFO)
        )
        self.__logger.addHandler(
            self.__get_file_handler(log_path + "error.log", logging.ERROR)
        )

    def __get_file_handler(self, filename, level):
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(level)
        file_handler.addFilter(MyFilter(level))
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        return file_handler

    def get_logger(self):
        return self.__logger



LOG_DIR = os.getenv("LOG_DIR")

logger = Logger(LOG_DIR).get_logger()
