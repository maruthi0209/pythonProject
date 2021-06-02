import logging

def test_logging():
    my_logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logfile.log")
    myFormatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(myFormatter)
    my_logger.addHandler(fileHandler)
    my_logger.setLevel(logging.DEBUG)
'''
    my_logger.debug("A debug statement is executed")
    my_logger.info("A information statement")
    my_logger.warning("Something is wrong here")
    my_logger.error("An error has occured")
    my_logger.critical("Critical issue")
'''
