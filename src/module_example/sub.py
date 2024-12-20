import logging


def sub_logging():
    logger = logging.getLogger('subLogger')

    logger.debug('sub debug message')
    logger.info('sub info message')
    logger.warning('sub debug message')
    logger.critical('sub critical message')
    logger.error('sub error message')
