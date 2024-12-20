import logging


def module_logging() -> None:
    logger = logging.getLogger('example')

    logger.debug('module debug message')
    logger.info('module info message')
    logger.warning('module debug message')
    logger.critical('module critical message')
    logger.error('module error message')
