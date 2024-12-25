from datetime import datetime
import logging
import logging.handlers
import os
import sys
from time import sleep

from module_example import module_logging
from module_example.sub import sub_logging


def main():
    logger = logging.getLogger('example')
    logger.setLevel('INFO')

    if not os.path.exists('logs'):
        os.mkdir('logs')

    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s - %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S'
    )

    # Create and apply handlers for logging to console and file.
    console_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.handlers.TimedRotatingFileHandler(
        'logs/main.log', when='midnight')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('debug message')
    logger.critical('critical message')
    logger.error('error message')

    module_logging()
    sub_logging()

    while True:
        logger.info('hello world')
        sleep(4)


if __name__ == '__main__':
    main()
