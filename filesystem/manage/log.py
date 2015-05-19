import logging
from logging.handlers import RotatingFileHandler
from config.settings import DEFAULT_PATH, MAX_LOG_SIZE
from os.path import join

# TODO : Use Singleton for logger so only one file is ever created
logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    handlers=[RotatingFileHandler(join(DEFAULT_PATH, 'filecleaner.log'), backupCount=3, maxBytes=MAX_LOG_SIZE)],
    level=logging.DEBUG)

def log(message, log_type="ERROR"):
    if log_type == "ERROR":
        logging.error(message)
    elif log_type == "WARNING":
        logging.warning(message)
    elif log_type == "INFO":
        logging.info(message)
    elif log_type == "DEBUG":
        logging.debug(message)