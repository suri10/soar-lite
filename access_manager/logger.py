import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("access_manager")

def log_event(event):
    logger.info(event)
