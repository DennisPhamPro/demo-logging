import logging
import logging.config

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__); """create custom logger (__name__ will make this logger get default name, if make this file to module
        and access this module, logger name will be file name (file_conf_logging).)"""

logger.debug('This is a debug message')