import logging

# 1. Write a Python function to create a basic logger that logs messages to a file named `app.log`.
# 2. Modify the function to log messages of levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

def basicLogger():
    logging.basicConfig(filename='assignement_1.log', level=logging.DEBUG)
    logging.debug('This is debug message')
    logging.warning('This is warning message')
    logging.info('This is info message')
    logging.error('This is error message')
    logging.critical('This is critical error ')

if __name__ == "__main__":
    basicLogger()