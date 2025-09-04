import logging
import sys
# 1. Write a Python function to create a basic logger that logs messages to a file named `app.log`.
# 2. Modify the function to log messages of levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

def basicLogger():
    logging.basicConfig(filename='assignement_1.log', level=logging.DEBUG)
    logging.debug('This is debug message')
    logging.warning('This is warning message')
    logging.info('This is info message')
    logging.error('This is error message')
    logging.critical('This is critical error ')

# 1. Write a Python function to create a logger that logs messages to both a file named `app.log` and the console.
# 2. Modify the function to use different logging levels for the file and console handlers.

def logger_with_handlers():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    file_hadler = logging.FileHandler('app.log')
    consolHandler = logging.StreamHandler()

    file_hadler.setLevel(logging.DEBUG)
    consolHandler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_hadler.setFormatter(formatter)
    consolHandler.setFormatter(formatter)

    logger.addHandler(file_hadler)
    logger.addHandler(consolHandler)

    logger.debug("this is debug message")
    logger.warning("this is warning message")
    logger.critical("this is critical message that will stop your application")
    logger.error("this is error message")
    logger.info("this is info message")


if __name__ == "__main__":
    logger_with_handlers()