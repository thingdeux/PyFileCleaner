import logging

# TODO : Use Singleton for logger so only one file is ever created
logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    filename='filecleaner.log',
    level=logging.DEBUG)

def log(message, log_type="ERROR"):
    if log_type == "ERROR":
        logging.error(message)
    elif log_type == "WARNING":
        logging.warning(message)
    elif log_type == "DEBUG":
        logging.debug(message)