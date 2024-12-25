from datetime import datetime
import logging
import logging.config
import os
import toml
from time import sleep

from module_example import module_logging
from module_example.sub import sub_logging


def write_default_config(fname: str) -> None:
    """Write default configurations to toml file."""
    toml_string = toml.dumps({
        'loggers': {'keys': 'root,simpleLogger'},
        'handlers': {
            'keys': 'consoleHandler,mainFileHandler,detectionFileHandler'},
        'formatters': {'keys': 'simpleFormatter'},
        'logger_root': {
            'level': 'INFO',
            'handlers': 'consoleHandler'
        },
        'logger_simpleLogger': {
            'level': 'INFO',
            'handlers': 'consoleHandler,mainFileHandler',
            'qualname': 'simpleLogger',
            'propagate': 0
        },
        'handler_consoleHandler': {
            'class': 'StreamHandler',
            'level': 'INFO',
            'formatter': 'simpleFormatter',
            'args': '(sys.stdout,)'
        },
        'handler_mainFileHandler': {
            'class': 'handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'simpleFormatter',
            'args': '(logs/main_log.log,midnight)'
        },
        'handler_detectionFileHandler': {
            'class': 'handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'simpleFormatter',
            'args': '(logs/detection_log.log,midnight)'
        },
        'formatter_simpleFormatter': {
            'format': '[%(asctime)s] %(levelname)s - %(message)s',
            'datefmt': '%Y/%m/%d %H:%M:%S'
        }
    })
    with open(fname, 'w') as file:
        # fileConfig refuses to work with values with quotation marks.
        # For that reason, remove all quotation marks.
        file.write(toml_string.replace('"', '').replace("'", ''))


def main():
    logging_config = 'logging.toml'
    if not os.path.exists(logging_config):
        write_default_config(logging_config)
    if not os.path.exists('logs'):
        os.mkdir('logs')

    try:
        logging.config.fileConfig(logging_config)
    except:
        # Configuration file was invalid. I wasn't able to find how to import
        # configparser.InterpolationSyntaxError which can be raised if
        # formatting was written incorrectly. A bare except was the cleanest solution.
        write_default_config(logging_config)

        # Try to read file again.
        logging.config.fileConfig(logging_config)
    logger = logging.getLogger('example')
    logger.setLevel('INFO')

    # Create file handler for logging to file.
    # file_handler = logging.FileHandler(
    #     '{:%Y-%m-%d}.log'.format(datetime.today()))
    # Get formatter obtained by config file.
    # formatter = logging.root.handlers[0].formatter
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)

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
