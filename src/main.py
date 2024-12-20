import logging
import logging.config
import os
import toml

from module_example import module_logging
from module_example.sub import sub_logging


def write_default_config(fname: str) -> None:
    """Write default configurations to toml file."""
    toml_string = toml.dumps({
        'loggers': {'keys': 'root,simpleLogger'},
        'handlers': {'keys': 'consoleHandler'},
        'formatters': {'keys': 'simpleFormatter'},
        'logger_root': {
            'level': 'INFO',
            'handlers': 'consoleHandler'
        },
        'logger_simpleLogger': {
            'level': 'INFO',
            'handlers': 'consoleHandler',
            'qualname': 'simpleLogger',
            'propagate': 0
        },
        'handler_consoleHandler': {
            'class': 'StreamHandler',
            'level': 'INFO',
            'formatter': 'simpleFormatter',
            'args': '(sys.stdout,)'
        },
        'formatter_simpleFormatter': {
            'format': '[%(asctime)s] %(levelname)s - %(message)s'
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

    try:
        logging.config.fileConfig(logging_config)
    except (RuntimeError, KeyError, ValueError):
        # Configuration file was invalid.
        write_default_config(logging_config)

        # Try to read file again.
        logging.config.fileConfig(logging_config)
    logger = logging.getLogger('example')

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('debug message')
    logger.critical('critical message')
    logger.error('error message')

    module_logging()
    sub_logging()


if __name__ == '__main__':
    main()
