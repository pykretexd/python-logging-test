import logging
import logging.handlers
import os
import sys
from datetime import datetime


def sub_logging():
    logger = logging.getLogger('subLogger')
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
        'logs/sub.log', when='midnight')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.debug('sub debug message')
    logger.info('sub info message')
    logger.warning('sub debug message')
    logger.critical('sub critical message')
    logger.error('sub error message')
