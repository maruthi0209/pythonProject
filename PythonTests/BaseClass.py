import inspect
import logging


class BaseClass:

    def test_logging(self):
        loggerName = inspect.stack()[1][3]
        my_logger = logging.getLogger(loggerName)
        file_handler = logging.FileHandler("logfile.log")
        my_formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(my_formatter)
        my_logger.addHandler(file_handler)
        my_logger.setLevel(logging.DEBUG)
        return my_logger
'''
        my_logger.debug("A debug statement is executed")
        my_logger.info("A information statement")
        my_logger.warning("Something is wrong here")
        my_logger.error("An error has occured")
        my_logger.critical("Critical issue")
'''
